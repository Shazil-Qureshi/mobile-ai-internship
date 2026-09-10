# Day 3 — Mobile AI UX Patterns

## Common Interaction Pipeline
**User action → App input → Backend request → AI task → Structured response → UI state**

## Required UI States
- Loading
- Empty
- Error
- Retry
- Low confidence

## Reliability Principle
AI output should be validated against a defined response contract before the application displays or consumes it.

## Fallback Principle
Every flow has a controlled fallback. Invalid or incomplete AI output should not be rendered as uncontrolled raw model text.

## Five Use Cases
| Use case | Primary interaction | AI task | Main fallback |
|---|---|---|---|
| Chat | Send a message | Understand and respond | Retry / clarification |
| Smart Search | Natural-language search | Interpret intent and find results | Refine / retry |
| Extraction | Submit content | Extract fields | Manual entry / retry |
| Recommendation | Describe requirements | Match suitable options | Refine / retry |
| Assistant / Form Help | Ask about a field | Explain or guide | Manual entry / clarification |
