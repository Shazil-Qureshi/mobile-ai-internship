"""
Day 9 — Context Budget Rules
Controls how much conversation history is sent to the model.
"""

# Maximum number of recent turns to keep in full detail
MAX_RECENT_TURNS = 4

# Maximum total characters allowed for history
MAX_HISTORY_CHARS = 1500

# Older turns beyond MAX_RECENT_TURNS are summarised into one short string
SUMMARY_MAX_CHARS = 200


def apply_context_budget(history: list[dict]) -> list[dict]:
    """
    history item format:
      {"role": "user" | "assistant", "content": str}

    Returns a reduced history that respects the budget.
    """
    if not history:
        return []

    # Keep the most recent turns fully
    recent = history[-MAX_RECENT_TURNS:]
    older = history[:-MAX_RECENT_TURNS] if len(history) > MAX_RECENT_TURNS else []

    result = []

    # Summarise older turns if any
    if older:
        summary_text = _summarise_turns(older)
        result.append({
            "role": "system",
            "content": f"[Earlier conversation summary]: {summary_text}"
        })

    result.extend(recent)

    # Final character budget check
    total_chars = sum(len(t["content"]) for t in result)
    while total_chars > MAX_HISTORY_CHARS and len(result) > 1:
        # Drop the oldest non-summary item
        result.pop(0)
        total_chars = sum(len(t["content"]) for t in result)

    return result


def _summarise_turns(turns: list[dict]) -> str:
    """Very simple extractive summary for older turns."""
    parts = []
    for t in turns:
        role = t.get("role", "user")
        content = t.get("content", "")[:80]
        parts.append(f"{role}: {content}")
    summary = " | ".join(parts)
    return summary[:SUMMARY_MAX_CHARS]
