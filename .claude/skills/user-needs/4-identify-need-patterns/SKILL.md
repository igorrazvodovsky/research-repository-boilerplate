---
name: identify-need-patterns
description: Analyze collections of user needs to find themes, clusters, duplicates, and gaps
type: user
---

# Identify Need Patterns

## Purpose

Analyze a collection of user needs to find themes, clusters, duplicates, and gaps. Surface insights about what users care about most and where design should focus.

## When to Use This Skill

Invoke this skill when:
- The user asks to analyze, find patterns, or identify themes across user needs
- Working with a collection of documented needs and looking for insights
- The user wants to understand what users care about most
- Identifying gaps in research coverage or duplicate needs

## Inputs

- Collection of validated user needs (structured files or data)
- User type taxonomy (if available)
- Journey stage definitions (if available)

## Skill

### Pattern Types to Look For

#### 1. Similar Outcomes

Needs that aim for the same user goal but through different actions.

**Example cluster:**
- Need: "see my assigned tasks" → so that: "I know what to work on next"
- Need: "get notified of deadlines" → so that: "I know what to work on next"
- Need: "view my calendar" → so that: "I know what to work on next"

**Insight:** "Knowing what to work on next" is a key outcome — multiple needs serve this goal.

**Use Grep to find:**
```
pattern: "so that:.*[outcome phrase]"
output_mode: "content"
```

#### 2. Duplicate or Overlapping Needs

Needs that describe essentially the same capability in different words.

**Example duplicates:**
- "I need to find documents by name"
- "I need to search for files using keywords"
- "I need to locate items by title"

**Insight:** Same core need stated different ways — consolidate into one.

**Use Grep to find:**
```
pattern: "I need to: [specific action phrase]"
output_mode: "files_with_matches"
```

Then review matches manually to identify semantic duplicates.

#### 3. Theme Clusters

Needs that share conceptual threads even if actions differ.

**Example theme: "Recoverability"**
- "Undo accidental deletions"
- "Restore previous versions"
- "See history of changes"
- "Get confirmation before destructive actions"

**Example theme: "Awareness"**
- "Know when someone responds"
- "See who's currently editing"
- "Track changes since last visit"
- "Monitor project status"

**Insight:** Themes cut across journey stages and user types — they're strategic focus areas.

**Use Grep to find seeds:**
```
pattern: "theme:.*[theme name]"
output_mode: "files_with_matches"
```

Then expand by reading needs to find thematically related ones.

#### 4. Coverage by User Type

Which user types have many needs vs few?

**Example distribution:**
- Team members: 45 needs
- Admins: 12 needs
- Guests: 3 needs

**Insight:** We understand team members well, but guests are under-researched.

**Use Grep to count:**
```
pattern: "user type:.*\\[\\[team-member\\]\\]"
output_mode: "count"
path: "example-1/outputs/needs"
```

#### 5. Coverage by Journey Stage

Where in the user journey do most needs cluster?

**Example distribution:**
- Onboarding: 8 needs
- Daily use: 52 needs
- Offboarding: 1 need

**Insight:** We've focused heavily on daily use but haven't explored the full journey.

**Use Grep to count:**
```
pattern: "user journey stage:.*\\[\\[daily-use\\]\\]"
output_mode: "count"
```

#### 6. Uncategorized Needs

Needs missing category or theme metadata.

**Use Grep to find:**
```
pattern: "^category:$"
output_mode: "files_with_matches"
```

**Insight:** These need more analysis to understand where they fit.

#### 7. High-Frequency Action Verbs

What actions appear across many needs?

**Example:**
- "see/view": 23 occurrences → Visibility is important
- "know/understand": 18 occurrences → Information needs dominate
- "share/collaborate": 14 occurrences → Teamwork is key

**Use Grep with regex:**
```
pattern: "I need to: (see|view|understand|know)"
output_mode: "count"
```

#### 8. Needs Without Clear Outcomes

"So that" statements that are vague or circular.

**Red flags:**
- "so that: I can use the system"
- "so that: it works"
- "so that: I accomplish my goal"

