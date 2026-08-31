"""
Day 8 — Server-side validation and defaults for prompt variables.
"""

from prompts.dynamic_triage_prompt import (
    DEFAULT_LOCALE,
    DEFAULT_CATEGORIES,
    DEFAULT_RESPONSE_LIMIT,
)


ALLOWED_LOCALES = {"en", "ur", "hi", "ar"}
MAX_USER_INPUT_LENGTH = 1000
MAX_RESPONSE_LIMIT = 300
MIN_RESPONSE_LIMIT = 20


def validate_and_normalize(
    user_input: str,
    locale: str | None = None,
    allowed_categories: list | None = None,
    response_limit: int | None = None,
) -> dict:
    """
    Validate incoming variables and apply safe defaults.
    Returns a clean dictionary ready for prompt building.
    """
    errors = []

    # --- user_input (UNTRUSTED) ---
    if user_input is None:
        user_input = ""
    user_input = str(user_input).strip()

    if len(user_input) == 0:
        errors.append("user_input is empty")
    elif len(user_input) > MAX_USER_INPUT_LENGTH:
        user_input = user_input[:MAX_USER_INPUT_LENGTH]
        errors.append(f"user_input truncated to {MAX_USER_INPUT_LENGTH} chars")

    # Prevent user from injecting schema-breaking instructions
    # (basic safeguard — real systems use stronger filtering)
    dangerous_patterns = [
        "ignore previous",
        "ignore all instructions",
        "system prompt",
        "reveal your prompt",
    ]
    lower_input = user_input.lower()
    for pattern in dangerous_patterns:
        if pattern in lower_input:
            errors.append(f"potentially adversarial input detected: '{pattern}'")
            break

    # --- locale (TRUSTED) ---
    if not locale or locale not in ALLOWED_LOCALES:
        locale = DEFAULT_LOCALE

    # --- allowed_categories (TRUSTED) ---
    if not allowed_categories or not isinstance(allowed_categories, list):
        allowed_categories = DEFAULT_CATEGORIES.copy()
    else:
        # Only keep non-empty strings
        allowed_categories = [str(c).strip() for c in allowed_categories if str(c).strip()]
        if not allowed_categories:
            allowed_categories = DEFAULT_CATEGORIES.copy()

    # --- response_limit (TRUSTED) ---
    if response_limit is None:
        response_limit = DEFAULT_RESPONSE_LIMIT
    try:
        response_limit = int(response_limit)
    except (TypeError, ValueError):
        response_limit = DEFAULT_RESPONSE_LIMIT

    if response_limit < MIN_RESPONSE_LIMIT:
        response_limit = MIN_RESPONSE_LIMIT
    elif response_limit > MAX_RESPONSE_LIMIT:
        response_limit = MAX_RESPONSE_LIMIT

    return {
        "user_input": user_input,
        "locale": locale,
        "allowed_categories": allowed_categories,
        "response_limit": response_limit,
        "errors": errors,
        "is_valid": len(user_input) > 0,
    }
