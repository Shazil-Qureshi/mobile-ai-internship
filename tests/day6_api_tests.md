# Day 6 — API / Service Tests

## Objective
Verify that the Python service correctly:
- Accepts user input
- Builds the prompt
- Calls the mock provider
- Returns structured JSON
- Handles empty / edge inputs

## Test Cases

| ID  | Input                                      | Expected Category | Expected clarification_needed | Result |
|-----|--------------------------------------------|-------------------|-------------------------------|--------|
| T01 | My payment failed and I need help          | billing           | false                         | Pass   |
| T02 | I can't log into my account                | account           | false                         | Pass   |
| T03 | The app crashes on the transactions page   | technical         | false                         | Pass   |
| T04 | It isn't working                           | other             | true                          | Pass   |
| T05 | (empty string)                             | other             | true                          | Pass   |
| T06 | Please refund 2500 PKR                     | billing           | false                         | Pass   |
| T07 | I forgot my password                       | account           | false                         | Pass   |

## How to Run

```bash
cd "Week 2/day6"
python app.py
```

## Sample Output (T01)

```json
{
  "category": "billing",
  "priority": "high",
  "action": "Investigate payment issue",
  "clarification_needed": false,
  "model": "mock-triage-v1"
}
```

## Notes
- All tests currently use the **Mock Provider**.
- No real API key is used.
- Response contract stays the same when a real provider is connected later.
