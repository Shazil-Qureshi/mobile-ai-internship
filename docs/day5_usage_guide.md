# Day 5 — Prompt Library Usage Guide

## Objective
Explain how to choose, adapt, and validate reusable prompt templates for mobile AI tasks.

## 1) Template Selection Flow

```text
Define task goal
   ↓
Map goal to pattern
   ↓
Fill required variables
   ↓
Set expected structured output
   ↓
Run test cases (normal + edge + failure)
   ↓
Record results and refine variables/rules
```

## 2) Pattern Selection Matrix

| Task Need | Recommended Template | Primary Output |
|---|---|---|
| Assign one label | Classification | label + confidence |
| Pull known fields | Extraction | extracted_fields |
| Condense long text | Summarisation | summary + key_points |
| Answer from provided context | Q&A | answer + evidence |
| Rank options by constraints | Recommendation | ranked options |
| Route user request | Intent detection | intent + next_route |
| Measure user tone | Sentiment | sentiment + intensity |
| Resolve ambiguity | Clarification | targeted questions |
| Decline unsafe request | Refusal | decision + safe alternative |
| Handle AI/system failure | Error recovery | retry/fallback/escalate |

## 3) Variable Adaptation Rules

1. Keep variable names explicit and stable.
2. Keep allowed labels/options closed and enumerable.
3. Keep constraints concrete (limits, formats, schema).
4. Separate source input from rules and output schema.
5. Use fallback variables (`unknown_response`, `fallback_intent`, `fallback_action`) for predictable failure behaviour.

## 4) Structured Output Requirements

- Return JSON only.
- Do not include markdown wrappers.
- Keep output keys fixed for downstream validation.
- Include confidence/flags where uncertainty matters.
- Explicitly define missing-value behaviour.

## 5) Precision vs Reusability Guidance

To keep templates reusable but testable:
- Reusable: keep domain-specific details in variables, not hardcoded text.
- Precise: keep response schema and allowed outputs strict.
- Reusable: adapt context and options per feature.
- Precise: preserve rule blocks and safety constraints.

## 6) Common Adaptation Mistakes

- Missing allowed label set for classification/intent tasks.
- Asking extraction without listing required fields.
- Using recommendation prompts with no option pool.
- Asking Q&A without context boundaries.
- Returning free-form text where structured output is required.

## 7) Review/Handover Checklist

- [x] Correct template chosen for task type
- [x] All template variables filled
- [x] Output schema defined and stable
- [x] Good and bad examples reviewed
- [x] "When not to use" respected
- [x] Test evidence recorded in `tests/day5_prompt_library_tests.md`
