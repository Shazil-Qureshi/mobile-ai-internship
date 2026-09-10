# Day 9 — Conversation & Context Design

## Objective
Handle multi-turn mobile conversations responsibly by managing history, detecting topic changes, and resolving conflicting information.

## 1. Conversation State Design

```text
ConversationManager
├── history[]          ← list of {role, content}
├── current_topic      ← billing | account | technical | chitchat | None
└── key_facts{}        ← small store of important values (order_id, etc.)
```

### What is sent to the model
- Recent full turns (last 3–4)
- Optional short summary of older turns
- Never the entire unlimited history

### What is discarded / summarised
- Turns older than the recent window
- Resolved conflicts (old wrong values)
- Pure chitchat once the real task starts

## 2. Context Budget Rules

| Rule                        | Value      | Purpose |
|-----------------------------|------------|---------|
| Max recent full turns       | 4          | Keep latest context accurate |
| Max history characters      | 1500       | Control token cost & latency |
| Older turns                 | Summarised | Preserve signal, drop noise |

See implementation: `Week 2/day9/context_budget.py`

## 3. Topic Change Handling

When the user clearly switches topic (e.g. from payment → login):

1. Update `current_topic`
2. Optionally clear old `key_facts` that belong to the previous topic
3. Let the context budget drop or summarise the old turns
4. Respond to the **latest** instruction

## 4. Conflict Handling

When new information contradicts earlier facts (e.g. different order IDs):

1. Do **not** silently overwrite
2. Ask a short confirmation question
3. After user confirms, keep only the correct value
4. Continue with the corrected state

## 5. Two Test Transcripts

See: `Week 2/day9/test_transcripts.md`

- **Transcript 1** — User changes topic mid-conversation
- **Transcript 2** — Earlier information conflicts with new information

## 6. Key Design Decisions

| Decision | Reason |
|----------|--------|
| History is intentionally limited | Prevents token explosion and confusion |
| Latest valid instruction wins | Mobile users often correct themselves |
| Conflicts trigger clarification | Avoids acting on wrong data |
| Topic change can reset facts | Prevents old context leaking into new task |

## 7. Definition of Done

- [x] Conversation-state design documented
- [x] Context budget rules implemented
- [x] 2 multi-turn test transcripts created
- [x] Topic-change behaviour defined
- [x] Conflict-handling behaviour defined
- [x] Latest valid user instruction is prioritised
- [x] History is managed (not endlessly appended)
