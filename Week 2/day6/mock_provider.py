def generate(prompt: str) -> dict:
    """
    Mock LLM provider.
    Accepts a prompt string and returns a structured response.
    This can later be replaced with a real LLM provider
    without changing the response contract.
    """
    prompt_lower = prompt.lower()

    if "payment" in prompt_lower or "refund" in prompt_lower or "charged" in prompt_lower:
        return {
            "category": "billing",
            "priority": "high",
            "action": "Investigate payment issue",
            "clarification_needed": False
        }
    elif "login" in prompt_lower or "password" in prompt_lower or "account" in prompt_lower:
        return {
            "category": "account",
            "priority": "medium",
            "action": "Send password reset link",
            "clarification_needed": False
        }
    elif "crash" in prompt_lower or "error" in prompt_lower or "not working" in prompt_lower:
        return {
            "category": "technical",
            "priority": "high",
            "action": "Escalate to engineering team",
            "clarification_needed": False
        }
    else:
        return {
            "category": "other",
            "priority": "low",
            "action": "Request more details from user",
            "clarification_needed": True
        }
