# Week 2 Improvement Challenge — AI Mobile Assistant

## What this is
An end-to-end Flutter-facing AI support triage assistant with a defined backend contract.

## How the pieces connect

```text
Flutter (Day 7)
  TriageScreen + AiService + TriageResponse
        ↓
Backend / Mock (Day 6)
  app.py + mock_provider + prompts
        ↓
Validation & Errors (Day 8 + Day 10)
  dynamic variables + error_handler
        ↓
Structured JSON → typed UI states
```

## Quick start

### Backend (mock)
```bash
cd "Week 2/day6"
python app.py
```

### Flutter
```bash
# Use the Day 7 Flutter code
# Ensure http package is in pubspec.yaml
flutter pub get
flutter run
```

By default the Flutter service uses `classifyMock()` so it works offline.

## Backend contract

**Request**
```json
{ "user_message": "My payment failed" }
```

**Success**
```json
{
  "success": true,
  "data": {
    "category": "billing",
    "priority": "high",
    "action": "Investigate payment issue",
    "clarification_needed": false,
    "model": "mock-triage-v1"
  }
}
```

**Error**
```json
{
  "success": false,
  "error_type": "invalid_input",
  "message": "Please describe your issue so we can help.",
  "retryable": false
}
```

## Tests
See `tests/challenge_20_tests.md` (24 cases).

## Security
- No API keys in Flutter
- All secrets stay on the backend
- User input is untrusted
- Output is validated before the UI uses it

## Related docs
- `docs/week2_challenge_report.md`
- Days 6–10 individual reports
