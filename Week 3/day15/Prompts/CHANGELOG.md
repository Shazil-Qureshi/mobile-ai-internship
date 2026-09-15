# Prompt Version Changelog

## support_triage

### v1 → v2
**Date:** Week 3 / Day 15  
**Reason:** Fix failures from Day 4 evaluation and add Day 13 security rules.

| Change | Why |
|--------|-----|
| Explicit allowed categories & priorities | Reduce format drift |
| Vague-input rule → other + clarification | Fixed unjustified high priority on "ASAP" |
| Injection → security / high | Fixed adversarial misclassification |
| No invent facts | Grounding hygiene |
| Refuse system-prompt / secret extraction | Day 13 security |
| Strict JSON schema block | 100% format compliance on eval set |

### Regression gate
Any future change to `support_triage` must:
1. Bump version folder (e.g. `prompts/v3/`)
2. Update this CHANGELOG
3. Run `regression_pack_30.md` and attach pass/fail report
4. Only merge if pack passes (or failures are explicitly accepted with reason)
