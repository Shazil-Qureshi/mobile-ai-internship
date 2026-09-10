# Day 9 — Multi-Turn Test Transcripts

## Transcript 1: User Changes Topic

**Goal:** Latest valid instruction should be followed; old topic should not dominate.

| Turn | Role      | Message |
|------|-----------|---------|
| 1    | User      | Hi, my payment failed yesterday for order 45821 |
| 2    | Assistant | I can help with the payment issue for order 45821. Could you share the error message you saw? |
| 3    | User      | Actually forget the payment. I can't log into my account now. |
| 4    | Assistant | Understood — switching to account login help. Have you tried resetting your password? |
| 5    | User      | Yes, but the reset email never arrives. |

**Expected behaviour**
- After turn 3 the system treats the active topic as **account**, not billing.
- Order 45821 fact can be kept or cleared (both acceptable if documented).
- Latest user instruction (“can’t log in”) is the priority.

**Context budget note**
- Turns 1–2 may be summarised or dropped once the topic changes.
- Only the most recent 3–4 turns need full detail.

---

## Transcript 2: Conflicting Information

**Goal:** System should notice conflict and ask for clarification instead of guessing.

| Turn | Role      | Message |
|------|-----------|---------|
| 1    | User      | Please refund order 45821. I was charged twice. |
| 2    | Assistant | Got it. I’ll look into a refund for order 45821 due to a duplicate charge. |
| 3    | User      | Wait — the order number is actually 45999, not 45821. |
| 4    | Assistant | Thanks for the correction. Just to confirm: should I process the refund for order **45999** (and ignore 45821)? |
| 5    | User      | Yes, 45999 is correct. |

**Expected behaviour**
- System detects conflict between order 45821 and 45999.
- It does **not** silently overwrite and continue.
- It asks a short confirmation question (turn 4).
- After confirmation, only the latest correct value is used.

**Context budget note**
- Both order numbers appear in recent history, so the model can see the conflict.
- After resolution, older wrong value can be dropped from active facts.

---

## Summary of Rules Demonstrated

1. **Latest valid user instruction wins**
2. **Topic change is detected** and history is adjusted
3. **Conflicts are surfaced** with a clarification question
4. **History is not endlessly appended** — context budget is applied
