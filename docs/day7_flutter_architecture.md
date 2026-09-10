# Day 7 — Flutter-to-AI Architecture

## Overview

Day 7 connects the mobile UI to the AI service created on Day 6.

```text
Flutter UI (TriageScreen)
        ↓
AiService (no secrets)
        ↓
Backend / Mock Provider
        ↓
TriageResponse (typed model)
        ↓
Clean UI states (loading / success / error)
```

## Key Files

| File | Responsibility |
|------|----------------|
| `lib/models/triage_response.dart` | Typed model + safe JSON parsing |
| `lib/services/ai_service.dart` | Network calls + mock + error handling |
| `lib/screens/triage_screen.dart` | UI with all required states |
| `lib/main.dart` | App entry point |

## States Implemented

1. **Initial** — empty form
2. **Loading** — spinner while waiting
3. **Success** — shows category, priority, action
4. **Error** — network / malformed / empty input

## Security

- No API keys in Flutter
- Mobile only talks to our own backend (or mock)
- Backend (Day 6) is the only place that may hold provider credentials

## How to Test

1. Run the app (`flutter run`)
2. Try these inputs:
   - `My payment failed`
   - `I can't log into my account`
   - `The app crashes`
   - `It isn't working`
   - (empty submit)

## Definition of Done

- [x] Screen with input, submit, loading, result, error
- [x] Typed model (no raw JSON in UI)
- [x] Service layer
- [x] Handles failures without crashing
- [x] No secrets in Flutter code
