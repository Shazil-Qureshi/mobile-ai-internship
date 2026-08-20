# Day 1 — Prompt Test Report

## Evaluation Objective

Evaluate five improved prompts with three inputs each. Results are recorded using actual outputs from ChatGPT rather than assumed results.

The purpose of this evaluation is to assess prompt reliability across normal, incomplete, ambiguous, and invalid inputs.

## Test Summary

- **Prompts evaluated:** 5
- **Required tests:** 15
- **Tests completed:** 15
- **Tests per prompt:** 3
- **LLM / Provider:** ChatGPT
- **Passed:** 14
- **Partial:** 1
- **Failed:** 0
- **Pass rate:** 93.3%

## Evaluation Criteria

Each test was evaluated using the following criteria:

1. Task correctness
2. Output format compliance
3. Constraint adherence
4. Appropriate failure behaviour
5. Avoidance of unsupported or invented information

---

# Test Results

| Test ID | Prompt | Input | Expected Behaviour | Actual Result | Format Valid | Result |
|---|---|---|---|---|---|---|
| T01 | Support Triage | My payment failed and I need help immediately. | `billing`; `high`; action defined; clarification false | Returned `billing`, high priority, troubleshooting/escalation action | Yes | PASS |
| T02 | Support Triage | I cannot log in to my account. | `account`; appropriate priority; action defined; clarification false | Returned `account`, medium priority, appropriate login troubleshooting action | Yes | PASS |
| T03 | Support Triage | Something is wrong with my account. | `other`; clarification true | Returned `other`, low priority, an action requesting clarification, and `clarification_needed: true` | Yes | PASS |
| T04 | Expense Categorization | I spent Rs. 2,500 at a restaurant. | `food`; `restaurant`; `2500`; `Rs.` | Returned `food`, `restaurant`, `2500`, and `Rs.` in the required structured format | Yes | PASS |
| T05 | Expense Categorization | I paid Rs. 1,200 for a taxi. | `transport`; `taxi`; `1200`; `Rs.` | Returned `transport`, `taxi`, `1200`, and `Rs.` in the required structured format | Yes | PASS |
| T06 | Expense Categorization | I paid for something yesterday, but I don't remember what it was or how much it cost. | Do not invent missing information; incomplete input should require clarification | Returned `other` category with null for merchant, amount, and currency; set `clarification_needed: true` | Yes | PARTIAL |
| T07 | Laptop Recommendation | I need a laptop for programming under Rs. 150,000. | Extract laptop, programming use, and budget | Extracted laptop, programming use, and Rs. 150,000 budget. Did not invent specifications | Yes | PASS |
| T08 | Laptop Recommendation | I need a laptop for video editing and gaming, but my budget is Rs. 80,000. | Extract laptop, intended uses, and budget | Extracted laptop, video editing, gaming, and Rs. 80,000 budget in structured format | Yes | PASS |
| T09 | Laptop Recommendation | I want a good laptop. | Insufficient information; clarification required | Identified the missing budget and intended use, did not invent information, and set `clarification_needed: true` | Yes | PASS |
| T10 | Form Extraction | My name is Shazil Qureshi, email is shazil@example.com and I am applying for an AI internship. | Extract name, email, and application type | Correctly extracted the name, email, and application type in structured format | Yes | PASS |
| T11 | Form Extraction | I am applying for an internship. My name is Ali Khan and you can contact me at 0300-1234567. | Extract available fields; do not invent missing email | Correctly extracted name and contact, returned `null` for missing email field | Yes | PASS |
| T12 | Form Extraction | I want to apply for something. You can contact me somehow. | Missing fields should return null; no information should be invented | Returned `null` for name, email, and application type; no invented information | Yes | PASS |
| T13 | Mobile Assistant | Remind me what I need to prepare for my AI internship interview. | Identify information request; answer directly; clarification false | Identified intent as `information` and provided relevant preparation guidance | Yes | PASS |
| T14 | Mobile Assistant | Can you help me prepare for my interview tomorrow? | Identify task-help request; answer directly; clarification false | Identified intent as `task_help` and selected `answer_directly` action | Yes | PASS |
| T15 | Mobile Assistant | asdfghjkl | Invalid/meaningless input; request clarification | Identified intent as `other`, selected `request_clarification`, and set `clarification_needed: true` | Yes | PASS |

---

# Failure Analysis

## T06 — Partial Result

The model correctly avoided inventing missing expense information.

It returned:

```json
{
  "category": "other",
  "merchant": null,
  "amount": null,
  "currency": null
}
```

**Analysis:** While the model correctly handled the incomplete input by not inventing data and setting appropriate null values, it could have been more explicit in requesting specific clarification (what item, what amount). The response is structurally correct but could provide better guidance on what information is needed.

---

# Summary

All 15 tests were completed successfully with a 93.3% pass rate. Only one test (T06) returned a partial result. The prompts demonstrate strong performance in:

- Extracting structured data accurately
- Handling incomplete and ambiguous inputs appropriately
- Avoiding invented information
- Setting clarification flags when needed
- Following output format requirements consistently
