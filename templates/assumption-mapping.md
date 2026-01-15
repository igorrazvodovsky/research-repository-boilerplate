Copy this template when creating a new assumption mapping note (typically in `2-information/` until reviewed/synthesized).

```markdown
---
type:
  - report
  - assumptions
status:
  - draft
project: Project / study name
date: YYYY-MM-DD
environment: Where/when this was done (e.g., "Mural workshop", "Async review in Obsidian")
audience: Who this is for (e.g., "Product team", "Research", "Leadership")
lens: The lens used (e.g., "Discovery", "Delivery", "Value prop", "Go-to-market")
scope: What is included / excluded
facilitator: Name(s)
participants: [Name / role, Name / role]
inputs:
  - "[[2-information/...]]"
  - "OneDrive: /path/to/1-data/artifact"
outputs:
  - "[[3-knowledge/...]]"
  - "[[4-insights/...]]"
structure:
  summary-note: "projects/<Project>/assumptions.md"
  assumption-notes: "projects/<Project>/assumptions/"
  canvas: "projects/<Project>/assumptions.canvas"
tags:
  - "#assumptions"
  - "#workshop"
aliases: []
---

# Assumption map — Topic / bet

## Goal

What decision(s) this assumption map should inform and by when.

## Definitions (shared language)

- **Assumption**: A belief that must be true for a plan/idea to work.
- **Type**: What kind of risk it is:
  - **Desirability**: Do people want it / will they use it?
  - **Feasibility**: Can we build/operate it with our constraints?
  - **Viability**: Does it work for the business/strategy (costs, ROI, governance)?
- **Impact**: If false, how much it damages outcomes (Low/Medium/High).
- **Uncertainty**: How confident we are it’s true today (Low/Medium/High).

## Sources / inputs (evidence trail)

Link to what informed this map (keep raw artifacts in `1-data/` via OneDrive paths; keep notes in `2-information/`):

- [[2-information/...]] — why it matters
- OneDrive: /path/to/1-data/... — why it matters

## Assumptions (linked notes)

Create one note per assumption under `projects/<Project>/assumptions/`, then list them here to avoid duplication and make them reusable.

Recommended filename pattern:
- `projects/<Project>/assumptions/<short-slug>.md` (hyphenated; avoid spaces to reduce link churn)

Assumptions table:
- Prefer Markdown links for readability in tables.
- Avoid `[[wikilinks|with aliases]]` inside tables: the `|` breaks Markdown table columns.

| Assumption | Type | Impact | Uncertainty | Notes |
|---|---|---|---|---|
| [Short readable title](projects/<Project>/assumptions/<short-slug>.md) | Desirability/Feasibility/Viability | High | High | Why it’s risky / what could fail |
| [Another assumption](projects/<Project>/assumptions/<short-slug>.md) |  | Medium | High |  |

## Map (Impact × Uncertainty)

Optional but recommended: create an Obsidian Canvas at `projects/<Project>/assumptions.canvas` and place assumption **file nodes** in the 2×2.

Embed here:

![[projects/<Project>/assumptions.canvas]]

|  | **High uncertainty** | **Low uncertainty** |
|---|---|---|
| **High impact** | **Riskiest (test first)**: … | **Key constraints (monitor)**: … |
| **Low impact** | **Explore (nice-to-know)**: … | **Safe assumptions (don’t over-test)**: … |

## Riskiest assumptions (prioritized)

Pick the smallest set that, if false, would force a major rethink.

1. …
2. …
3. …

## Tests / how we’ll reduce uncertainty

| Assumption | Test | Method | Success criteria | Timeframe | Owner | Status |
|---|---|---|---|---|---|---|
| [Assumption link](projects/<Project>/assumptions/<short-slug>.md) |  | Interview / Prototype / Analytics / Desk research | What would convince us | Days/weeks |  | Planned/In progress/Done |

## Decision implications

If the top assumptions hold, what do we do next? If they fail, what changes?

- If … holds → …
- If … fails → …

## Context-bridging links

Connect to adjacent domains with an “applies when…” note.

- [[Related topic]] — applies when …
- [[Related decision]] — applies when …

## Next steps

- [ ] Create/attach missing source notes in `2-information/` for any unsupported assumptions
- [ ] Create one note per assumption in `projects/<Project>/assumptions/`
- [ ] Build/update `projects/<Project>/assumptions.canvas` with assumption file nodes
- [ ] Run/assign tests for the riskiest assumptions
- [ ] Synthesize outcomes into [[3-knowledge/...]] (cite this note + supporting sources)
- [ ] If warranted, write recommendations in [[4-insights/...]] (cite knowledge items)
```

---

## Usage notes

- **Default placement**: Put workshop outputs in `2-information/` until reviewed and synthesized.
- **One assumption per note**: Keep assumptions atomic; split compound statements.
- **Evidence required**: Every high-impact assumption should point to at least one source note or artifact.
- **Make it falsifiable**: Prefer observable signals over opinions (“we’ll know when…”).
- **Keep links healthy**: Use `[[wiki-links]]` and add “applies when…” context near cross-links.
- **Tables are picky**: Avoid `[[wikilinks|with aliases]]` inside Markdown tables; use Markdown links instead.

---

## Assumption note template (one per assumption)

```markdown
---
type:
  - assumption
status:
  - draft
project: Project / study name
date: YYYY-MM-DD
assumption-type: Desirability/Feasibility/Viability
impact: High/Medium/Low
uncertainty: High/Medium/Low
tags:
  - "#assumptions"
---

# Assumption — short title

## Assumption

We believe **[actor]** will **[behavior]** because **[reason]**.

We’ll know we’re right if **[observable signal]**; wrong if **[counter-signal]**.

## Why it matters

What breaks / changes if this is false.

## Evidence / rationale

- [[2-information/...]] — why this supports the assumption
- OneDrive: /path/to/1-data/... — raw artifact

## How to test

- Test idea 1
- Test idea 2
```
