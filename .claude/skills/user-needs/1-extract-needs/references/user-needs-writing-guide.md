A reference for writing clear, actionable user needs based on research insights.

> **For practical execution:** See commands [`sketch-user-needs.md`](commands/discovery/research/process/sketch-user-needs.md) and [`refine-user-needs.md`](commands/discovery/research/process/refine-user-needs.md)

## Your Setup

This guide is for humans using:
- **Format:** Individual .md files per user need (one file per need)
- **Tool:** Obsidian with **Bases** plugin for interactive database management
- **Structure:** YAML frontmatter with standardized fields
- **Links:** Wiki-links like `[[user]]` and `[[registration]]` create navigable relationships
- **Location:** Need files stored in `example-1/outputs/needs/`
- **Template:** Use `templates/user-need.md` for consistency

## Terminology: User Needs vs User Stories

While both terms are used interchangeably, _user need_ is preferred over _user story_ because:

- User stories are used beyond user research contexts
- "Need" helps focus creation on what users actually need, not what they want
- The terminology reinforces a focus on fundamental requirements rather than feature requests

**Need** = fundamental capability required to accomplish a goal
**Want** = desire for a specific solution or feature

## The User Need Format

### Standard Structure

The traditional user need format is: **As a [role] / I need to [action] / So that [outcome]**

### Enhanced Structure with "Who is"

A more flexible approach splits the "As a" into two parts:

**As a [primary user type] / Who is [qualifier] / I need to [action] / So that [outcome]**

#### Why Split "As a"?

- **As a** — Keep consistent high-level user types (easier to group and filter in Bases)
- **Who is** — Capture cross-cutting secondary characteristics

**Examples:**
- As a: **teammate** / Who is: **invited by an admin**
- As a: **user** / Who is: **with accessibility needs**
- As a: **admin** / Who is: **managing multiple workspaces**

This separation allows you to:
- Maintain a limited, manageable set of primary user types
- Still capture important contextual variations
- Filter in Bases by either primary type or secondary characteristics
- Find all needs for users "with accessibility needs" across all types

## Core Writing Principles

### 1. Focus on Needs, Not Wants

**Need** describes a fundamental capability.
**Want** prescribes a specific solution.

Users need to accomplish goals. They may want specific features, but those are solutions, not needs.

**Examples:**
- ❌ "I want a dashboard with graphs"
- ✓ "I need to see my progress at a glance so that I can stay on track"

### 2. Distinguish Actions from Outcomes

The "I need to" should never duplicate the "So that." They exist at different levels:

- **I need to:** Immediate action or capability
- **So that:** Higher-level goal or benefit

**Example:**
- ❌ Need: "save my work" / Outcome: "my work is saved" (circular)
- ✓ Need: "save my work" / Outcome: "I don't lose progress if interrupted"

### 3. Be Goal-Oriented

Every user need should trace back to a meaningful user goal. If the "So that" feels trivial or circular, dig deeper to find the real outcome.

**Ask yourself:**
- Why does the user need this capability?
- What changes for them when this need is met?
- What can they accomplish that they couldn't before?

### 4. Avoid Solution Specification

Needs should be technology-agnostic and implementation-independent.

**Examples:**
- ❌ "I need to have a blue button on the homepage"
- ✓ "I need to quickly access my saved work so that I can resume tasks efficiently"

The first prescribes a solution. The second describes a need that designers can address in various ways.

### 5. Keep User Types Consistent

Standardizing user types makes it easier to:
- Group related needs in Obsidian Bases
- Identify gaps in coverage
- Present findings to stakeholders
- Filter and analyze your research

**In Obsidian:**
- Create user type notes (e.g., `user.md`, `admin.md`, `teammate.md`)
- Link to them from need frontmatter: `user type: "[[user]]"`
- Use Bases backlinks to see all needs for a type

## Working in Obsidian Bases

### Setting Up Your Needs Base

1. **Enable Bases plugin** in Obsidian settings (core plugin)
2. **Create a new Base** pointing to `example-1/outputs/needs`
3. **Configure visible properties:**
   - ID
   - user type
   - as a
   - who is
   - I need to
   - so that
   - category
   - theme
   - user journey stage

4. **Create views for different perspectives:**
   - "All Needs" - no filters, sorted by ID
   - "By User Type" - filter by `user type` field
   - "By Journey Stage" - group by `user journey stage`
   - "Unprocessed" - filter where `category` is empty
   - "By Outcome" - sort by `so that` to spot similar goals

### Creating Needs in Obsidian

**Using the template:**
1. Use Templater or manually copy `templates/user-need.md`
2. Fill in frontmatter fields
3. Name file to match "I need to" field exactly
4. Place in `example-1/outputs/needs/`
5. The need automatically appears in your Bases views

**Inline editing:**
- Click into any property cell in Bases view
- Edit directly without opening the file
- Changes save to frontmatter automatically

### Finding and Filtering Needs

