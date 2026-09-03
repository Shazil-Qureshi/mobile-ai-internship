# Week 2 Improvement Challenge — AI Mobile Assistant

## Overview

This challenge delivers a small end-to-end **Flutter-facing AI assistant** with a defined backend contract. It combines the work from Days 6–10 into one coherent feature.

```text
Flutter UI
   ↓
Service layer (no API keys)
   ↓
Backend / Mock provider
   ↓
Prompt template + validation
   ↓
Structured JSON
   ↓
Typed model → Loading / Success / Error UI
```

---

## Requirements Checklist

| Requirement                                      | Status | Evidence |
|--------------------------------------------------|--------|----------|
| User enters text in Flutter                      | Done   | Day 7 `TriageScreen` |
| Backend/provider processes request               | Done   | Day 6 `app.py` + mock provider |
| Validated structured response → typed app data   | Done   | Day 7 `TriageResponse.fromJson` |
| Loading state                                    | Done   | Day 7 UI |
| Invalid input handled                            | Done   | Day 10 error matrix + handler |
| Provider failure handled                         | Done   | Day 10 retry + user messages |
| At least 20 tests                                | Done   | `challenge_20_tests.md` |

---

## Architecture

### Backend contract (request)

```json
{
  "user_message": "string"
}
```

### Backend contract (success response)

```json
{
  "success": true,
  "data": {
    "category": "account | billing | technical | security | other",
    "priority": "low | medium | high",
    "action": "string",
    "clarification_needed": true,
    "model": "string"
  }
}
```

### Backend contract (error response)

```json
{
  "success": false,
  "error_type": "timeout | rate_limit | invalid_json | empty_response | provider_error | invalid_input | network_error",
  "message": "User-friendly text",
  "retryable": true
}
```

---

## Components Used

| Day | Component                         | Role in Challenge |
|-----|-----------------------------------|-------------------|
| 6   | Mock provider + app service       | Process request, return structured data |
| 7   | Flutter screen + model + service  | UI states + typed parsing |
| 8   | Dynamic variables + validation    | Safe prompt building |
| 9   | Context budget (optional)         | Multi-turn ready |
| 10  | Error matrix + retry rules       | Deterministic failure handling |

---

## Security

- No LLM API keys in Flutter
- Secrets stay on backend only
- User input treated as untrusted
- Output validated before UI consumes it

---

## How to Demo

1. Open the Flutter triage screen
2. Enter: `My payment failed and I need help`
3. Observe loading → success (billing / high)
4. Enter empty text → invalid input message
5. Simulate provider failure (or disconnect) → retryable error message

---

## Scoring Focus (from Master KPI)

- **Mobile/AI Technical Implementation** (primary)
- **Testing & QA**
- Documentation and delivery also contribute

---

## Definition of Done

- [x] End-to-end path: Flutter → backend/mock → structured response → UI
- [x] Loading, invalid input, provider failure handled
- [x] Typed model (no raw JSON in UI logic)
- [x] ≥ 20 tests documented
- [x] No secrets in mobile code
- [x] Deterministic error behaviour
