# Day 8 — Dynamic Prompt Variables

## Objective
Make prompts reusable across users and contexts by introducing variables, server-side validation, and clear trusted vs untrusted boundaries.

## 1. Variable Specification

| Variable              | Type     | Trusted?   | Default                         | Notes |
|-----------------------|----------|------------|----------------------------------|-------|
| `user_input`          | string   | **Untrusted** | (required)                     | Comes from the end user. Must be sanitized/truncated. |
| `locale`              | string   | Trusted    | `"en"`                           | Only allowed values: en, ur, hi, ar |
| `allowed_categories`  | list     | Trusted    | account, billing, technical, security, other | Controlled by backend |
| `response_limit`      | int      | Trusted    | `100`                            | Clamped between 20 and 300 |

## 2. Trusted vs Untrusted

### Trusted (backend-controlled)
- `locale`
- `allowed_categories`
- `response_limit`

These values are set by the server. The user cannot change them freely.

### Untrusted (user-controlled)
- `user_input`

This text can contain anything (including prompt-injection attempts).  
It must **never** be allowed to redefine the output schema or override system rules.

## 3. Validation Rules Applied

| Case                        | Behaviour                                      |
|-----------------------------|------------------------------------------------|
| Empty `user_input`          | Marked invalid                                 |
| `user_input` > 1000 chars   | Truncated                                      |
| Invalid / missing `locale`  | Falls back to `"en"`                           |
| Empty categories list       | Falls back to default categories               |
| `response_limit` too small  | Raised to minimum (20)                         |
| `response_limit` too large  | Capped at maximum (300)                        |
| Non-integer `response_limit`| Replaced with default (100)                    |
| Adversarial phrases         | Flagged in errors list                         |

## 4. Dynamic Prompt Template

See: `Week 2/day8/prompts/dynamic_triage_prompt.py`

Key idea:
```text
User message:
{user_input}          ← untrusted, injected as data only
```

The schema and rules stay under backend control.

## 5. 15-Case Test Summary

| ID  | Scenario                        | Expected Behaviour                  |
|-----|---------------------------------|-------------------------------------|
| T01 | Normal input                    | Valid, prompt built                 |
| T02 | Empty input                     | Invalid                             |
| T03 | Very long input (1500 chars)    | Truncated to 1000                   |
| T04 | Invalid locale (`fr`)           | Falls back to `en`                  |
| T05 | Missing locale                  | Falls back to `en`                  |
| T06 | Empty categories                | Uses default categories             |
| T07 | Excessive response_limit        | Capped at 300                       |
| T08 | Too small response_limit        | Raised to 20                        |
| T09 | Non-integer response_limit      | Uses default 100                    |
| T10 | Urdu locale                     | Accepted                            |
| T11 | Custom categories               | Accepted                            |
| T12 | Adversarial input               | Flagged, still processed safely     |
| T13 | Whitespace only                 | Treated as empty / invalid          |
| T14 | Dirty categories list           | Cleaned                             |
| T15 | All defaults                    | Uses all default values             |

Run the tests:
```bash
cd "Week 2/day8"
python test_variables.py
```

## 6. Key Design Decisions

1. **Untrusted text cannot redefine the schema**  
   The JSON schema is written by the backend, not taken from user input.

2. **Defaults are explicit**  
   Every variable has a documented default and clamping rules.

3. **Validation happens before the prompt is built**  
   Bad values are corrected or rejected early.

4. **Prompt injection attempts are detected**  
   Basic pattern matching flags common attack phrases.

## 7. Definition of Done

- [x] Prompt refactored with variables (`user_input`, `locale`, `allowed_categories`, `response_limit`)
- [x] Server-side validation and defaults implemented
- [x] 15 test combinations created and documented
- [x] Trusted vs untrusted variables clearly documented
- [x] Untrusted user text cannot silently change the output schema
