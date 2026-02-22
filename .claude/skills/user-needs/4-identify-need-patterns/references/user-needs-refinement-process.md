A systematic approach to organising, categorising, and analysing user needs to uncover insights and gaps.

## Your Setup

This guide is adapted for use with:
- **Format:** Individual .md files per user need (one file per need)
- **Tool:** Obsidian with **Bases** plugin for database-like management
- **Structure:** YAML frontmatter in each .md file
- **Links:** Wiki-links to create relationships between needs, user types, and journey stages
- **Analysis:** Obsidian Bases for filtering, sorting, and multiple views

Instead of a traditional database (Airtable/Coda), you're using:
- Individual markdown files with frontmatter
- **Obsidian Bases** as your interactive database interface
- Wiki-links as your "relationships"
- Folder organization and tags for grouping
- Bases views for analysis and reporting (no code required)

**Why Bases is ideal for user needs:**
- Visual, interactive interface like Airtable/Coda
- Filter by any property (user type, journey stage, category)
- Create multiple views for different perspectives
- Edit properties inline
- Sort and organize visually
- No programming knowledge required (unlike Dataview)
- Data stays in plain markdown files

## Why Refine User Needs?

Refinement transforms a collection of user needs into a structured knowledge base that:

- Reveals patterns and themes across research
- Identifies duplicates and gaps
- Makes needs easier to search, filter, and group
- Enables deeper analysis and insight discovery
- Creates consistency across projects and teams
- Facilitates stakeholder communication

## The Three-Part Refinement Process

### Part 1: Standardize the Structure

Focus on making all needs follow the consistent format:
**As a / Who is / I need to / So that**

**Tasks:**
1. Split combined "As a" fields into "As a" and "Who is" where appropriate
2. Ensure "I need to" focuses on needs, not wants
3. Verify "So that" articulates the ultimate goal, not just restating the need
4. Remove obvious non-needs (feature requests, implementation details)
5. Eliminate or merge duplicates

**Outcome:** All needs follow a consistent structure that makes them comparable and analyzable.

### Part 2: Tag and Categorize

Add metadata to enable grouping, filtering, and analysis.

**Key activities:**
1. Assign standardized user types
2. Create category groupings (epics)
3. Map needs to journey stages
4. Identify themes
5. Link to source projects/research

**Outcome:** Needs are enriched with metadata that enables multi-dimensional analysis.

### Part 3: Review for Insights

Analyze the structured, tagged needs to discover patterns and gaps.

**Analysis approaches:**
1. Group by outcome to find similar needs
2. Group by journey stage to identify coverage gaps
3. Group by user type to understand different perspectives
4. Count needs per category to spot imbalances
5. Look for orphaned or singleton categories

**Outcome:** Actionable insights about user needs coverage, gaps, and priorities.

## File-Based Structure in Obsidian

Instead of database columns, you use YAML frontmatter fields in each .md file.

### Essential Frontmatter Fields

Based on your template at `templates/user-need.md`:

#### ID
```yaml
ID: "8"
```
- Unique identifier for each need
- Enables consistent references even if the text changes
- Use sequential numbering or any unique scheme

#### user type
```yaml
user type: "[[user]]"
```
- Wiki-link to user type definition
- Creates relationship in Obsidian graph
- View all needs for a user type via backlinks

**In your setup:**
- Use wiki-links like `[[user]]`, `[[admin]]`, `[[teammate]]`
- This creates a navigable network in Obsidian
- Prevents inconsistent type names through link suggestions

#### as a
```yaml
as a: teammate
```
- Specific user role (plain text)
- Should align with standardized roles
- Examples: teammate, admin, guest, external collaborator

**Best practice:** Create a note listing valid "as a" values to maintain consistency

#### who is
```yaml
who is: invited by an admin
```
- Optional qualifier for cross-cutting characteristics
- Leave blank when not needed
- Examples: "invited by an admin", "with accessibility needs", "managing multiple workspaces"

#### I need to
```yaml
I need to: accept an invite and land in the correct workspace
```
- The specific action or capability (plain text)
- **This becomes the filename**
- Focus on capability, not implementation

**In your setup:**
- Filename must match this field exactly
- Use lowercase and spaces for readability
- Creates intuitive file navigation

