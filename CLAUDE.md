# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository is the **research-repository-boilerplate** component of the [design-kit](https://github.com/igorrazvodovsky/design-kit) project. It provides a starter template for UX research repositories with templates, examples, and AI-powered tools.

### Core Philosophy

- _Markdown-first approach_: All content uses Markdown to enable seamless integration with AI tools (Claude, etc.) and human-readable tools (Obsidian)
- _Knowledge compounding_: Serves as a memory and knowledge base for other design-kit components, creating compounding value over time
- _AI-native architecture_: Designed for both human readability and machine processing

## Repository Architecture

### Content Structure

The repository is organized to balance human navigation (via Obsidian) with AI consumption:

- `templates/` - Reusable research document templates
  - `planning/` - Project checklists, sprint planning, research strategies
  - `interviews/` - Discussion guides, question templates, consent forms
  - `analysis/` - Synthesis frameworks, tag taxonomies, insight extraction
  - `outputs/` - User needs, personas, journey maps, final reports
- `examples/` - Real-world examples demonstrating template usage
- `tools/` - AI-powered utilities for research tasks
  - Synthesis and pattern detection across interviews
  - User needs extraction and categorization
  - Cross-reference mapping between hypotheses, questions, and findings
- `data/`, `information/`, `knowledge/` - placeholders

### Data Model

Research documents follow a structured data model:

#### Research Planning
- Project metadata (goals, team, timeline)
- Hypotheses and research questions (linked to research areas)
- Sprint/phase planning with task checklists
- User recruitment criteria and screening

#### Interview Management
- Participant metadata (unique IDs, segments, characteristics)
- Discussion guides (questions organized by section/theme)
- Interview transcripts with timestamps
- Tag taxonomy for coding responses

#### User Needs Tracking
- Original user needs (as stated by participants)
- Refined user needs (consistent, actionable format)
- User story format: "As a [who] [context], I need [need] so that [outcome]"
- Categorization (themes, journey stages, priority)
- Traceability (links to source research)

#### Findings & Insights
- Evidence-based findings linked to interview data
- Journey stage mapping
- Success/failure impacts and measures
- Cross-references to supporting research

### Markdown Conventions

- Use frontmatter (YAML) for metadata (research type, dates, participants, tags)
- Cross-reference related documents using `[[wiki-style]]` links for Obsidian compatibility
- Structure documents with consistent heading hierarchy for AI parsing
- Include explicit tags for categorization and retrieval
- Maintain unique IDs for all entities (participants, needs, findings) to enable cross-referencing

## Development Guidelines

### File Creation

When creating new templates or examples:
- Include frontmatter with: `title`, `type`, `project`, `status`, `tags`, `created`, `updated`
- For research artifacts, add: `unique_id`, `participant_id` (if applicable), `research_phase`
- Follow the existing template structure for consistency
- Add cross-references to related documents using `[[document-name]]` syntax
- Document AI prompts or workflows in a dedicated section

### Data Integrity

Maintain structured relationships:
- Assign unique IDs to all research entities (use format: `USR001`, `NEED042`, `HYP05`, etc.)
- Link interview responses to research questions and hypotheses
- Connect user needs to source interviews and findings
- Track refinement history (original vs. refined user needs)

### Knowledge Base Maintenance

When adding to `knowledge/`:
- Extract reusable patterns and insights
- Link back to source research documents
- Tag with methodology, domain, or pattern type
- Include success/failure metrics when available
- Update related design-kit components when patterns emerge
