# Day 14 — Narrative Insights

## 1. What the metrics say

**Format compliance is solved for triage.**  
Structured JSON with required fields hit 100% once the schema and rules were explicit. This matters for Flutter: the app can parse responses without defensive guessing.

**Task accuracy improved through evaluation, not vibes.**  
Moving from 88% → 100% on the 25-case set came from fixing three failure patterns (urgency on vague input, security misclassification, action phrasing). That is the Day 4 lesson applied as a metric story.

**Grounding and security are the next quality frontiers.**  
Triage classification can be accurate while RAG still invents details, or while injection attacks still succeed. Day 12 (unsupported-claim rate) and Day 13 (block rate) complete the picture.

---

## 2. Insights by metric

### Format compliance
- Strict schema + “JSON only” instructions work when validated on the backend.
- Mobile should still handle malformed payloads (Day 7/10), but the model side is stable.

### Task accuracy
- Edge cases (vague, multilingual, adversarial) dominate residual risk.
- A small labeled set is enough to drive iteration if failure types are tagged.

### Hallucination / unsupported claims
- Ungrounded answers look fluent but break trust in support policies.
- Measuring unsupported rate on answerable / partial / unanswerable slices shows where the prompt fails.

### Refusal quality
- Good refusals are short, calm, and still offer a legitimate path (“describe your order issue”).
- Multilingual and encoded jailbreaks must be scored, not only English overrides.

---

## 3. Trade-offs observed

| Choice | Benefit | Cost / risk |
|--------|---------|-------------|
| Strict JSON schema | Easy Flutter parsing | Model may need retries if it drifts |
| Context budget (Day 9) | Lower latency/cost | May drop useful older facts |
| Hard security rules | Higher block rate | Over-refusal on edge-case support asks |
| Small eval sets | Fast iteration | Wide uncertainty on true rate |

---

## 4. Recommendations

1. **Keep the triage scorecard green** — re-run the 25 cases when the prompt changes.  
2. **Fill RAG unsupported rate and adversarial block rate** with real runs; put numbers in the scorecard.  
3. **Report counts + percentages** (e.g. 1/20 unsupported) because N is small.  
4. **Promote refusal style** from Day 13 into production triage/RAG templates.  
5. **Automate later** — same metrics can become CI checks on prompt PRs.

---

## 5. One-paragraph executive summary (for managers)

> Our support-triage prompt reaches 100% format compliance and 100% task accuracy on a 25-case held evaluation after iterative patching (+12 points vs baseline). Remaining quality work focuses on grounded RAG (unsupported-claim rate) and adversarial robustness (injection block rate). Metrics are reproducible from saved datasets; sample sizes are modest, so we report counts alongside percentages and treat results as directional evidence for the internship KPI review.
