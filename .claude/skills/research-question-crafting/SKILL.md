---
name: research-question-crafting
description: Craft, refine, and validate actionable user research questions for design projects. Use when a designer has a project in `projects/` and needs to write or improve a research question, including turning a draft into a focused, decision-linked question and capturing it in project notes.
---

# Research Question Crafting Skill

## Workflow

1) Locate the project
- Identify the target `projects/<Project>/` folder from the user request or recent context.
- Open `problem.md`, `solution.md`, `plan.md`, `README.md`, and any linked notes in that project.
- Search for existing questions: `rg -n "research question|question" projects/<Project>`.

2) Extract context
- Capture: decision to inform, target audience, environment/context, time horizon, constraints, success criteria, known hypotheses or assumptions.
- If any of these are missing and needed, ask up to three clarifying questions.

3) Craft or refine the question
- If a draft exists, point out issues (scope, bias, actionability, feasibility) and rewrite it.
- Produce 1-3 candidate questions; vary angle if helpful (behavioral, needs, viability).
- Prefer neutral "What/How/Why" wording; avoid leading solutions or baked-in metrics.
- Ensure each question implies a decision (finish: "...so we can decide...").

4) Write back to the project
- Default file: `projects/<Project>/research question.md` (create if missing).
- If the project already stores questions elsewhere, update that note instead and add a `[[research question]]` link from the main project note if appropriate.
- Use a short structure:
  - `# Research question`
  - `## Draft`
  - `## Final`
  - `## Rationale` (1-2 bullets)
  - `## Assumptions to test` (bullets)
- Use Markdown and Obsidian `[[wiki-links]]` to related project notes.

## Quality checklist
- Decision-linked: can you finish "So we can decide..."?
- Focused: one problem slice, not the whole product.
- Answerable: feasible with available methods and time.
- Neutral: avoids solution or metric bias.
- Audience-specific: names the user/group and context.

## Templates and examples
- See `references/question-patterns.md` for wording patterns and sample rewrites.
