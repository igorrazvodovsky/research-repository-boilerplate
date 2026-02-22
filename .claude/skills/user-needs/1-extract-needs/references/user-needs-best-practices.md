Practical guidance for managing user needs as a living practice, including team collaboration, timing, and common scenarios.

## Your Setup

This guide is adapted for use with:
- **Format:** Individual .md files per user need in `example-1/outputs/needs/`
- **Tool:** Obsidian with **Bases** plugin for database-like management
- **Version control:** Your needs folder can be tracked with Git
- **Template:** `templates/user-need.md` for consistent structure
- **Analysis:** Obsidian Bases views (primary), plus backlinks and graph view

## Core Principles

### 1. User Needs Are a Living Document

User needs repositories should evolve continuously:

- Review at the start of every project
- Update at the end of every project
- Refine as understanding deepens
- Retire needs that become obsolete
- Split needs that prove too broad
- Merge needs revealed as duplicates

**Anti-pattern:** Creating a needs repository once and never touching it again.

### 2. Team Ownership Over Individual Control

While user researchers often do the bulk of refinement work, the team should be involved in:

- Reviewing groupings and categories
- Validating outcomes
- Identifying gaps
- Prioritizing needs
- Defining acceptance criteria

**Anti-pattern:** User researcher working in isolation, then presenting finished categorization to team.

### 3. This Is A Way, Not The Way

The methodology described here is one effective approach, not a rigid standard. Adapt it to:

- Your organization's scale
- Your team's workflow
- Your tool preferences
- Your project types

**Anti-pattern:** Forcing a method that doesn't fit your context.

## When to Refine User Needs

### Initial Repository Creation

**When:** First time building a user needs repository, or when consolidating needs from multiple legacy projects.

**Scope:** Often 100-1000+ needs to review.

**Effort:** Substantial—plan for significant dedicated time.

**Approach in Obsidian:**
1. Gather all existing user stories/needs (from docs, spreadsheets, etc.)
2. Create individual .md files for each need
3. Use your template to ensure consistent frontmatter
4. Fill in user types, journey stages using wiki-links
5. Use Dataview to analyze and find gaps

**Tip:** This is satisfying work but time-consuming. Block dedicated time rather than trying to fit it around other work.

**In your setup:** You might create a temporary "needs-to-process" folder, then move refined needs to `example-1/outputs/needs/` once complete.

### Project Start

**When:** Beginning a new project or sprint.

**Purpose:**
- Select which existing needs apply to this project
- Identify any obvious gaps in coverage
- Brief team on relevant needs
- Plan research to address gaps

**Effort:** Light—filtering and reviewing existing needs.

**Approach in Obsidian with Bases:**
1. Open your User Needs Base
2. Create a view filtered by relevant user types and journey stages
3. Create a project note that links to relevant needs
4. Add a `projects:` field to need frontmatter to track which project addresses it
5. Use a Base view to see gaps (e.g., filter for empty categories)

**Example Base setup for project start:**
- **View name:** "Project: Registration Flow"
- **Filter:** `user journey stage` contains `[[registration]]` AND `user type` contains `[[user]]`
- **Visible properties:** ID, as a, I need to, so that, category
- **Sort by:** category
- This gives you all user needs for registration at a glance

### Project End

**When:** Completing a research phase or project.

**Purpose:**
- Add new needs discovered
- Update existing needs that research refined
- Remove duplicates
- Validate categorization

**Effort:** Medium—integrating new findings.

**Approach in Obsidian with Bases:**
1. Extract new needs from research notes
2. Search existing needs to check for duplicates: `path:example-1/outputs/needs "I need to: [action]"`
3. Create new .md files using your template
4. Add wiki-links for user types and journey stages
5. Open your Bases view to see the new needs appear automatically
6. Use Bases filtering to analyze patterns (group by outcome, category, etc.)
7. Update or archive needs if research changes understanding