#### so that
```yaml
so that: I see the right data and teammates
```
- The ultimate goal or benefit (plain text)
- Should articulate the user's outcome

**Analysis tip:**
- After refining many needs, you'll notice common outcomes
- Use Obsidian search to find needs with similar "so that" statements
- Consider creating outcome tags or categories

### Organizational Frontmatter Fields

#### category
```yaml
category:
```
- Optional grouping for related needs (epics)
- Plain text or could use tags
- Typically 8-12 categories for 60-80 needs

**In your setup:**
- Can be plain text: `category: access and permissions`
- Or use Obsidian tags: `category: "#access"`
- Or leave blank and add later during refinement

**Benefits:**
- Easier to present to stakeholders
- Provides high-level view of project scope
- Helps organize work planning
- Query with Dataview to see all needs in a category

#### theme
```yaml
theme:
```
- Optional conceptual thread tying needs together
- Examples: findability, security, efficiency, collaboration

**In your setup:**
- Use plain text or tags
- Themes help see patterns across categories
- Different from category (themes are conceptual, categories are practical)

#### user journey stage
```yaml
user journey stage: "[[registration]]"
```
- Wiki-link to journey stage definition
- Creates relationship in Obsidian graph

**In your setup:**
- Use wiki-links like `[[registration]]`, `[[onboarding]]`, `[[daily use]]`
- View all needs at a stage via backlinks
- Create journey stage notes that describe each stage

**Examples from your repo:**
- `[[registration]]`
- You likely have others like `[[discovery]]`, `[[creation]]`, etc.

#### customer journey stage
```yaml
customer journey stage:
```
- Optional alternative journey view
- Useful if you track both user and customer journeys
- Can be plain text or wiki-link

### Optional Fields for Future Use

#### acceptance criteria
```yaml
acceptance criteria:
```
- Specific, testable conditions for meeting the need
- Can be added during refinement or project planning
- Use bullet points in the file body (after frontmatter) or in this field

**Example in file body:**
```markdown
---
[frontmatter fields]
---

## Acceptance Criteria
- User receives email invite with workspace link
- Link expires after 7 days
- Landing page shows workspace name and teammates
- User doesn't need to select workspace manually
```

#### Additional Fields You Might Add

Your template is extensible. You could add:
- `priority:` — High/Medium/Low
- `status:` — Discovered/Validated/In Progress/Addressed
- `source research:` — Link to research notes
- `related needs:` — Wiki-links to related need files
- `tags:` — Obsidian tags for flexible categorization

## Standardization in Obsidian

After refining many needs, certain values naturally consolidate. Instead of database dropdowns, you use:

### Wiki-Links for Controlled Vocabulary

**User types** — Create notes for each type:
- `user.md` (or `[[user]]`)
- `admin.md` (or `[[admin]]`)
- `teammate.md` (or `[[teammate]]`)

When adding `user type: "[[user]]"`, Obsidian suggests existing links, preventing typos and inconsistency.

### Standardized Plain Text Fields

**"as a" roles** — Maintain a reference note listing valid values:
```markdown
# Valid User Roles

- teammate
- admin
- guest
- external collaborator
```

**Journey stages** — Create wiki-links:
- `[[registration]]`
- `[[onboarding]]`
- `[[daily use]]`
- `[[collaboration]]`

### Benefits of This Approach

- **Flexibility:** Easy to add new types/stages
- **Discoverability:** Obsidian suggests existing links as you type
- **Analysis:** Backlinks show all needs for a type/stage
- **Graph view:** Visualizes relationships between needs, types, and stages
- **No lock-in:** Plain markdown files, not proprietary database

## The Refinement Workflow

### Initial Setup (One-time)
1. Create database structure with fields
2. Import existing user needs
3. Do initial pass to understand scope

### Bulk Refinement
1. **First pass:** Standardize format (As a/Who is/I need to/So that)
2. **Second pass:** Split "As a" into "As a" and "Who is"
3. **Third pass:** Identify and merge duplicates
4. **Fourth pass:** Standardize user types into dropdown
5. **Fifth pass:** Group similar outcomes and create dropdown
6. **Sixth pass:** Create and assign themes
7. **Seventh pass:** Create and assign epics/category needs
8. **Eighth pass:** Map to journey stages
9. **Ninth pass:** Review groupings to identify patterns

