# Day 15 — Regression Suite & Prompt Versioning

## Objective
Protect quality as prompts evolve: version prompts, keep a 30+ regression pack, and require pass evidence before merge.

---

## Short explanation

| Idea | Meaning |
|------|---------|
| **Versioned prompts** | Store each revision in `prompts/v1`, `prompts/v2`, … never overwrite silently |
| **Changelog** | Record why the prompt changed |
| **Regression pack** | Fixed 30+ cases (normal, edge, multilingual, adversarial) |
| **Gate** | No prompt merge without a filled pass/fail report |

---

## Deliverables

```text
Week 3/day15/
├── prompts/
│   ├── v1/support_triage.txt
│   ├── v2/support_triage.txt
│   └── CHANGELOG.md
├── regression_pack_30.md
├── pass_fail_report.md
└── day15_regression_versioning.md

docs/
└── day15_regression_versioning.md
```

---

## Process (before any prompt change)

1. Copy current prompt to a new folder `prompts/vN/`  
2. Edit only the new version  
3. Update `CHANGELOG.md`  
4. Run all cases in `regression_pack_30.md`  
5. Fill `pass_fail_report.md`  
6. Merge only if gate = PASS (or documented waivers)

---

## Definition of Done

- [x] Versioned prompt directory (v1 + v2)  
- [x] Changelog with v1→v2 diff narrative  
- [x] Regression pack of 30+ cases  
- [x] Pass/fail report template  
- [x] Rule documented: changed prompt needs regression evidence  

---

## Suggested commit

```text
feat(day15): versioned prompts, 32-case regression pack, pass/fail gate template
```
