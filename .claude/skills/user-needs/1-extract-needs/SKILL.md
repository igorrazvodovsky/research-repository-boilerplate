---
name: extract-needs-from-research
description: Extract user needs from research materials (interviews, observations, feedback)
type: user
---

# Extract Needs from Research

## Purpose

Parse research materials (interviews, observations, feedback) to identify user needs. Distinguish genuine needs from wants and solutions.

## When to Use This Skill

Invoke this skill when:
- The user asks to extract, identify, or parse user needs from research
- Working with interview transcripts, user feedback, or observation notes
- The user wants to analyze qualitative research data
- Processing research materials to find underlying user requirements

## Inputs

- Research material: transcripts, notes, observations, or direct quotes
- Context: what you know about the users and their goals

**Tool Usage**: Use the **Read** tool to access research files, and **Grep** to search for patterns across multiple research documents.

## Skill

### Listen for Needs, Not Solutions

When users speak, they often jump to solutions. Listen for the underlying need:

**User says:** "I want a dashboard with all my tasks"
**Extract:** Need to see what I need to work on → so that I can prioritize my day

**User says:** "There should be a filter dropdown"
**Extract:** Need to narrow down results → so that I can find relevant items quickly

### Distinguish Needs from Wants

**Needs** are functional requirements tied to goals:
- "I need to know when someone responds to my message"
- "I need to recover if I make a mistake"
- "I need to understand what changed since I last checked"

**Wants** are preferences or nice-to-haves:
- "I want it to be blue"
- "I want it to work like [other app]"
- "I want more options"

Extract needs. Note wants separately as preferences.

### Look for the "Why"

Ask (or infer): _Why does this matter to the user?_

**Quote:** "When I'm looking at projects, I just want to see the ones I'm actually working on, not everything in the whole system. It's overwhelming."

**Ask why:**
- Why only their projects? → They're focused on their own work
- Why is seeing everything overwhelming? → Too much information prevents focus
- What's the real goal? → Being able to focus on what matters to them

**Extract:** Need to see only relevant projects → so that I can focus on my work without distraction

### Think Solution-Agnostic

Remove implementation details from the need statement:

- ❌ "Need a search box with autocomplete"
- ✅ "Need to quickly find items by name"

- ❌ "Need a red notification badge"
- ✅ "Need to know when there's something requiring attention"

- ❌ "Need it to send me an email"
- ✅ "Need to be notified of important updates"

### Identify Patterns Across Sources

Look for the same need expressed different ways:

**Participant 1:** "I spend too much time scrolling through everything"
**Participant 2:** "I wish I could filter out irrelevant stuff"
**Participant 3:** "The main screen is too cluttered"

**Common need:** Need to see only relevant information → so that I can find what matters efficiently

### Common Need Categories

Use these as lenses when reviewing research:

**Discovery:** Understand what's possible, evaluate fit, learn the system
**Access:** Get in, prove identity, gain permissions
**Creation:** Make something new, express ideas, produce output
**Finding:** Locate existing items, search, browse, filter
**Understanding:** Make sense of information, get context, see relationships
**Acting:** Complete tasks, make changes, take action
**Monitoring:** Stay informed, track progress, see status
**Collaboration:** Work with others, share, coordinate
**Efficiency:** Do things faster, reduce effort, streamline workflows
**Recovery:** Fix mistakes, undo, get help when stuck
**Trust:** Feel secure, maintain privacy, control data

## Outputs

For each identified need, provide:

1. **Raw quote or observation** (evidence)
2. **Interpreted need** (capability statement)
3. **Intended outcome** (why it matters)
4. **User context** (who, when, under what circumstances)

Example output:
```
Evidence: "I'm constantly switching between tabs to check if anyone responded"
Need: Monitor for responses to my messages
Outcome: Stay updated without constant manual checking
Context: Team member, during active collaboration, checking for time-sensitive updates
```

## Quality Checks

Before finalizing an extracted need:

- [ ] Is it a capability, not a solution?
- [ ] Is there evidence from research (not assumption)?
- [ ] Would different technical solutions satisfy this need?
- [ ] Does the outcome explain _why_ the user cares?
- [ ] Is it specific enough to validate with users?

## Bundled Resources

### References

- **user-needs-writing-guide.md** — Detailed guide for writing clear, actionable user needs
- **user-needs-best-practices.md** — Practical guidance for managing user needs as a living practice

Use **Read** tool to access these references when needing additional context on need writing standards and team workflows.

## Related Skills

- `validate-need-quality` — Check if extracted needs meet quality criteria
- `identify-need-patterns` — Find themes and relationships across needs
- `render-user-need` — Format needs using the template structure
