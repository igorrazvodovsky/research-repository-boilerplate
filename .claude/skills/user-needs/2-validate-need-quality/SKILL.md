---
name: validate-need-quality
description: Validate that extracted user needs meet quality standards and catch common pitfalls
type: user
---

# Validate Need Quality

## Purpose

Evaluate whether an extracted need meets quality standards. Catch common pitfalls before needs are documented.

## When to Use This Skill

Invoke this skill when:
- The user asks to validate, review, or check user needs for quality
- After extracting needs from research (before documenting them)
- The user wants to ensure needs are well-formed and actionable
- Reviewing existing needs for quality issues

## Inputs

- Candidate need statement (I need to... / so that...)
- User context (as a... / who is...)
- Source evidence

**Tool Usage**: Use **Read** to access need files, and **Grep** to search for patterns or potential duplicates across the needs collection.

## Skill

### Quality Criteria Checklist

Run each need through these checks:

#### 1. Capability vs Solution

**Check:** Does it describe what the user needs to accomplish, not how?

❌ **Solution:**
- "I need to have a blue button"
- "I need a filter dropdown"
- "I need an email notification"

✅ **Capability:**
- "I need to trigger an action quickly"
- "I need to narrow down results to find relevant items"
- "I need to know when something requires my attention"

**Test:** Can you imagine 3+ different ways to satisfy this need? If not, it's probably a solution.

#### 2. Different Levels (Not Circular)

**Check:** Are "I need to" and "so that" at different levels of abstraction?

❌ **Circular:**
- Need: "save my work" / Outcome: "my work is saved"
- Need: "search for items" / Outcome: "I can find things by searching"
- Need: "see a list" / Outcome: "there's a list visible"

✅ **Different Levels:**
- Need: "save my work" / Outcome: "I don't lose progress if interrupted"
- Need: "search for items" / Outcome: "I can find specific items quickly without browsing"
- Need: "see my assigned tasks" / Outcome: "I know what to work on next"

**Test:** Cover up "I need to" — does "so that" still make sense as a user goal? Cover up "so that" — does "I need to" still describe an action?

#### 3. Evidence-Based (Not Assumed)

**Check:** Is there research evidence supporting this need?

✅ **Evidence-based:**
- Direct quote from interview
- Observed behavior in usability test
- Support ticket theme from multiple users
- Survey response pattern

❌ **Assumed:**
- "Users probably want..."
- "It makes sense that..."
- "Best practice is..."
- Based on what competitors do

**Test:** Can you point to specific research sources? Could you show this to a user and ask "does this resonate?"

#### 4. Specific Enough to Validate

**Check:** Is it concrete enough to test with users?

❌ **Too Vague:**
- "I need to use the system effectively"
- "I need a better experience"
- "I need it to work well"

✅ **Specific:**
- "I need to recover from accidental deletions"
- "I need to see when my teammate last updated the document"
- "I need to complete checkout in under 2 minutes"

**Test:** Could you design a prototype specifically to address this need? Could users tell you if the need was met?

#### 5. Technology-Agnostic

**Check:** Does it avoid prescribing implementation?

❌ **Prescriptive:**
- "I need a dropdown menu"
- "I need to click a toggle"
- "I need a REST API endpoint"

✅ **Agnostic:**
- "I need to select from multiple options"
- "I need to enable or disable a setting"
- "I need to integrate with external systems"

**Test:** Would this need exist regardless of platform (mobile, web, voice, API)?

#### 6. Testable / Measurable

**Check:** Can you determine objectively whether the need is met?

✅ **Testable:**
- "I need to complete checkout" → Can measure completion
- "I need to find documents by name" → Can test search success
- "I need to know if my action succeeded" → Can observe feedback presence

❌ **Untestable:**
- "I need to feel confident" → Subjective, hard to measure directly
- "I need a good experience" → Undefined criteria
- "I need it to be intuitive" → Vague, personal

**Note:** Emotional outcomes (confidence, trust) are valid but should be tied to concrete capabilities that enable them.

