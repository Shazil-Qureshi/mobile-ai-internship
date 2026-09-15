# Day 14 — Evaluation Metrics Deep Dive

## Objective
Report prompt quality like a professional prompt engineer: format compliance, task accuracy, hallucination/unsupported-claim rate, refusal quality, plus sample-size caveats.

---

## Deliverables

| Item | Path |
|------|------|
| Metrics scorecard | `Week 3/day14/metrics_scorecard.md` |
| Narrative insights | `Week 3/day14/narrative_insights.md` |
| This report | `docs/day14_evaluation_metrics.md` |

---

## Metrics computed / defined

1. **Format compliance** — 100% (25/25) on triage v2  
2. **Task accuracy** — 100% (25/25) on triage v2; was 88% on v1  
3. **Hallucination / unsupported-claim rate** — defined on Day 12’s 20 questions; measure and record  
4. **Refusal quality** — defined on Day 13’s 25 adversarial cases; measure and record  

---

## Scorecard snapshot

| Metric | Value | Source |
|--------|-------|--------|
| Format compliance | 100% | Day 4 eval |
| Task accuracy (v2) | 100% | Day 4 eval |
| Lift vs v1 | +12 pp | Day 4 |
| Unsupported-claim rate | (fill after RAG run) | Day 12 |
| Adversarial block rate | (fill after security run) | Day 13 |

---

## Sample-size caveats

- N = 20–25 per suite → percentages move with few cases  
- Report **counts** (e.g. 2/20) not only %  
- Treat results as **directional** evidence for the internship, not production SLAs  
- Larger sets needed before tight confidence claims  

---

## Reproducibility (Definition of Done)

Metrics can be recomputed from saved artifacts:
- Day 4 evaluation table / dataset  
- Day 12 twenty questions + grounded context  
- Day 13 adversarial dataset + before/after sheet  
- Explicit pass/fail rules in `metrics_scorecard.md`  

---

## Definition of Done checklist

- [x] Format compliance reported  
- [x] Task accuracy reported (with v1→v2 comparison)  
- [x] Hallucination/unsupported metric defined and linked to dataset  
- [x] Refusal quality metric defined and linked to adversarial suite  
- [x] Markdown scorecard dashboard created  
- [x] Narrative insights written  
- [x] Sample-size caveats documented  
- [x] Reproducible from saved datasets  

---

## Suggested commit message

```text
feat(day14): evaluation metrics scorecard, narrative insights, sample-size caveats
```
