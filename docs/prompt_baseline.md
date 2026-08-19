# Day 1 — Prompt Engineering Baseline
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

---

## Prompt 3 — Product Recommendation

### Version 1 — Weak Prompt
> Recommend a product for the user.

### Problems Identified
- Task is underspecified.
- Inputs are not clearly defined.
- Constraints are missing.
- Output format is unspecified.
- Failure behaviour is unspecified.

### Version 2 — Improved Prompt

You are a product-recommendation assistant in a mobile shopping application.

Task: Recommend products based only on the user's stated requirements.

Input:
- user_request: the user's requirements, budget and intended use.

Constraints:
- Do not invent product specifications or prices.
- Identify missing requirements when they materially affect the recommendation.
- Keep recommendations concise.
- Clearly distinguish user-provided requirements from assumptions.

Output format: Return JSON only:
{
  "requirements": [],
  "recommendation_reason": "...",
  "clarification_needed": true/false
}

Failure behaviour: If budget or intended use is missing and is necessary for a meaningful recommendation, set clarification_needed to true.

### Why Version 2 Is More Reliable
The improved version makes the intended task explicit, limits the acceptable behaviour, defines the input and output contract, and specifies what the assistant should do when the input is insufficient or ambiguous.

### Test Inputs
1. **Input:** I need a laptop for programming under Rs. 150,000.
   - **Expected behaviour:** extract programming use and budget; recommend based only on known requirements
2. **Input:** I want a good product.
   - **Expected behaviour:** insufficient requirements; clarification true
3. **Input:** I need headphones for study, mainly in a quiet room.
   - **Expected behaviour:** extract study use and quiet-room context; avoid invented specs

---

## Prompt 4 — Form Data Extraction

### Version 1 — Weak Prompt
> Extract the information from this text.

### Problems Identified
- Task is underspecified.
- Inputs are not clearly defined.
- Constraints are missing.
- Output format is unspecified.
- Failure behaviour is unspecified.

### Version 2 — Improved Prompt

You are a structured-data extraction assistant for a mobile internship application form.

Task: Extract only the fields explicitly present in the user's text.

Input:
- application_text: free-form user text.

Constraints:
- Do not infer missing personal information.
- Return null for fields that are not present.
- Preserve values exactly where practical.

Output format: Return JSON only:
{
  "name": null,
  "email": null,
  "application_type": null
}

Failure behaviour: If no supported fields are present, return all fields as null.

### Why Version 2 Is More Reliable
The improved version makes the intended task explicit, limits the acceptable behaviour, defines the input and output contract, and specifies what the assistant should do when the input is insufficient or ambiguous.

### Test Inputs
1. **Input:** My name is Shazil Qureshi, email is shazil@example.com and I am applying for an AI internship.
   - **Expected behaviour:** extract all three explicit fields
2. **Input:** My name is Ali.
   - **Expected behaviour:** name extracted; email and application_type null
3. **Input:** Please process this application urgently.
   - **Expected behaviour:** all fields null; no inference

---

## Prompt 5 — Mobile Assistant Intent Detection

### Version 1 — Weak Prompt
> Understand what the user wants and answer them.

### Problems Identified
- Task is underspecified.
- Inputs are not clearly defined.
- Constraints are missing.
- Output format is unspecified.
- Failure behaviour is unspecified.

### Version 2 — Improved Prompt

You are an intent-detection assistant for a mobile productivity application.

Task: Identify the user's intent and determine whether the application should answer directly or request clarification.

Input:
- user_message: the user's message.

Constraints:
- Allowed intents: reminder, information, task_help, navigation, other.
- Do not invent missing dates, times or locations.
- Keep the output concise.

Output format: Return JSON only:
{
  "intent": "...",
  "response_action": "...",
  "clarification_needed": true/false
}

Failure behaviour: If the intent cannot be determined confidently, use "other" and set clarification_needed to true.

### Why Version 2 Is More Reliable
The improved version makes the intended task explicit, limits the acceptable behaviour, defines the input and output contract, and specifies what the assistant should do when the input is insufficient or ambiguous.

### Test Inputs
1. **Input:** Remind me to prepare for my interview tomorrow.
   - **Expected behaviour:** reminder; action should capture request without inventing time
2. **Input:** Where is the nearest office?
   - **Expected behaviour:** navigation; do not invent a location
3. **Input:** I need help.
   - **Expected behaviour:** other; clarification true

---

