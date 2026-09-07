# Day 12 — Grounded Answer Prompt

## Objective
Design prompts that respect supplied evidence. Measure unsupported-answer rate on 20 questions (answerable, partial, unanswerable).

---

## 1. RAG Prompt v1

See: `Week 3/day12/rag_prompt_v1.txt`

Core idea:
- Answer using ONLY supplied context
- Return `answer`, `answerable`, `confidence`, `source_ids`

---

## 2. RAG Prompt v2 (improved)

See: `Week 3/day12/rag_prompt_v2.txt`

### Improvements over v1
- Explicit `true | partial | false` definitions
- Clear rule: if false, answer must say info is not in the knowledge base
- `source_ids` must only come from the given context
- Marks user question as untrusted, context as trusted

---

## 3. 20-Question Dataset

See: `Week 3/day12/day12_20_questions.md`

| Type | Count | IDs |
|------|-------|-----|
| Answerable | 8 | Q01–Q08 |
| Partial | 6 | Q09–Q14 |
| Unanswerable | 6 | Q15–Q20 |

---

## 4. Step 4 — Measuring Unsupported-Answer Rate

### What is an unsupported answer?
An answer that:
- Adds facts **not** present in the retrieved context, or
- Claims certainty when `answerable` should be false/partial, or
- Cites source IDs that were not retrieved

### Formula

```text
Unsupported-Answer Rate = (Number of unsupported answers / Total questions) × 100
```

### How to measure
1. For each of the 20 questions, retrieve context (Day 11 retriever)
2. Run Prompt v1 and/or v2
3. Mark each output as **Supported** or **Unsupported**
4. Calculate the rate
5. List top failure patterns (e.g. invented numbers, answering unanswerable questions)

### Target behaviour (Definition of Done)
- Unanswerable questions → `answerable: false`, no invented facts
- Source IDs map to real retrieved records only
- Unsupported-answer rate should drop from v1 → v2

### Example analysis table

| Metric | v1 | v2 |
|--------|----|----|
| Total questions | 20 | 20 |
| Unsupported answers | (fill) | (fill) |
| Unsupported rate | (fill)% | (fill)% |
| Unanswerable handled correctly | (fill)/6 | (fill)/6 |

### Top failure patterns to look for
1. Inventing numbers/timelines not in context
2. Answering unanswerable questions instead of refusing
3. Citing FAQ IDs that were never retrieved
4. Marking `answerable: true` when context is only partial

---

## 5. Definition of Done Checklist

- [x] RAG answer prompt written (v1)
- [x] Improved prompt written (v2)
- [x] 20 questions created (answerable / partial / unanswerable)
- [x] Unsupported-answer measurement method documented
- [x] Unanswerable questions instructed not to invent facts
- [x] Source IDs required and constrained to retrieved records

---

## 6. How to run a quick test

```bash
cd "Week 3/day11"
python retriever.py
```

Then manually (or with an LLM) fill context + question into `rag_prompt_v2.txt` and check the JSON output against the expected `answerable` type.
