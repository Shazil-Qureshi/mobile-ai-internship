# Day 10 — Error, Cost & Latency Tests

## Objective
Verify that every failure type has deterministic behaviour and that retries follow the rules.

## Test Cases

| ID  | Scenario                         | Input / Condition                    | Expected error_type   | Retryable? | Expected user message (summary)           | Result |
|-----|----------------------------------|--------------------------------------|-----------------------|------------|-------------------------------------------|--------|
| T01 | Empty input                      | `""`                                 | invalid_input         | No         | Please describe your issue...             |        |
| T02 | Whitespace only                  | `"   "`                              | invalid_input         | No         | Please describe your issue...             |        |
| T03 | Normal success                   | `"My payment failed"`                | (none – success)      | —          | Structured triage JSON returned           |        |
| T04 | Timeout simulation               | Force timeout exception              | timeout               | Yes        | Something went wrong on our side...       |        |
| T05 | Rate limit simulation            | Force 429 / rate limit               | rate_limit            | Yes        | Too many requests...                      |        |
| T06 | Invalid JSON from provider       | Provider returns `{bad json`         | invalid_json          | No         | We couldn’t process the response...       |        |
| T07 | Empty response from provider     | Provider returns `null` / `{}`       | empty_response        | No         | We couldn’t process the response...       |        |
| T08 | Provider 500 error               | Force 500 / provider down            | provider_error        | Yes        | Service temporarily unavailable...        |        |
| T09 | Network error                    | Force connection error               | network_error         | Yes        | Network error. Please check...            |        |
| T10 | Retry limit respected            | Temporary failure × 3                | timeout (or similar)  | Yes → stop | After 2 retries, final error shown        |        |

## Retry Rules Checked

- [ ] Only temporary failures are retried
- [ ] Max retries = 2
- [ ] Invalid input is never retried
- [ ] Invalid JSON / empty response are never retried
- [ ] After max retries the app stops and shows the message

## Cost / Latency Checks (manual notes)

| Check                                      | Status |
|--------------------------------------------|--------|
| Context budget applied (no unbounded history) |        |
| Prompt kept reasonably short               |        |
| Empty input fails fast (no model call)     |        |

## How to Run (example)

```bash
cd "Week 2/day10"
python error_handler.py
```

Or call your service with the inputs above and record the `error_type` and message.

## Sample Success Response

```json
{
  "success": true,
  "data": {
    "category": "billing",
    "priority": "high",
    "action": "Investigate payment issue",
    "clarification_needed": false
  }
}
```

## Sample Error Response

```json
{
  "success": false,
  "error_type": "timeout",
  "message": "Something went wrong on our side. Please try again.",
  "retryable": true
}
```

## Notes
- Mark each Result column Pass/Fail after you run the tests.
- Temporary failures may be simulated by raising exceptions in the mock provider.
