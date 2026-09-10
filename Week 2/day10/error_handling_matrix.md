# Day 10 — Error-Handling Matrix (Standalone)

| Failure Type       | Retry? | Max Retries | User Message                                              | Notes |
|--------------------|--------|-------------|-----------------------------------------------------------|-------|
| Timeout            | Yes    | 2           | Something went wrong on our side. Please try again.       | Temporary |
| Rate limit         | Yes    | 2           | Too many requests. Please wait a moment and try again.    | Temporary |
| Invalid JSON       | No     | 0           | We couldn’t process the response. Please try again.       | Do not retry |
| Empty response     | No     | 0           | We couldn’t process the response. Please try again.       | Do not retry |
| Provider error     | Yes    | 2           | Service temporarily unavailable. Please try again.        | Temporary |
| Invalid input      | No     | 0           | Please describe your issue so we can help.                | User-side |
| Network error      | Yes    | 2           | Network error. Please check your connection.              | Temporary |

## Retry Policy
- Retry only temporary failures.
- Max retries = 2.
- Short delay between attempts.
- Stop after max retries and show the message.
- Never retry invalid input or malformed model output.