**Workflow tip:**
- Keep research notes in a separate folder
- Link from research notes to needs: "This research identified [[accept an invite and land in the correct workspace]]"
- Link from needs back to research: Add `source: [[Research Session 5]]` in frontmatter
- Create a Bases view called "Recent Needs" filtered by date to see new additions

**Critical timing:** Do this _toward_ the end with enough runway to address gaps, not _at_ the very end when it's too late to do follow-up research.

### Regular Review Cycles

**When:** Quarterly or semi-annually, independent of specific projects.

**Purpose:**
- Maintain consistency as repository grows
- Identify emerging patterns across projects
- Consolidate similar needs from different projects
- Update taxonomy as understanding evolves

**Effort:** Medium to substantial, depending on activity.

**Approach:**
1. Review needs added since last review
2. Check for drift in terminology or categorization
3. Update dropdowns if new patterns have emerged
4. Merge duplicates
5. Generate cross-project insights

## Team Collaboration

### Roles and Responsibilities

#### User Researcher (Lead)
- Owns the refinement process
- Does bulk of initial standardization
- Maintains consistency in repository
- Facilitates team reviews
- Synthesizes insights

**Time commitment:** Substantial during refinement phases.

#### Full Team (Participants)
- Reviews proposed groupings
- Validates outcomes and categorization
- Identifies gaps from their perspective
- Contributes to acceptance criteria
- Challenges assumptions

**Time commitment:** Focused sessions for input and validation.

#### Stakeholders (Recipients)
- Receive summarized findings (epics, not all needs)
- Provide strategic input on priorities
- Validate that needs align with business goals

**Time commitment:** Minimal—high-level presentations.

### Collaboration Workflow

**Phase 1: Solo Refinement (User Researcher)**
- Standardize format
- Initial categorization
- Identify obvious duplicates
- Prepare for team review

**Phase 2: Team Review (Full Team)**
- Present proposed groupings
- Discuss outcomes and themes
- Validate categorization
- Identify gaps as a group
- Assign priorities

**Phase 3: Refinement (User Researcher)**
- Incorporate team feedback
- Finalize categorization
- Complete analysis
- Generate insights

**Phase 4: Presentation (Full Team + Stakeholders)**
- Share key findings
- Present epics and themes
- Highlight gaps
- Propose research priorities

### Review Session Tips

**Prepare materials:**
- Summary of new/changed needs
- Proposed groupings in visual format
- Specific questions for team input
- Examples of unclear categorizations

**Structure the session:**
1. Context: Why we're reviewing (5 min)
2. Overview: What's changed (10 min)
3. Discussion: Groupings and categories (30 min)
4. Gaps: What are we missing? (15 min)
5. Next steps: Actions and timeline (10 min)

**Facilitate effectively:**
- Focus on areas where you're uncertain
- Don't ask team to rubber-stamp your work
- Encourage constructive challenge
- Document decisions and rationale
- Park tangent discussions for later

## Common Scenarios

### Scenario: Duplicate Needs from Different Projects

**Situation:** Two projects identified very similar needs with different wording.

**Approach:**
1. Examine both in detail—are they truly identical?
2. Look at the "So that" outcome—if it's the same, likely duplicates
3. Check if one is more specific than the other
4. If duplicates, merge and note both source projects
5. If one is more specific, make it a child or variation

**Example:**
- Need A: "I need to quickly add research to the library"
- Need B: "I need to easily add research without complex steps"
- **Resolution:** Merge to "I need to quickly and easily add research" noting both projects

### Scenario: Need vs Want

**Situation:** A user need sounds like a feature request.

**Original:** "As a user researcher, I want a search box on every page"

**Approach:**
1. Identify the underlying need behind the want
2. Ask: What would that feature enable?
3. Reframe as capability, not solution

**Refined:** "As a user researcher, I need to find relevant research from anywhere in the system so that I can quickly locate information"

### Scenario: Vague Outcome

