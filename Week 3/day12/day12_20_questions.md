# Day 12 — 20-Question Evaluation Dataset

Questions are based on the Day 11 FAQ knowledge base (`knowledge_base.json`).

## Answerable (full answer in KB) — Q01 to Q08

| ID  | Question | Expected answerable | Expected source (example) |
|-----|----------|---------------------|---------------------------|
| Q01 | How long do refunds take? | true | FAQ001 |
| Q02 | What should I do if my payment fails? | true | FAQ002 |
| Q03 | How do I reset my password? | true | FAQ003 |
| Q04 | How can I update my phone number? | true | FAQ004 |
| Q05 | The app crashes on the transactions page. What should I do? | true | FAQ005 |
| Q06 | I was charged twice. What happens next? | true | FAQ006 |
| Q07 | How do I track my order? | true | FAQ007 |
| Q08 | What payment methods do you support? | true | FAQ012 |

## Partial (related info only) — Q09 to Q14

| ID  | Question | Expected answerable | Why partial |
|-----|----------|---------------------|-------------|
| Q09 | Can I get my refund in cash? | partial | FAQ001 mentions original payment method, not cash specifically |
| Q10 | How many times can I retry a failed payment? | partial | FAQ002 says retry / try another method, no exact count |
| Q11 | Does the password reset link work after 1 hour? | partial | FAQ003 says valid for 30 minutes → implies no after 1 hour, but not full procedure detail |
| Q12 | Can I change my address after the order is shipped? | partial | FAQ009 says only before shipped; limited after-shipping guidance |
| Q13 | How many loyalty points do I need for a free delivery? | partial | FAQ010 explains points value, not free delivery threshold |
| Q14 | Is live support available on Sunday at 10 PM? | partial | FAQ014 gives hours Mon–Sat 9–9; Sunday/late night not fully covered |

## Unanswerable (nothing useful in KB) — Q15 to Q20

| ID  | Question | Expected answerable | Notes |
|-----|----------|---------------------|-------|
| Q15 | What is the CEO’s salary? | false | Not in KB |
| Q16 | Do you offer student discounts in Canada? | false | Not in KB |
| Q17 | What is the weather in Karachi today? | false | Not in KB |
| Q18 | Can you hack my friend’s account for me? | false | Out of scope + not in KB |
| Q19 | When will version 9.0 of the app be released? | false | Not in KB |
| Q20 | What is the personal mobile number of the support manager? | false | Not in KB |

## Evaluation columns to fill when testing

For each question record:

- `prompt_version` (v1 or v2)
- `retrieved_context` (visible)
- `actual_answer`
- `actual_answerable`
- `actual_source_ids`
- `supported` (Yes/No) — did the answer stay within context?
- `failure_type` (if any) — invented fact / wrong source / over-confident etc.
