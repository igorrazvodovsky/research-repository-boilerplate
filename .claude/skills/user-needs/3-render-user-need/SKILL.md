---
name: render-user-need
description: Transform extracted needs into properly formatted markdown files with correct IDs and metadata
type: user
---

# Render User Need

## Purpose

Transform extracted need information into properly formatted markdown files following the user-need template structure. Handle ID assignment, filename creation, and metadata consistency.

## When to Use This Skill

Invoke this skill when:
- The user asks to create, render, or document user needs as files
- Converting extracted/validated needs into the standard template format
- Batch creating need files from research analysis
- The user wants to save needs to the needs collection

## Inputs

- Extracted need data (from research analysis)
- Existing needs collection (for ID assignment and consistency checking)
- Template: `templates/user-need.md`

## Skill

### File Naming Convention

The filename is derived directly from the "I need to" statement:

**Format:** `[I need to text].md`

**Rules:**
- Use exact text from "I need to" field
- Lowercase
- Keep spaces (do not replace with dashes)
- Examples:
  - "see only my assigned projects" → `see only my assigned projects.md`
  - "return to my previous view quickly" → `return to my previous view quickly.md`
  - "prove my identity securely" → `prove my identity securely.md`

### ID Assignment

**Process:**
1. Use **Glob** to count existing needs:
   ```
   pattern: "example-1/outputs/needs/*.md"
   ```
2. Count the matches
3. Next ID = count + 1
4. Format as string (e.g., `"42"`)

**Important:** IDs are sequential integers, formatted as strings in YAML frontmatter.

### Field-by-Field Rendering

#### Required Fields

**ID** (string)
- Format: `ID: "42"`
- Sequential number starting from 1
- Always quoted in YAML

**user type** (wiki-link)
- Format: `user type: "[[type-name]]"`
- High-level category for grouping
- Common types: `[[user]]`, `[[admin]]`, `[[team-member]]`, `[[guest]]`
- Check existing types before creating new:
  ```
  Grep: pattern="user type:" output_mode="content"
  ```
- Reuse existing types for consistency

**as a** (plain text)
- Format: `as a: specific role description`
- More specific than user type
- Examples: `teammate`, `project contributor`, `frequent user`, `admin`
- Keep to 5-10 distinct roles across the entire need set

