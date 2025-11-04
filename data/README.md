# Data

_Raw research materials and primary sources_

This directory contains the unprocessed, factual records from research activities.

## What Goes Here

### Interview Materials
- **Transcripts** - Full, verbatim interview transcripts (redacted for privacy)
- **Recording metadata** - Session info, participant IDs, timestamps (not the actual recordings)
- **Notes** - Raw notes from sessions, observations, field notes

### Participant Information
- **User panel** - Anonymized participant database with segments, characteristics
- **Recruitment data** - Screening responses, scheduling information
- **Consent records** - Documented consent (store actual forms securely offline)

### Survey & Test Data
- **Survey responses** - Raw response data from questionnaires
- **Usability test results** - Task completion, time-on-task, error rates
- **Analytics exports** - Raw data from tools (GA, Hotjar, etc.)

### Research Artifacts
- **Screenshots** - Interface captures, competitor examples
- **Documents collected** - Materials participants shared or referenced
- **Session artifacts** - Card sorting results, whiteboard photos, journey maps created during sessions

## Structure

Organize by project and date:

```
data/
├── project-name/
│   ├── interviews/
│   │   ├── 2024-01-15-USR001-transcript.md
│   │   ├── 2024-01-15-USR002-transcript.md
│   │   └── ...
│   ├── participants/
│   │   └── user-panel.md
│   ├── surveys/
│   │   └── survey-01-responses.csv
│   └── artifacts/
│       └── ...
```

## Privacy & Ethics

⚠️ **Important**: This directory may contain sensitive information
- Always redact personally identifiable information (PII)
- Follow your research ethics approval and consent agreements
- Never commit unredacted transcripts, recordings, or personal details
- Use unique participant IDs (USR001, USR002, etc.) instead of names

## AI-Friendly Format

Structure data for both human reading and AI processing:
- Use consistent frontmatter with metadata
- Include participant IDs, dates, project tags
- Link to related research questions and hypotheses
- Use markdown tables for structured data

## Moving Up the Hierarchy

Data in this folder is the foundation for:
- **Information** (organized, tagged, contextualized data)
- **Knowledge** (synthesized insights and patterns)

Think: _"What happened?"_ → Data answers this question.