## Common Pitfalls

### Pitfall: Solution Dressed as Need

**Smells like:**
- Mentions specific UI elements (button, dropdown, modal)
- Names specific technologies (email, SMS, push notification)
- Describes implementation ("sorted alphabetically", "color-coded")

**Fix:** Ask "why do they want that specific solution?"

Example:
- Before: "I need a red badge icon"
- After: "I need to immediately notice when there's something requiring action"

### Pitfall: Duplicate Action and Outcome

**Smells like:**
- "So that" just restates "I need to" differently
- Outcome describes system behavior, not user benefit
- The two clauses could be swapped without loss of meaning

**Fix:** Ask "what does accomplishing this enable the user to do?"

Example:
- Before: "I need to filter the list → so that the list shows only certain items"
- After: "I need to narrow results → so that I can find relevant items without scrolling"

### Pitfall: Too Vague to Act On

**Smells like:**
- Uses words like "better", "improved", "easy", "good"
- Could apply to almost any feature
- Doesn't suggest design direction

**Fix:** Ask "what specifically would be better? In what context?"

Example:
- Before: "I need a better way to organize things"
- After: "I need to group related items together → so that I can find everything for a project in one place"

### Pitfall: Assumed Without Evidence

**Smells like:**
- "Users probably...", "It makes sense that..."
- Based on best practices, not your users
- No research quotes or observations provided

**Fix:** Mark as hypothesis to test, or find supporting research

### Pitfall: Overly Specific Context

**Smells like:**
- Describes one very specific scenario
- Won't apply to other users in the same role
- Too narrow to be a general need

**Fix:** Generalize while keeping the core capability

Example:
- Before: "As a developer debugging a crash on Tuesday afternoon in the staging environment..."
- After: "As a developer troubleshooting issues..."

## Validation Process

For each need, work through this sequence:

1. **Read it aloud** — Does it sound like something a user would say?
2. **Check the criteria** — Run through all 6 quality checks above
3. **Test for pitfalls** — Look for common problems
4. **Imagine solutions** — Can you think of 3+ ways to solve this? (proves it's not a solution itself)
5. **Connect to evidence** — Can you point to the research source?
6. **Get feedback** — Would another designer understand this need?

## Outputs

For each need:

**Status:**
- ✅ **Valid** — Meets all criteria, ready to document
- ⚠️ **Needs revision** — Close, but has specific issues to fix
- ❌ **Invalid** — Should be rewritten or discarded

**If needs revision, provide:**
- Which criteria it fails
- Suggested improvement
- Questions to clarify with user/research

## Examples

### Example 1: Good Need

```
Need: I need to see who else is currently editing a document
So that: I can avoid edit conflicts and coordinate with teammates

✅ Capability (not "show avatars in header")
✅ Different levels (coordination ≠ seeing)
✅ Specific enough (testable)
✅ Technology-agnostic (many solutions possible)
✅ Based on collaboration research observation
```

### Example 2: Needs Revision

```
❌ Need: I need to have a dashboard with widgets
So that: I can see my dashboard

Issues:
- "Dashboard with widgets" is a solution, not a capability
- Circular: "see my dashboard" just restates the need
- Missing user benefit

Suggested revision:
Need: I need to monitor key metrics at a glance
So that: I can spot issues quickly without opening multiple tools
```

### Example 3: Invalid (Discard)

```
❌ Need: I need the app to be fast
So that: It doesn't feel slow

Issues:
- Too vague ("fast" is undefined)
- Circular logic
- No specific context
- Untestable without criteria

Action: Discard. Look for specific research about where slowness impacts users.
```

## Bundled Resources

### References

- **user-needs-writing-guide.md** — Detailed guide for writing clear, actionable user needs
- **user-needs-best-practices.md** — Practical guidance for managing user needs as a living practice

Use **Read** tool to access these references when needing additional context on validation standards and quality criteria.

## Related Skills

- `extract-needs-from-research` — How to identify needs in research materials
- `identify-need-patterns` — Find relationships across validated needs