**Situation:** The "So that" doesn't articulate a clear goal.

**Original:** "As a user, I need to login so that I can use the system"

**Problem:** "Use the system" is too vague.

**Approach:**
1. Ask: What specifically does system access enable?
2. Look at the user type for context
3. Consider what's different before vs after login

**Refined:** "As a user researcher who is authorized, I need to login so that I can access and contribute to the research repository"

### Scenario: Multiple Outcomes

**Situation:** One need seems to have multiple distinct outcomes.

**Original:** "As a user, I need to export data so that I can analyze it in other tools and share it with external stakeholders"

**Problem:** Two different outcomes bundled together.

**Approach:**
1. Split into separate needs with distinct outcomes
2. Keep "I need to" the same if the action is identical
3. Distinguish via different "So that" statements

**Refined:**
- Need 1: "...export data so that I can analyze it in specialized tools"
- Need 2: "...export data so that I can share findings with external stakeholders"

### Scenario: Gap in Journey Coverage

**Situation:** Analysis reveals 15 needs for "Creation" but only 2 for "Maintenance."

**Interpretation questions:**
- Is maintenance genuinely less complex?
- Did research focus disproportionately on creation?
- Are maintenance needs bundled into creation needs?
- Is maintenance a separate journey we didn't map?

**Response:**
1. Review with team to validate the gap
2. If genuine gap, plan targeted research
3. If needs are bundled, separate them
4. If journey mapping is incomplete, revisit it

### Scenario: Singleton Category

**Situation:** An epic/category has only one need in it.

**Possible interpretations:**
- This is a genuinely distinct area (keep it)
- This is under-researched (do more research)
- This need doesn't warrant its own category (recategorize)
- The need is too specific and should be split (refactor)

**Decision factors:**
- Strategic importance of the area
- Likelihood of finding more needs in this category
- Whether it makes sense standalone in presentations

### Scenario: Outcome Proliferation

**Situation:** You have 50 needs with 40 different outcomes.

**Problem:** Too much variation prevents useful grouping.

**Approach:**
1. Review outcomes looking for similarity
2. Identify higher-level outcome categories
3. Standardize wording where goals are similar
4. Create a standard dropdown list

**Example outcomes that should merge:**
- "I can easily share research"
- "Others can see my research"
- "Research is accessible to the team"

**Standardized:** "I can share research with others"

## Maintenance Strategies

### Preventing Drift

**Problem:** Over time, new needs get added without consistent categorization.

**Solutions in Obsidian:**
- **Use wiki-links:** Obsidian suggests existing links, preventing typos
- **Maintain reference notes:** Create notes like "Valid User Roles" listing all accepted values
- **Use templates:** Always create new needs from `templates/user-need.md`
- **Regular review:** Periodically check backlinks to ensure consistency
- **Document standards:** Keep a "User Needs Guide" note with examples
- **Onboarding:** Show new team members the template and reference notes

**Example reference note:** `user-roles-reference.md`
```markdown
# Valid User Roles

Use these values in the "as a:" field:

- teammate
- admin
- guest
- external collaborator

Examples:
- [[accept an invite and land in the correct workspace]]
```

### Managing Growth

**Problem:** Repository grows to hundreds or thousands of needs.

**Solutions in Obsidian:**
- **Folder organization:** Use subfolders like `needs/core/`, `needs/advanced/`, `needs/archived/`
- **Dataview views:** Create saved queries for different perspectives
- **Tags:** Use tags like `#priority-high` or `#validated` for flexible filtering
- **Project notes:** Create notes that link to subsets of relevant needs
- **Archive folder:** Move outdated needs to `needs/archived/` rather than deleting
- **Summary notes:** Create a "Top User Needs" note with links to most important ones

**Example folder structure:**
```
example-1/
  outputs/
    needs/
      core/           # Essential needs
      emerging/       # Newly discovered
      archived/       # No longer relevant
```