### Ongoing Maintenance
- Review needs at project start to select relevant ones
- Add new needs from research at project end
- Update existing needs if research refines understanding
- Periodically review for new duplicates or gaps

## Analysis Techniques in Obsidian

### Using Bases (Primary Method)

**Obsidian Bases** is your main tool for analyzing user needs. It provides a visual, interactive interface similar to Airtable or Coda.

**Setting up your User Needs Base:**
1. Enable Bases core plugin in Obsidian settings
2. Create a new Base pointing to `example-1/outputs/needs`
3. Configure visible properties: `as a`, `I need to`, `so that`, `user journey stage`, `category`, `theme`
4. Create multiple views for different analysis needs

**Example Base Views to Create:**

**View 1: By Journey Stage**
- Filter: `user journey stage` contains `[[registration]]`
- Shows: All registration-related needs
- Use case: Planning onboarding improvements

**View 2: By User Type**
- Filter: `user type` contains `[[user]]`
- Shows: All needs for regular users
- Use case: Understanding specific user segment

**View 3: Unprocessed Needs**
- Filter: `category` is empty
- Shows: Needs that haven't been categorized yet
- Use case: Refinement workflow

**View 4: All Needs Table**
- No filters
- Shows: Complete list with key properties
- Sort by: ID, journey stage, or category
- Use case: High-level overview

**View 5: By Outcome**
- Group by: `so that` field
- Shows: Which needs share similar outcomes
- Use case: Finding duplicates or related needs

**Benefits of Bases for analysis:**
- **Visual filtering:** Click to filter, no code needed
- **Inline editing:** Update properties without opening files
- **Multiple perspectives:** Save different views for different questions
- **Sorting:** Click column headers to sort
- **Counts:** See how many needs match each filter
- **Formula fields:** Can add calculated properties

### Using Backlinks (Supplementary)

**View all needs for a user type:**
1. Open the user type note (e.g., `[[user]]`)
2. View "Backlinks" panel
3. See all needs that reference this user type

**View all needs at a journey stage:**
1. Open the journey stage note (e.g., `[[registration]]`)
2. View "Backlinks" panel
3. See all needs at this stage

### Using Search (For specific queries)

**Find needs with similar outcomes:**
```
path:example-1/outputs/needs "so that: I can share"
```

**Find needs by specific user:**
```
path:example-1/outputs/needs "as a: teammate"
```

**Find needs with qualifiers:**
```
path:example-1/outputs/needs "who is:"
```

### Using Graph View (For relationships)

- View your needs as nodes connected to user types and journey stages
- Identify clusters of related needs
- Spot isolated needs that might need better categorization
- See which user types or journey stages have many vs. few needs

### Traditional Analysis (Now Adapted)

### Grouping by Outcome
Group needs by their "So that" field to find:
- Needs that serve the same ultimate goal
- Potential duplicates with different wording
- Related needs that could be addressed together

**Insight example:** "19 outcomes for 32 needs—many needs share common goals"

### Grouping by Journey Stage
View needs by where they occur to find:
- Stages with heavy need concentration
- Stages with few or no identified needs (potential gaps)
- Whether research has covered the full journey

**Insight example:** "9 needs for Creation, 11 for Library Management, but only 3 for Editing and 1 for Review—are we missing needs in later stages?"

### Grouping by User Type
Filter to single user types to understand:
- Unique needs of each user group
- Whether certain user types dominate (potential bias)
- Gaps in research coverage

**Insight example:** "All but 3 needs are for user researchers—have we adequately captured other user types?"

### Category Need Analysis
Review your epics/categories:
- How many needs fall into each category?
- Are there singleton categories (only one need)?
- Are categories balanced or heavily skewed?

**Insight example:** "3 category needs only have one user need each—are these categories appropriate, or should we research further?"

**Insight example:** "11 category needs for 39 user needs—good ratio for stakeholder digestion"

### Cross-tabulation
Combine multiple groupings:
- Which user types need what at which journey stages?
- Which themes appear across all user types vs. specific ones?
- Do certain outcomes correlate with journey stages?

