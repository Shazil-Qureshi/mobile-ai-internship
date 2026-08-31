"""
Day 8 — Dynamic Prompt Template
Support Triage prompt parameterized with variables.
"""

# Default values (trusted)
DEFAULT_LOCALE = "en"
DEFAULT_CATEGORIES = ["account", "billing", "technical", "security", "other"]
DEFAULT_RESPONSE_LIMIT = 100
DEFAULT_PRIORITY_OPTIONS = ["low", "medium", "high"]


def build_dynamic_prompt(
    user_input: str,
    locale: str = DEFAULT_LOCALE,
    allowed_categories: list | None = None,
    response_limit: int = DEFAULT_RESPONSE_LIMIT,
) -> str:
    """
    Build a support-triage prompt using dynamic variables.

    Trusted variables (controlled by backend):
      - locale
      - allowed_categories
      - response_limit

    Untrusted variable (comes from user):
      - user_input
    """
    if allowed_categories is None:
        allowed_categories = DEFAULT_CATEGORIES

    categories_str = ", ".join(allowed_categories)

    prompt = f"""
You are a mobile-app customer support triage assistant.
Locale: {locale}

Task:
Classify the user's support message and determine the next action.

Allowed categories:
{categories_str}

Allowed priorities:
low, medium, high

Rules:
- Do not invent facts.
- If the message is too vague, use category "other" and set clarification_needed to true.
- Keep the "action" field under {response_limit} characters.
- Return valid JSON only. No markdown or extra text.

Required JSON schema:
{{
  "category": "one of the allowed categories",
  "priority": "low | medium | high",
  "action": "string (max {response_limit} chars)",
  "clarification_needed": true or false
}}

User message:
{user_input}
""".strip()

    return prompt
