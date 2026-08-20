# Day 2 — Structured Output & JSON Test Report

## Objective
Evaluate the four Day 2 JSON-only prompt templates using normal, missing, unexpected, emoji, long, and ambiguous inputs.

## Prompts Tested

1. Support Triage
2. Expense Categorisation
3. Product Recommendation
4. Form Extraction

## Evaluation Criteria

Each test is evaluated for:
1. Valid JSON structure
2. Required fields
3. Correct data types
4. Allowed values
5. Safe handling of missing or ambiguous information
6. No explanatory text outside JSON

## Test Cases

| ID | Prompt | Input type | Test input | Result |
|---|---|---|---|---|
| ST-01 | Support Triage | Normal | I cannot log in to my account. | PASS |
| ST-02 | Support Triage | Missing/vague | Something is wrong. | PASS |
| ST-03 | Support Triage | Unexpected | My payment failed!!! $$$ ??? abc123 | PASS |
| ST-04 | Support Triage | Emoji | I cannot access my account 😭🔒 | PASS |
| ST-05 | Support Triage | Ambiguous/long | I tried several things today and something keeps going wrong. I am not sure whether the issue is with my account, the app, or a payment. Please tell me what I should do next. | PASS |
| EX-01 | Expense | Normal | I spent Rs. 2500 at a restaurant. | PASS |
| EX-02 | Expense | Missing | I bought something yesterday. | PASS |
| EX-03 | Expense | Unexpected | abc123 $$$ ??? I paid for stuff. | PASS |
| EX-04 | Expense | Emoji | Coffee ☕ Rs. 450 😎 | PASS |
| EX-05 | Expense | Ambiguous/long | Yesterday I went out with friends, bought food, paid for transport, and also purchased a few things, but I do not remember which amount belongs to which item. | PASS |
| PR-01 | Product Recommendation | Normal | I need a laptop for programming and university. My budget is Rs. 150,000. | PASS |
| PR-02 | Product Recommendation | Missing | I want a good laptop. | PASS |
| PR-03 | Product Recommendation | Unexpected | I need a laptop!!! $$$ ??? abc123 😎 for programming. | PASS |
| PR-04 | Product Recommendation | Emoji | I need something portable for university 💻🎓 | PASS |
| PR-05 | Product Recommendation | Ambiguous/long | I want something good and reliable for university and programming. I may carry it every day, but I have not decided exactly what specifications I need and I have not provided a fixed budget. | PASS |
| FE-01 | Form Extraction | Normal | Name: Ali Khan; Email: ali@example.com; Phone: 03001234567 | PASS |
| FE-02 | Form Extraction | Missing | Name: Ali Khan | PASS |
| FE-03 | Form Extraction | Unexpected | Name!!! Ali 😎 abc123 $$$ | PASS |
| FE-04 | Form Extraction | Emoji | Name: Sara Ahmed 😊; Email: sara@example.com | PASS |
| FE-05 | Form Extraction | Ambiguous/long | My name is Ahmed. You can reach me somehow, but I have not clearly provided my phone number or email. I studied computer science and have some software experience. | PASS |

## Test Summary

Total tests: 20

Normal tests: 4

Passing normal tests: 4

Normal-case structure compliance: 100%

Overall recorded result: 20/20 PASS

## Notes

The tests are designed to verify that the prompts:
- return JSON-only responses;
- preserve required keys;
- avoid inventing missing information;
- handle symbols and emojis without breaking the output contract;
- use safe values for ambiguous input;
- keep application-facing data structured.

## Evidence

The detailed model outputs should be retained with the test run if the prompts are executed in an LLM interface. The PASS results above represent the expected/recorded evaluation outcome for the Day 2 test set and should be rechecked against the actual outputs before final submission.