## Example: Hackney Library Project Analysis

From refining 32 needs on an open library project:

**Outcomes:** Only 19 distinct "so that" outcomes despite 32 needs—many needs share ultimate goals

**Journey distribution:**
- Creation: 9 needs
- Library Management: 11 needs
- Editing: 3 needs
- Review: 1 need

**Question raised:** Are we missing needs in Editing and Review stages?

**User type distribution:** All but 3 needs are for user researchers

**Question raised:** Have we captured needs of other user types adequately?

**Category distribution:** 11 category needs for 39 refined user needs

**Assessment:** Good ratio for stakeholder presentations

**Singletons:** 3 categories with only one need each

**Question raised:** Are these legitimate distinct categories, or should we research further?

## Tools and Formats

### Your Tool: Obsidian with Bases

You're using **Obsidian Bases** with markdown files, which offers the best of both worlds:

**Advantages:**
- **Plain text:** Future-proof, portable, version-controllable
- **Bases interface:** Visual, interactive database like Airtable/Coda
- **No code required:** Unlike Dataview, Bases needs no programming
- **Wiki-links:** Natural relationships between needs, types, stages
- **Graph view:** Visualize the network of needs
- **Backlinks:** Automatically see all needs for a type/stage
- **Multiple views:** Different perspectives on the same data
- **Inline editing:** Update properties without opening files
- **No vendor lock-in:** Your data is always accessible as markdown
- **Git-friendly:** Easy to track changes over time

**Why Bases is perfect for user needs management:**
- Replaces the need for Airtable or Coda with a local-first solution
- Visual interface familiar to anyone who's used a database
- Filter, sort, and organize without writing queries
- Create views like "Registration needs", "Unprocessed needs", "By user type"
- Properties are stored in frontmatter, fully portable
- Can still use Dataview if you need advanced queries

**Recommended Obsidian plugins:**
- **Bases (core plugin):** Your primary interface for managing needs
- **Templater:** Automate new need file creation from template
- **Tag Wrangler:** Manage tags for categories/themes (optional)
- **Obsidian Git:** Sync and version control (optional)
- **Dataview:** Advanced queries if needed (optional with Bases)

### Alternative Tools (For Reference)

Other teams use:
- **Airtable:** Visual database, good filtering/grouping
- **Coda.io:** Flexible formulas, complex views
- **Spreadsheet:** Simple, universal
- **Specialized tools:** Dovetail, Aurelius, UserQ

Your Obsidian setup provides similar capabilities through different means:
- Dropdowns → Wiki-links and reference notes
- Formulas → Dataview queries
- Grouping → Backlinks and search
- Views → Dataview tables and custom queries

## Output Artifacts

### For Stakeholders
- **Epic summary:** List of 8-12 category needs
- **Journey map:** Needs mapped to stages
- **User type comparison:** Key needs per user group

### For Team
- **Full needs database:** Filterable and searchable
- **Gap analysis:** Stages/types with missing coverage
- **Duplicate list:** Candidates for merging

### For Future Projects
- **Reusable needs library:** Searchable repository
- **Acceptance criteria bank:** Examples of well-defined criteria
- **Outcome list:** Standard outcomes to check against

## Common Pitfalls

1. **Not standardizing early enough:** Harder to fix inconsistency in large repositories
2. **Too many categories:** Keep epics/categories to 8-12 for clarity
3. **Forcing dropdowns too early:** Let patterns emerge before constraining
4. **Ignoring duplicates:** Similar needs with different wording hide insights
5. **Solo refinement:** Team input crucial for accurate categorization
6. **One-and-done:** Needs repositories should be living documents

## Success Indicators

You've successfully refined user needs when:

- ✓ Duplicates are easily spotted by outcome similarity
- ✓ Filtering by user type instantly shows relevant needs
- ✓ Stakeholders can grasp scope via 8-12 epics
- ✓ Journey gaps are visually obvious
- ✓ New needs can be quickly categorized using existing taxonomy
- ✓ Team confidently references specific needs by ID
- ✓ Cross-project patterns become visible

## References

Based on Jonathan Richardson's methodology from refining several hundred user stories for a research repository project. Source: "User needs refinement — why and how to do it" (2020)