**Use Grep to find candidates:**
```
pattern: "so that: I can (use|access|have)"
output_mode: "content"
```

Manually review to identify needs requiring better outcome definition.

### Analysis Process

**Step 1: Get the landscape**
```bash
# Count total needs
ls example-1/outputs/needs/*.md | wc -l

# List user types
grep "user type:" example-1/outputs/needs/*.md | sort | uniq

# List journey stages
grep "user journey stage:" example-1/outputs/needs/*.md | sort | uniq
```

**Step 2: Find duplicates**
- Use Grep to search for similar "I need to" phrases
- Read potential matches side-by-side
- Determine if they're true duplicates or variations

**Step 3: Identify themes**
- Look for needs that feel related even if actions differ
- Group by underlying goal or concern
- Name the theme (e.g., "trust", "efficiency", "awareness")

**Step 4: Check coverage**
- Count needs by user type, journey stage, category
- Identify gaps (types/stages with few needs)
- Note heavy clusters (areas with many needs)

**Step 5: Extract insights**
- What patterns emerged?
- What's surprising?
- Where should design focus?
- What questions remain?

## Outputs

Produce a patterns analysis document containing:

### 1. Theme Clusters
```markdown
## Theme: [Name]

Description: [What ties these needs together]

Needs:
- [Need ID + summary]
- [Need ID + summary]
...

Insight: [What this cluster tells us about user priorities]
```

### 2. Coverage Summary
```markdown
## User Type Distribution
- Type A: X needs
- Type B: Y needs
...

## Journey Stage Distribution
- Stage 1: X needs
- Stage 2: Y needs
...

## Gaps Identified
- [User types with < 5 needs]
- [Journey stages with < 5 needs]
```

### 3. Duplicates to Resolve
```markdown
## Potential Duplicates

### Cluster 1
- Need #X: [summary]
- Need #Y: [summary]

Recommendation: [Merge/Keep separate/Refine]
```

### 4. Strategic Insights
```markdown
## Key Findings

1. [Pattern or insight]
   - Evidence: [Which needs, what frequency]
   - Implication: [What it means for design]

2. [Pattern or insight]
   ...
```

### 5. Recommended Actions
```markdown
## Next Steps

- Research gaps: [Which user types/stages need more study]
- Consolidate: [Which needs to merge]
- Focus areas: [Themes to prioritize in design]
- Questions: [What we still don't understand]
```

## Pattern Recognition Tips

**Look for absence, not just presence:**
- Which user types have almost no needs? Why?
- Which journey stages are empty? Are they unimportant or under-researched?
- What capabilities are never mentioned? Should they be?

**Watch for intensity:**
- Needs mentioned by many users → High priority
- Needs with strong emotional language → Pain point
- Needs with complex "so that" chains → Strategic importance

**Notice relationships:**
- Needs that depend on each other
- Needs that conflict
- Needs that are mutually exclusive by user type

**Consider maturity:**
- Early journey stages → Adoption blockers
- Late journey stages → Retention drivers
- Cross-stage needs → Core value propositions

## Grep Patterns Reference

Find similar outcomes:
```
pattern: "so that: I can [phrase]"
output_mode: "content"
```

Find specific user type:
```
pattern: "user type:.*\\[\\[[type]\\]\\]"
output_mode: "files_with_matches"
```

Find specific journey stage:
```
pattern: "user journey stage:.*\\[\\[[stage]\\]\\]"
output_mode: "content"
```

Find needs without categories:
```
pattern: "^category:\\s*$"
output_mode: "files_with_matches"
```

Find needs by action verb:
```
pattern: "I need to: (verb1|verb2|verb3)"
output_mode: "content"
-i: true  # case insensitive
```

Count by theme:
```
pattern: "theme: [theme-name]"
output_mode: "count"
```

## Bundled Resources

### References

- **user-needs-refinement-process.md** — Systematic approach to organizing and analyzing user needs

Use **Read** tool to access this reference when needing detailed guidance on the refinement workflow.

## Related Skills

- `extract-needs-from-research` — Identify needs before pattern analysis
- `validate-need-quality` — Ensure needs are well-formed before analyzing patterns
