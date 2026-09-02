# Day 10 — Error, Cost & Latency Handling

## Objective
Make the AI feature behave like a real application: every failure has deterministic behaviour, retries are limited, and cost/latency are controlled.

---

## 1. Error-Handling Matrix

| Failure Type       | Detected When                          | Retry?     | Max Retries | User-Facing Message (Mobile)                          | App Behaviour |
|--------------------|----------------------------------------|------------|-------------|-------------------------------------------------------|---------------|
| **Timeout**        | Request exceeds time limit             | Yes        | 2           | Something went wrong on our side. Please try again.   | Retry → then show error |
| **Rate limit**     | Provider returns 429 / rate exceeded   | Yes        | 2           | Too many requests. Please wait a moment and try again.| Wait briefly → retry → then error |
| **Invalid JSON**   | Response cannot be parsed              | No         | 0           | We couldn’t process the response. Please try again.   | Show error, no retry |
| **Empty response** | Model returns empty or null body       | No         | 0           | We couldn’t process the response. Please try again.   | Show error, no retry |
| **Provider error** | 5xx or provider unavailable            | Yes        | 2           | Service temporarily unavailable. Please try again.    | Retry → then show error |
| **Invalid input**  | Empty or whitespace-only user message  | No         | 0           | Please describe your issue so we can help.            | Block request, show message |
| **Network error**  | No connection / DNS / connection reset | Yes        | 2           | Network error. Please check your connection.          | Retry → then show error |

### Retry Rules
- Only retry **temporary** failures (timeout, rate limit, provider error, network).
- Never retry **invalid input**, **invalid JSON**, or **empty response**.
- Maximum retries = **2**.
- Short delay between retries (e.g. 1–2 seconds).
- After max retries → stop and show the user-facing message.
- **No infinite retries.**

---

## 2. Cost & Latency Optimisation Note

### Rough token estimate (sample triage prompt)

| Component                    | Approx. Tokens |
|-----------------------------|----------------|
| System / instructions       | 120–180        |
| User message (typical)      | 20–60          |
| Recent conversation history | 0–400 (with budget) |
| **Total per request**       | **~150–600**   |

Without a context budget, history can easily exceed 1000+ tokens and increase both cost and latency.

### 3 Ways to Reduce Unnecessary Context

1. **Apply a context budget** (Day 9)  
   Keep only the last 3–4 turns fully. Summarise or drop older turns.

2. **Keep the prompt template short**  
   Remove repeated or non-essential instructions. Prefer clear, compact rules.

3. **Do not send large irrelevant data**  
   Avoid attaching full FAQs, long logs, or entire past chats unless the current turn needs them.

### Additional practical tips
- Prefer structured JSON output (easier to validate, less waste).
- Fail fast on empty input (saves a full model call).
- Cache deterministic responses for identical repeated queries when safe.

---

## 3. Updated Prototype Behaviour (Notes)

### Backend / Service layer
- Validate input before calling the model.
- Catch timeout, rate-limit, and provider errors.
- Apply retry policy with max 2 attempts.
- Validate JSON before returning to the mobile app.
- Return a consistent error shape the mobile app can understand.

### Mobile (Flutter) layer
- Show loading state while waiting.
- Map error codes/types to the user-facing messages above.
- Distinguish:
  - Temporary failure → allow manual retry button
  - Invalid input → ask user to fix the message
- Never display raw stack traces or provider error bodies.

### Suggested error response shape (backend → mobile)

```json
{
  "success": false,
  "error_type": "timeout | rate_limit | invalid_json | empty_response | provider_error | invalid_input | network_error",
  "message": "User-friendly text",
  "retryable": true
}
```

---

## 4. Definition of Done Checklist

- [x] Error-handling matrix defined for all required failure types
- [x] Retry rules documented (max 2, only temporary failures)
- [x] User-friendly mobile messages defined
- [x] Token/cost estimate provided
- [x] 3 concrete ways to reduce context documented
- [x] Deterministic behaviour for every listed failure
- [x] No infinite retries

---

## 5. Related Files

- `Week 2/day10/error_handler.py` — example retry + error mapping logic
- `Week 2/day10/error_handling_matrix.md` — same matrix (standalone)
- `docs/day10_error_cost_latency.md` — this document
