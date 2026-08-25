# Day 4 — Prompt Evaluation

## Objective
Replace trial-and-error prompting with measurable, reproducible evaluation.

Day 4 evaluates the Support-Triage prompt using 25 deliberately varied test cases. The evaluation measures format compliance, relevance, correctness, failure types, and possible fixes. After evaluating Prompt v1, the prompt is improved into Prompt v2 with rules refined based on recorded failure patterns.

---

## 1. Evaluation Method

```text
Prompt v1
   ↓
25 reproducible test cases
   ↓
Record actual outputs
   ↓
Evaluate each output
   ↓
Calculate v1 pass rate
   ↓
Identify top 3 failure patterns
   ↓
Improve prompt → Prompt v2
   ↓
Run the SAME 25 tests
   ↓
Evaluate v2
   ↓
Calculate v2 pass rate
   ↓
Compare v1 vs v2
```

### Evaluation Criteria

1. **Format compliance** — Does the response follow the required output schema without markdown or formatting artifacts?
2. **Relevance** — Does the response address the customer's actual operational issue and ignore distractors?
3. **Correctness** — Are the category, priority, action, and clarification decisions appropriate?
4. **Failure type** — If the response fails or behaves inconsistently, what specifically went wrong?
5. **Fix** — What prompt rule or guardrail change prevents the failure?

---

## 2. Support-Triage Prompt v1

```text
You are a mobile-app customer support triage assistant.

Task:
Classify the user's support message and determine the appropriate next action.

Input:
- user_message: the customer's message.

Allowed categories:
- account
- billing
- technical
- security
- other

Allowed priorities:
- low
- medium
- high

Rules:
- Do not invent facts.
- If the message is too vague to determine the category, use "other".
- If clarification is needed, set clarification_needed to true.
- Return JSON only.
- Do not include markdown, explanations, or additional text.

Required JSON schema:
{
  "category": "account | billing | technical | security | other",
  "priority": "low | medium | high",
  "action": "string",
  "clarification_needed": true
}
```

---

## 3. 25-Test Evaluation Dataset

| ID  | Category             | Input                                                                                                                      | Expected Behaviour                                              |
|-----|----------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| T01 | Normal               | My payment failed and I need help immediately.                                                                             | Billing/payment issue; urgent handling; valid JSON.             |
| T02 | Normal               | I can't log into my account because I forgot my password.                                                                  | Account/login issue; password recovery action; valid JSON.      |
| T03 | Normal               | The mobile app crashes every time I open the transactions page.                                                            | Technical/app issue; dev escalation; valid JSON.                |
| T04 | Normal               | I was charged twice for the same purchase.                                                                                 | Billing/duplicate charge issue; refund initiation.              |
| T05 | Normal               | I want to update the phone number linked to my account.                                                                    | Account/profile request; verification flow.                     |
| T06 | Vague                | It isn't working.                                                                                                          | Insufficient information; request clarification.                |
| T07 | Vague                | I have a problem with my account.                                                                                          | Insufficient details; request clarification.                |