**Example summary note:**
```markdown
# Top User Needs

## Registration & Onboarding
- [[accept an invite and land in the correct workspace]]
- [[verify eligibility for access]]

## Daily Use
- [[find what I'm looking for]]
- [[see my assigned work]]
```

### Your Tool: Obsidian

You've chosen **Obsidian** with markdown files. This provides:

**Strengths for your use case:**
- **Future-proof:** Plain text files will always be readable
- **Version control:** Works naturally with Git
- **Relationships:** Wiki-links create natural connections
- **Flexibility:** Easy to add custom fields
- **No lock-in:** Can migrate to any system that reads markdown
- **Graph view:** Visualize relationships between needs, types, stages
- **Local-first:** Your data stays with you

**Best practices for Obsidian Bases:**
- **Bases core plugin:** Your primary interface (essential)
- **Create multiple views:** Different perspectives for different questions
- **Templater plugin:** Automate new need creation
- **Consistent naming:** Filename = "I need to" field
- **Wiki-links:** Use for user types, journey stages
- **Frontmatter:** Keep structure consistent via template
- **Git tracking:** Commit changes to track evolution over time
- **Inline editing in Bases:** Update properties directly in views

**Alternative tools (for reference):**
- **Spreadsheet:** Simple but limited
- **Airtable:** Visual, collaborative
- **Coda:** Powerful formulas
- **Specialized:** Dovetail, Aurelius, UserQ

Your Obsidian setup offers similar capabilities through different mechanisms.

### Versioning

**With Obsidian and Git:**
Your markdown files are naturally version-controllable.

**Recommended approach:**
- **Git repository:** Track your entire Obsidian vault or just the needs folder
- **Commit on milestones:** After project end, after bulk refinement, etc.
- **Frontmatter date fields:** Add `created:` and `last_modified:` fields
- **Archive folder:** Move superseded needs to `needs/archived/` with date
- **Git history:** View evolution of individual needs via Git log

**Example frontmatter with versioning:**
```yaml
---
ID: "8"
created: 2024-01-15
last_modified: 2024-03-20
status: validated
user type: "[[user]]"
as a: teammate
# ... rest of fields
---
```

**Benefits:**
- See when each need was discovered
- Track how needs evolved over time
- Restore old versions if needed
- Understand research timeline

## Quality Indicators

### Signs Your Needs Are Well-Managed

✓ New team members can quickly find relevant needs
✓ Duplicates are caught before they're added
✓ Stakeholders grasp scope via epic summaries
✓ Gaps are obvious from journey/user type views
✓ Categorization decisions feel natural, not forced
✓ Repository is actively used in project planning
✓ Team references needs by ID in discussions
✓ Research validates and refines existing needs

### Signs You Need to Refactor

✗ People complain they can't find anything
✗ Same need appears multiple times with different wording
✗ Categorization feels arbitrary or contested
✗ Dropdowns have 30+ options
✗ Nobody uses the repository in actual work
✗ Major inconsistency between old and new needs
✗ Research keeps finding "new" needs already documented

## Getting Started: Minimum Viable Refinement

If you're starting from scratch or have limited time:

**Minimal structure in Obsidian:**
1. Create .md files with basic frontmatter: ID, "as a", "I need to", "so that"
2. Create 3-5 user type notes (e.g., `[[user]]`, `[[admin]]`, `[[guest]]`)
3. Create 5-8 journey stage notes (e.g., `[[registration]]`, `[[daily use]]`)
4. Link needs to types and stages using wiki-links
5. Use your template for consistency

**Skip for now:**
- "who is" qualifiers (add when you find cross-cutting needs)
- Detailed acceptance criteria
- Categories and themes
- Success/failure impacts
- Complex Dataview queries

**Iterate later:**
- Add fields as you discover patterns
- Create categories when groupings become clear
- Add themes after you have 20-30 needs
- Build Dataview queries as you need specific views

