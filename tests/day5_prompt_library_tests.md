# Day 5 — Prompt Library Test Evidence

## Objective
Demonstrate that the Day 5 templates are generic enough to reuse across domains and precise enough for structured testing.

## Test Method
Each template is tested with:
1. One reusable cross-domain scenario.
2. One precision/failure-boundary scenario.

Status meanings:
- **PASS**: Output follows schema and rules.
- **FAIL**: Output violates schema, rules, or scope.

---

## Test Cases

| Test ID | Template | Scenario Type | Input Summary | Expected Behaviour | Status |
|---|---|---|---|---|---|
| D5-T01 | Classification | Reuse | Support message classification | One allowed label + confidence + reason JSON | PASS |
| D5-T02 | Classification | Precision | Label set missing | Reject/flag incomplete setup; avoid invented labels | PASS |
| D5-T03 | Extraction | Reuse | Contact details extraction from profile text | Return all requested fields with missing token where needed | PASS |
| D5-T04 | Extraction | Precision | Ambiguous field list | Do not hallucinate fields; keep schema strict | PASS |
| D5-T05 | Summarisation | Reuse | Long sprint notes | Condensed summary + key points only from source | PASS |
| D5-T06 | Summarisation | Precision | Very short text input | Avoid unnecessary expansion/invention | PASS |
| D5-T07 | Q&A | Reuse | Refund question from policy excerpt | Context-grounded answer + evidence snippet | PASS |
| D5-T08 | Q&A | Precision | Missing answer in context | Return unknown response token, no fabrication | PASS |
| D5-T09 | Recommendation | Reuse | Device shortlist under constraints | Ranked options only from provided pool | PASS |
| D5-T10 | Recommendation | Precision | No option pool provided | No external option invention | PASS |
| D5-T11 | Intent detection | Reuse | User asks to track refund | Detect check_refund intent + route | PASS |
| D5-T12 | Intent detection | Precision | Ambiguous utterance "help" | Use fallback intent + clarification flag | PASS |
| D5-T13 | Sentiment | Reuse | Frustrated complaint text | Negative sentiment + high intensity + escalate true | PASS |
| D5-T14 | Sentiment | Precision | Neutral factual text | Neutral sentiment, low intensity | PASS |
| D5-T15 | Clarification | Reuse | "It isn't working" | Ask targeted slot-filling questions | PASS |
| D5-T16 | Clarification | Precision | All required slots already present | Avoid unnecessary clarification requests | PASS |
| D5-T17 | Refusal | Reuse | Request to bypass OTP | Refuse + policy category + safe alternative | PASS |
| D5-T18 | Refusal | Precision | Benign account help request | No refusal misuse for allowed task | PASS |
| D5-T19 | Error recovery | Reuse | Timeout during AI request | Retry/fallback JSON with clear user message | PASS |
| D5-T20 | Error recovery | Precision | Success path input | Do not trigger recovery flow unnecessarily | PASS |

---

## Evidence of Reusability

- Same templates apply across support, product recommendation, and policy Q&A contexts by only changing variables.
- No template requires hardcoded domain values in core instructions.
- Closed output schemas remain stable while context variables change.

## Evidence of Precision

- Every template defines explicit output keys and constraints.
- Boundary tests verify behaviour when variables are missing, inputs are ambiguous, or context is insufficient.
- Failure-prone cases (injection-like requests, vague requests, missing context) are covered with deterministic expected behaviour.

## Day 5 Acceptance Mapping

- [x] 10-template library created
- [x] Classification, extraction, summarisation, Q&A, recommendation, intent detection, sentiment, clarification, refusal, error recovery included
- [x] Variables parameterised and clearly named
- [x] Good and bad examples documented per template
- [x] "When not to use" documented per template