**By user type:**
1. Open user type note (e.g., `[[user]]`)
2. Check backlinks panel
3. See all needs linking to this type

**By journey stage:**
1. Open stage note (e.g., `[[registration]]`)
2. Check backlinks panel
3. See all needs at this stage

**In Bases:**
- Click column headers to sort
- Use filter button to filter by any property
- Create saved views for common filters
- Group by category or theme to see patterns

### Analysis Workflows

**Identifying patterns:**
1. Create a Bases view sorted by "so that"
2. Scroll through to see common outcomes
3. Note needs with identical or similar goals

**Finding gaps:**
1. Create view grouped by "user journey stage"
2. Count needs in each group
3. Identify stages with few needs

**Checking coverage:**
1. Create view filtered by each user type
2. Count needs per type
3. Ensure all key users are represented

## Common Patterns

Understanding common patterns helps you recognize and articulate needs quickly.

### Discovery Needs
Users exploring or learning about the system.

**Pattern:** "As a [user type] who is [exploring/new], I need to [understand/learn/discover] so that [I can determine if this meets my needs]"

**Example:**
- As a: new user
- Who is: evaluating the platform
- I need to: understand what I can accomplish
- So that: I can determine if this meets my needs

### Task Completion Needs
Users performing specific actions to achieve goals.

**Pattern:** "As a [user type], I need to [perform action] so that [I can accomplish goal]"

**Example:**
- As a: team member
- I need to: complete my assigned tasks
- So that: I can contribute to project success

### Access and Permission Needs
Users gaining entry or authorization.

**Pattern:** "As a [user type] who is [qualified], I need to [gain access/verify identity] so that [I can use protected features]"

**Example:**
- As a: team member
- Who is: authorized by an admin
- I need to: prove my identity securely
- So that: I can access confidential project data

### Efficiency Needs
Users wanting to complete work faster or easier.

**Pattern:** "As a [user type], I need to [do something quickly/easily] so that [I can complete work efficiently]"

**Example:**
- As a: frequent user
- I need to: find what I'm looking for quickly
- So that: I don't waste time searching

### Collaboration Needs
Users working with others.

**Pattern:** "As a [user type], I need to [share/coordinate/communicate] so that [team can work together effectively]"

**Example:**
- As a: team member
- I need to: share my work with colleagues
- So that: we can collaborate effectively

## Validation Checklist

Use this checklist to validate each user need:

- [ ] Describes a capability, not a solution?
- [ ] "I need to" and "so that" are at different levels (not duplicates)?
- [ ] Based on research evidence, not assumptions?
- [ ] Specific enough to validate with users?
- [ ] Technology-agnostic (doesn't prescribe implementation)?
- [ ] Testable (could determine if it's met)?
- [ ] Filename matches "I need to" field exactly?
- [ ] Uses wiki-links for user types and journey stages?
- [ ] Frontmatter is complete and properly formatted?

## Tips for Writing Quality Needs

### Listen for the Real Need

When users say "I want X feature," dig deeper:
- "What would that enable you to do?"
- "What goal are you trying to accomplish?"
- "What happens if you can't do this?"

### Avoid Common Pitfalls

**Circular outcomes:**
- ❌ "I need to manage permissions so that permissions are managed"
- ✓ "I need to manage permissions so that sensitive data stays secure"

**Solution specification:**
- ❌ "I need to have email notifications"
- ✓ "I need to know when something requires my attention so that I can respond promptly"

**Vague outcomes:**
- ❌ "I need to use the system so that I can work"
- ✓ "I need to track project progress so that I can meet deadlines"

### Use Concrete Language

Be specific about actions and outcomes:
- ✓ "find relevant documents quickly"
- ✗ "access information"

- ✓ "collaborate with team members on shared goals"
- ✗ "work together"

## Examples from Your Repository

See `example-1/outputs/needs/` for real examples:

**[[accept an invite and land in the correct workspace]]**
```yaml
---
ID: "8"
user type: "[[user]]"
as a: teammate
who is: invited by an admin
I need to: accept an invite and land in the correct workspace
so that: I see the right data and teammates
user journey stage: "[[registration]]"
---
```

**What makes this good:**
- Clear user context ("invited by an admin")
- Specific action ("accept invite and land in correct workspace")
- User-focused outcome ("I see the right data")
- Not prescriptive about how invitation works

## Next Steps

**For executing the process:**
- Use [`sketch-user-needs.md`](commands/discovery/research/process/sketch-user-needs.md) command for step-by-step extraction
- Use [`refine-user-needs.md`](commands/discovery/research/process/refine-user-needs.md) command for analysis and refinement

**For deeper methodology:**
- See [[user-needs-refinement-process]] for systematic refinement approach
- See [[user-needs-best-practices]] for team workflows and maintenance

## References

- Based on GDS (Government Digital Service) principles for user needs
- Adapted from Jonathan Richardson's user needs refinement methodology
- Source: "User needs refinement — why and how to do it" (2020)