**Your first need could be as simple as:**
```yaml
---
ID: "1"
as a: teammate
I need to: see my assigned work
so that: I know what to focus on
user journey stage: "[[daily use]]"
---
```

## Advanced Practices

### Acceptance Criteria as Sub-Needs

For complex needs, acceptance criteria can be detailed enough to function as sub-needs or implementation requirements.

**Example:**
- **Parent need:** "I need to securely access the system"
- **Acceptance criteria / sub-needs:**
  - Can authenticate via institutional login
  - Can use multi-factor authentication
  - Can recover forgotten password
  - Can see active sessions
  - Can revoke access from lost device

### Need Relationships and Dependencies

Track when needs relate to each other:
- **Prerequisites:** Need A must be met before Need B makes sense
- **Alternatives:** Needs that address the same outcome differently
- **Composites:** Need that combines several smaller needs
- **Conflicts:** Needs that may work against each other

### Impact Scoring

Quantify needs to aid prioritization:
- User impact (how many users affected)
- Frequency (how often needed)
- Severity (what happens if unmet)
- Alignment (strategic importance)

### Linking to Evidence

Connect each need to:
- Research sessions where it emerged
- Direct quotes from users
- Observational evidence
- Quantitative data supporting it

## Common Mistakes to Avoid

1. **Perfection paralysis:** Don't let pursuit of perfect categorization prevent using the repository
2. **Over-categorization:** Too many categories makes it harder to see patterns
3. **Solo work:** Team input is essential for accurate understanding
4. **One-time effort:** Needs repositories require ongoing maintenance
5. **Missing the forest:** Don't get so focused on individual needs you miss overall patterns
6. **Analysis without action:** Insights are only valuable if they inform decisions
7. **Rigid adherence:** If the structure isn't working, change it
8. **Ignoring duplicates:** Similar needs across projects are data, not errors

## Getting Buy-In

### For Teams

**Emphasize:**
- Reduces repeated research on same questions
- Makes research insights accessible when needed
- Provides structure for project planning
- Creates shared understanding of users

**Show:**
- Quick demos of finding relevant needs
- Examples of gaps identified through analysis
- How epics simplify scope communication

### For Stakeholders

**Emphasize:**
- Strategic view of user needs across products
- Evidence-based prioritization
- Visibility into research coverage
- Efficient use of research investment

**Show:**
- Epic-level summaries (not detailed needs)
- Gap analysis highlighting risks
- How needs inform roadmap decisions

### For Leadership

**Emphasize:**
- Organizational knowledge retention
- Consistency across teams
- Evidence-based decision making
- ROI on research investment

**Show:**
- Cross-project insights
- Coverage of strategic priorities
- Risk areas with gaps in understanding

## Measuring Success

### Usage Metrics
- How often is repository accessed?
- How many team members actively use it?
- Are needs referenced in project planning?
- Do new projects start by reviewing existing needs?

### Quality Metrics
- How often are duplicates caught?
- How quickly can relevant needs be found?
- How much does categorization change (stability)?
- Team confidence in using repository?

### Impact Metrics
- Does research build on previous findings?
- Are fewer redundant studies conducted?
- Do products address documented needs?
- Can team articulate user needs confidently?

## Summary: The Refinement Mindset

User needs refinement is not a one-time project but an ongoing practice:

- **Start simple:** Basic structure is better than no structure
- **Iterate:** Let sophistication evolve with usage
- **Collaborate:** Team involvement ensures accuracy and buy-in
- **Apply insights:** Analysis is only valuable if it informs action
- **Stay flexible:** Adapt the approach as you learn what works
- **Maintain:** Regular light maintenance prevents major overhauls

The goal is not a perfect taxonomy but a _useful_ one that helps teams understand and serve users better.

## References

Based on Jonathan Richardson's practical experience refining several hundred user needs and establishing user research repositories. Source: "User needs refinement — why and how to do it" (2020)
