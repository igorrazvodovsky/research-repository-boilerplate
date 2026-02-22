# Data

_Raw research materials and primary sources_

Unprocessed, factual records from research activities.

## What goes here

### Interview materials
- **Transcripts** - Full, verbatim interview transcripts (redacted for privacy)
- **Recording metadata** - Session info, participant IDs, timestamps (not the recordings)
- **Notes** - Raw session notes, observations, field notes

### Participant information
- **User panel** - Anonymised participant database with segments, characteristics
- **Recruitment data** - Screening responses, scheduling information
- **Consent records** - Documented consent (store actual forms securely offline)

### Survey and test data
- **Survey responses** - Raw response data from questionnaires
- **Usability test results** - Task completion, time-on-task, error rates
- **Analytics exports** - Raw data from tools (GA, Hotjar, etc.)

### Research artefacts
- **Screenshots** - Interface captures, competitor examples
- **Documents collected** - Materials participants shared or referenced
- **Session artefacts** - Card sorting results, whiteboard photos, journey maps created during sessions

## Structure

Organise by project and date:

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
│   └── artefacts/
│       └── ...
```

## Privacy and ethics

⚠️ **Important**: This directory may contain sensitive information
- Always redact personally identifiable information (PII)
- Follow research ethics approval and consent agreements
- Never commit unredacted transcripts, recordings, or personal details
- Use unique participant IDs (USR001, USR002) instead of names

## Format

Structure for both human reading and AI processing:
- Use consistent frontmatter with metadata
- Include participant IDs, dates, project tags
- Link to related research questions and hypotheses
- Use markdown tables for structured data

