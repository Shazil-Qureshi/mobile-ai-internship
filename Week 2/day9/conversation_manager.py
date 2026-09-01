"""
Day 9 — Conversation State Manager
Handles multi-turn dialogue, topic changes, and conflicting information.
"""

from context_budget import apply_context_budget


class ConversationManager:
    def __init__(self):
        self.history: list[dict] = []
        self.current_topic: str | None = None
        self.key_facts: dict = {}  # simple store for important facts

    def add_user_message(self, text: str) -> None:
        self.history.append({"role": "user", "content": text})
        self._detect_topic_change(text)
        self._extract_simple_facts(text)

    def add_assistant_message(self, text: str) -> None:
        self.history.append({"role": "assistant", "content": text})

    def get_context_for_model(self) -> list[dict]:
        """Return history after applying context budget."""
        return apply_context_budget(self.history)

    def _detect_topic_change(self, text: str) -> None:
        """Very simple topic detection for demo purposes."""
        lower = text.lower()
        new_topic = None

        if any(w in lower for w in ["payment", "refund", "charged", "bill"]):
            new_topic = "billing"
        elif any(w in lower for w in ["login", "password", "account"]):
            new_topic = "account"
        elif any(w in lower for w in ["crash", "error", "bug", "not working"]):
            new_topic = "technical"
        elif any(w in lower for w in ["hello", "hi", "thanks", "bye"]):
            new_topic = "chitchat"

        if new_topic and new_topic != self.current_topic:
            if self.current_topic is not None:
                # Topic changed — we can optionally clear old facts
                self.key_facts = {}
            self.current_topic = new_topic

    def _extract_simple_facts(self, text: str) -> None:
        """Store a few key facts (demo only)."""
        lower = text.lower()
        if "order" in lower and any(c.isdigit() for c in text):
            # naive order id capture
            for word in text.split():
                if word.isdigit() and len(word) >= 4:
                    self.key_facts["order_id"] = word
        if "refund" in lower:
            self.key_facts["wants_refund"] = True

    def handle_conflict(self, new_info: str) -> str:
        """
        Called when new user info conflicts with earlier facts.
        Returns a short clarification message.
        """
        return (
            "I noticed this might conflict with earlier information. "
            "Could you confirm which details are correct?"
        )

    def reset(self) -> None:
        self.history = []
        self.current_topic = None
        self.key_facts = {}
