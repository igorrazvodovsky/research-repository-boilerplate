#!/usr/bin/env python3
"""
Convert WebVTT transcripts to Markdown, merging consecutive cues by speaker with sane block sizing.

Dependencies:
    pip install webvtt-py
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple

import webvtt


def normalize_text(text: str) -> str:
    # Strip speaker tags, flatten whitespace.
    text = text.replace("\n", " ").strip()
    # Remove leading <v Speaker>
    if text.lower().startswith("<v"):
        closing = text.find(">")
        if closing != -1:
            text = text[closing + 1 :]
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_speaker_and_text(cue_text: str) -> Tuple[str, str]:
    lines = cue_text.splitlines()
    if not lines:
        return "Unknown", ""
    first_line = lines[0]
    match = re.match(r"<v\s*([^>]*)>", first_line, re.IGNORECASE)
    if match:
        speaker = match.group(1).strip() or "Unknown"
    else:
        speaker = "Unknown"
    normalized = normalize_text(cue_text)
    return speaker, normalized


def merge_cues(
    cues: Iterable[webvtt.Caption],
    max_chars: int,
) -> List[Tuple[str, str, str]]:
    """
    Return a list of (speaker, start_time, merged_text) tuples.
    max_chars: soft cap per block; 0 disables splitting by length.
    """
    merged: List[Tuple[str, str, str]] = []
    current_speaker: Optional[str] = None
    current_start: Optional[str] = None
    current_segments: List[str] = []

    for cue in cues:
        speaker = cue.voice or extract_speaker_and_text(cue.raw_text)[0]
        text = normalize_text(cue.raw_text)
        if not text:
            continue
        next_len = len(" ".join(current_segments + [text]))
        needs_split = max_chars > 0 and current_segments and next_len > max_chars
        if speaker == current_speaker and not needs_split:
            current_segments.append(text)
        else:
            if current_speaker is not None:
                merged_text = " ".join(current_segments)
                merged.append((current_speaker, current_start or "", merged_text))
            current_speaker = speaker
            current_start = cue.start
            current_segments = [text]

    if current_speaker is not None and current_segments:
        merged_text = " ".join(current_segments)
        merged.append((current_speaker, current_start or "", merged_text))

    return merged


def to_markdown(
    blocks: Sequence[Tuple[str, str, str]], with_time: bool = False
) -> str:
    lines: List[str] = []
    for speaker, start_time, text in blocks:
        prefix = f"**{speaker}:**"
        if with_time and start_time:
            prefix = f"{prefix} ({start_time})"
        lines.append(f"{prefix} {text}")
    return "\n\n".join(lines)


def convert_file(
    input_path: Path,
    output_path: Optional[Path],
    with_time: bool,
    max_chars: int,
) -> None:
    try:
        cues = list(webvtt.read(str(input_path)))
    except Exception as exc:  # noqa: BLE001
        raise SystemExit(f"Failed to read VTT file: {exc}")

    blocks = merge_cues(cues, max_chars=max_chars)
    markdown = to_markdown(blocks, with_time=with_time)

    if output_path:
        output_path.write_text(markdown, encoding="utf-8")
    else:
        sys.stdout.write(markdown + ("\n" if markdown and not markdown.endswith("\n") else ""))


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert WebVTT transcripts to Markdown, merging consecutive cues by speaker."
    )
    parser.add_argument("input", type=Path, help="Path to .vtt file")
    parser.add_argument(
        "-o", "--output", type=Path, help="Optional output .md path (default: stdout)"
    )
    parser.add_argument(
        "--with-time",
        action="store_true",
        help="Include the first timestamp for each speaker block",
    )
    parser.add_argument(
        "--max-chars",
        type=int,
        default=800,
        help="Soft maximum characters per speaker block before starting a new one (0 disables)",
    )
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> None:
    args = parse_args(argv)
    convert_file(
        args.input,
        args.output,
        with_time=args.with_time,
        max_chars=args.max_chars,
    )


if __name__ == "__main__":
    main()
