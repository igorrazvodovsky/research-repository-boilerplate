# Information

_Organized, tagged, and contextualized research data_

This directory transforms raw data into meaningful, structured information through analysis and organization. It's where you make sense of what you collected.

## What Goes Here

### Interview Analysis
- **Tagged excerpts** - Key quotes and observations organized by theme/tag
- **Question-answer mappings** - Responses organized by research question
- **Tag taxonomy** - Categorization scheme for coding responses
- **Pattern documentation** - Recurring themes identified across sessions

### User Needs
- **Original user needs** - Needs as expressed by participants
- **Refined user needs** - Standardized format: "As a [who] [context], I need [need] so that [outcome]"
- **Need categorization** - Organized by theme, journey stage, priority
- **Traceability matrix** - Links needs back to source interviews

### Research Findings
- **Evidence-based findings** - Specific discoveries with supporting data
- **Hypothesis validation** - Research questions answered with evidence
- **Journey stage mapping** - Where findings apply in user journey
- **Segmentation analysis** - How findings differ across user types

### Synthesis Documents
- **Affinity maps** - Thematic grouping of observations
- **Mental models** - How users think about the domain
- **Pain points catalog** - Documented frustrations with evidence
- **Opportunity areas** - Gaps and potential improvements identified

## Structure

Organize by research phase or theme:

```
information/
├── project-name/
│   ├── interviews/
│   │   ├── tagged-responses.md
│   │   ├── tag-taxonomy.md
│   │   └── question-answer-matrix.md
│   ├── user-needs/
│   │   ├── needs-master-table.md
│   │   ├── needs-by-category.md
│   │   └── needs-by-journey-stage.md
│   ├── findings/
│   │   ├── hypothesis-01-validation.md
│   │   └── key-findings.md
│   └── analysis/
│       ├── affinity-map.md
│       └── pain-points.md
```

## From Data to Information

This is where you add context and meaning:
- **Tag and code** raw interview data
- **Categorize and group** related observations
- **Refine and standardize** user needs
- **Link evidence** to findings
- **Map relationships** between different research elements

## Cross-Referencing

Use unique IDs to maintain traceability:
- Link findings to source data: `[USR001]`, `[Interview 2024-01-15]`
- Connect needs to hypotheses: `[HYP03]`, `[RQ-12]`
- Reference journey stages: `[Discovery]`, `[Evaluation]`

## Analysis

- Consistent tagging across documents
- Explicit links between related concepts
- Metadata-rich frontmatter
- Standardized user story format

## Moving Up the Hierarchy

Information in this folder becomes the input for:
- **Knowledge** (synthesized insights, patterns, principles)

Think: _"What does it mean?"_ → Information answers this question.
