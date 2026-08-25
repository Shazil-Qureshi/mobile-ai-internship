# Week 1 — Prompt Engineering Baseline
## Objective
Create five intentionally weak prompts, rewrite them using the required structured prompt framework, and establish a 15-test baseline.

## Prompt 1 — Customer Support Triage

### Version 1 — Weak Prompt
> Help the customer with their problem.

### Problems Identified
- Task is underspecified.
- Inputs are not clearly defined.
- Constraints are missing.
- Output format is unspecified.
- Failure behaviour is unspecified.

### Version 2 — Improved Prompt

You are a mobile-app customer support triage assistant.

Task: Classify the user's support message and determine the appropriate next action.

Input:
- user_message: the customer's message.

Constraints:
- Use only these categories: account, billing, technical, security, other.
- Use priority: low, medium, or high.
- Do not invent facts.
- If the message is too vague to classify confidently, request clarification.

Output format: Return JSON only:
{
  "category": "...",
  "priority": "...",
  "action": "...",
  "clarification_needed": true/false
}

Failure behaviour: If the input is empty, ambiguous, or outside the supported categories, set clarification_needed to true and use category "other".

### Why Version 2 Is More Reliable
The improved version makes the intended task explicit, limits the acceptable behaviour, defines the input and output contract, and specifies what the assistant should do when the input is insufficient or ambiguous.

### Test Inputs
1. **Input:** My payment failed and I need help immediately.
   - **Expected behaviour:** billing; high priority; clear action; clarification false
2. **Input:** I cannot log in to my account.
   - **Expected behaviour:** account; appropriate priority; clear action; clarification false
3. **Input:** Something is wrong with my account.
   - **Expected behaviour:** ambiguous; request clarification; clarification true

---

## Prompt 2 — Expense Categorisation

### Version 1 — Weak Prompt
> Categorize this expense.

### Problems Identified
- Task is underspecified.
- Inputs are not clearly defined.
- Constraints are missing.
- Output format is unspecified.
- Failure behaviour is unspecified.

### Version 2 — Improved Prompt

You are an expense-categorisation assistant for a mobile finance application.

Task: Identify the expense category from the user's transaction description.

Input:
- expense_description: text describing the expense.

Constraints:
- Allowed categories: food, transport, shopping, bills, healthcare, education, entertainment, other.
- Do not invent an amount or merchant.
- Use "other" when the category cannot be determined.

Output format: Return JSON only:
{
  "category": "...",
  "merchant": "...",
  "amount": null,
  "currency": null
}

Failure behaviour: If the description is empty or insufficient to determine a category, return category "other" and leave unknown fields null.

### Why Version 2 Is More Reliable
The improved version makes the intended task explicit, limits the acceptable behaviour, defines the input and output contract, and specifies what the assistant should do when the input is insufficient or ambiguous.

### Test Inputs
1. **Input:** I spent Rs. 2500 at a restaurant.
   - **Expected behaviour:** food; amount 2500; currency Rs if explicitly present
2. **Input:** Paid Rs. 1800 for a taxi.
   - **Expected behaviour:** transport; amount 1800
3. **Input:** I paid for something yesterday.
   - **Expected behaviour:** other; unknown fields remain null