**who is** (plain text, optional)
- Format: `who is: cross-cutting qualifier`
- Use when context matters
- Examples: `invited by an admin`, `managing multiple workspaces`, `with accessibility needs`
- Leave blank if not needed (don't omit the field)

**I need to** (plain text)
- Format: `I need to: action or capability`
- THIS BECOMES THE FILENAME
- Solution-agnostic
- Specific and action-oriented
- Examples: `search for relevant items`, `save my work`, `see who is online`

**so that** (plain text)
- Format: `so that: goal or outcome`
- Different level from "I need to" (not circular)
- Focus on user's goal, not system behavior
- Examples: `I can meet project deadlines`, `I don't lose progress if interrupted`

**user journey stage** (wiki-link)
- Format: `user journey stage: "[[stage-name]]"`
- Where in the journey this need occurs
- Common stages: `[[discovery]]`, `[[registration]]`, `[[daily-use]]`, `[[collaboration]]`, `[[offboarding]]`
- Check existing stages:
  ```
  Grep: pattern="user journey stage:" output_mode="content"
  ```

#### Optional Fields

**category** (plain text)
- Format: `category: bucket-name` or `category:` (blank)
- High-level grouping: `navigation`, `access`, `collaboration`
- Often left blank initially, filled during refinement
- If blank, include the field with no value

**theme** (plain text)
- Format: `theme: conceptual-thread` or `theme:` (blank)
- Conceptual patterns: `findability`, `efficiency`, `security`, `trust`
- Often left blank initially, filled during pattern analysis
- If blank, include the field with no value

**customer journey stage** (plain text)
- Format: `customer journey stage: stage-name` or leave blank
- Optional alternative perspective to user journey stage
- Usually left blank
- If blank, include the field with no value

### Template Structure

```yaml
---
ID: "[sequential-number]"
user type: "[[type]]"
as a: [specific role]
who is: [qualifier or blank]
I need to: [capability statement]
so that: [goal/outcome]
category: [optional grouping or blank]
theme: [optional conceptual thread or blank]
user journey stage: "[[stage-name]]"
customer journey stage: [optional or blank]
---
```

### Consistency Checks

Before writing the file:

**1. Check for duplicates**
```
Grep: pattern="I need to: [your need text]"
path: "example-1/outputs/needs"
output_mode: "files_with_matches"
```

If found, this may be a duplicate. Review before creating.

**2. Verify user type exists**
```
Grep: pattern="user type:.*\\[\\[[your-type]\\]\\]"
path: "example-1/outputs/needs"
output_mode: "files_with_matches"
```

If no matches, you're creating a new type. Ensure it's intentional.

**3. Verify journey stage exists**
```
Grep: pattern="user journey stage:.*\\[\\[[your-stage]\\]\\]"
path: "example-1/outputs/needs"
output_mode: "files_with_matches"
```

If no matches, you're creating a new stage. Ensure it's intentional.

### Writing the File

Use **Write** tool with:
- `file_path`: `example-1/outputs/needs/[I need to text].md`
- `content`: YAML frontmatter following template structure

**Example:**
```
Write:
  file_path: "example-1/outputs/needs/see only my assigned projects.md"
  content: |
    ---
    ID: "23"
    user type: "[[team-member]]"
    as a: project contributor
    who is: working on multiple projects
    I need to: see only my assigned projects
    so that: I can focus on my work without distraction
    user journey stage: "[[daily-use]]"
    category:
    theme:
    customer journey stage:
    ---
```

## Common Rendering Patterns

### Discovery/Learning Need
```yaml
---
ID: "[next-id]"
user type: "[[user]]"
as a: new user
who is: unfamiliar with the system
I need to: understand what I can accomplish
so that: I can determine if this meets my needs
user journey stage: "[[discovery]]"
category:
theme:
customer journey stage:
---
```

### Access/Permission Need
```yaml
---
ID: "[next-id]"
user type: "[[user]]"
as a: authorized user
who is:
I need to: prove my identity securely
so that: I can access protected features
user journey stage: "[[registration]]"
category:
theme:
customer journey stage:
---
```

### Task Completion Need
```yaml
---
ID: "[next-id]"
user type: "[[user]]"
as a: [specific-role]
who is:
I need to: [perform-action]
so that: I can accomplish [specific-goal]
user journey stage: "[[daily-use]]"
category:
theme:
customer journey stage:
---
```

### Efficiency Need
```yaml
---
ID: "[next-id]"
user type: "[[user]]"
as a: frequent user
who is:
I need to: [do-something] quickly
so that: I can complete work efficiently
user journey stage: "[[daily-use]]"
category:
theme:
customer journey stage:
---
```

### Collaboration Need
```yaml
---
ID: "[next-id]"
user type: "[[team-member]]"
as a: [collaborative-role]
who is: working with others
I need to: [share/coordinate/communicate]
so that: my team can work together effectively
user journey stage: "[[collaboration]]"
category:
theme:
customer journey stage:
---
```

## Batch Rendering

When rendering multiple needs:

1. Get ID for first need (count existing + 1)
2. Render first need with that ID
3. For each subsequent need, increment ID by 1
4. Track which user types and stages you're creating
5. After all renders, verify consistency

## Output

Individual `.md` files in `example-1/outputs/needs/` with:
- Sequential IDs
- Consistent user types and journey stages
- Proper filename derived from "I need to"
- Complete YAML frontmatter
- No content below frontmatter (just the `---` block)

## Bundled Resources

### Assets

- **user-need-template.md** — The template file defining the structure for user need files

Use **Read** tool to access the template at `.claude/skills/user-needs/3-render-user-need/assets/user-need-template.md`, then use **Write** tool to create new need files following this structure.

## Related Skills

- `extract-needs-from-research` — Get need data to render
- `validate-need-quality` — Ensure need is ready to render
- `identify-need-patterns` — Analyze rendered needs for themes
