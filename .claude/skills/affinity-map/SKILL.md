---
name: affinity-map
description: Create or capture an affinity map in Obsidian (solo mode) or parse/capture a workshop affinity map into a traceable `2-information/` artifact (workshop mode).
---

# Affinity Map Skill

## Purpose

Turn many observations into a small set of evidence-backed themes, either by:
- **Solo build** (Obsidian + Codex), or
- **Workshop parse/capture** (team workshop output → Obsidian artifact)

## Inputs

Always needed:
- Focus question (or decision to inform)

Solo mode needs:
- A set of source notes in `2-information/` (paths or a folder)

Workshop mode needs:
- A workshop capture note and/or exported sticky text (Markdown list, CSV/JSON export, or screenshots the user can attach)
- OneDrive paths for raw artifacts (don’t commit raw exports/screenshots if they contain PII)

If missing, ask up to **three** clarifying questions total:
1) Which mode: solo or workshop?
2) What is the focus question?
3) Where are the inputs (paths/attachments)?

## Workflow A — Solo (Obsidian + Codex)

1) Confirm focus question + scope (what’s in/out).
2) Create a new working note in `2-information/` using `templates/affinity-map.md` with `mode: solo`.
   - Filename: `2-information/YYYY-MM-DD-affinity-map-<topic>.md`
3) Extract **atomic observation cards** from the input notes.
   - Each card must include a link to the source note (and timestamp/page when available).
4) Cluster cards by affinity and label clusters (short noun phrases).
5) Optionally group clusters into 3–7 higher-order themes.
6) Write candidate implications as hypotheses (separate section).
7) Create `projects/<Project>/affinity-map.canvas` if spatial navigation would help.

## Workflow B — Workshop (team) → Codex parse/capture

1) Confirm focus question + what “the map” represents (topics, participants, time window).
2) Identify workshop artifacts:
   - Prefer a Markdown note containing the stickies/cluster labels, or a CSV export.
   - If only screenshots exist, ask the user to attach them; then extract text.
3) Create a new working note in `2-information/` using `templates/affinity-map.md` with `mode: workshop`.
4) Capture/parse results:
   - Preserve original cluster labels where possible
   - Capture “parking lot”/outliers explicitly
   - Add traceability: link to the workshop capture note + OneDrive artifact paths
5) Create `projects/<Project>/affinity-map.canvas` to recreate the workshop map for navigation.

## Quality checks (must pass)

- Traceability: every cluster has evidence links (solo) or artifact links (workshop) plus any available source links.
- Separation: clusters/themes ≠ implications (keep conclusions separate).
- Coverage: call out missing slices (user types, stages, contexts).
- Privacy: remove names/PII; keep raw exports in OneDrive references.

## Related

- Method: `methods/affinity map.md`
- Template: `templates/affinity-map.md`
- Useful skills: `obsidian-markdown`, `json-canvas`, `sensemaking-synthesis`
