"""
Day 6 — LLM API Fundamentals
Main application service.

Flow:
  User input → Prompt template → Provider (Mock or Real) → Structured response
"""

from mock_provider import generate
from prompts import build_support_triage_prompt
from config import USE_MOCK, MODEL_NAME


def process_request(user_message: str) -> dict:
    """
    Main entry point.
    Accepts user text, builds prompt, calls provider, returns structured response.
    """
    if not user_message or not user_message.strip():
        return {
            "category": "other",
            "priority": "low",
            "action": "Request a valid message from the user",
            "clarification_needed": True,
            "model": MODEL_NAME,
            "error": "empty_input"
        }

    # 1. Build prompt from template
    prompt = build_support_triage_prompt(user_message)

    # 2. Call provider (mock for now)
    if USE_MOCK:
        result = generate(prompt)
    else:
        # Placeholder for real provider integration
        raise NotImplementedError("Real LLM provider is not connected yet. Set USE_MOCK = True.")

    # 3. Attach metadata
    result["model"] = MODEL_NAME

    return result


if __name__ == "__main__":
    # Simple local tests
    test_cases = [
        "My payment failed and I need help",
        "I can't log into my account",
        "The app crashes on the transactions page",
        "It isn't working",
        ""
    ]

    for i, text in enumerate(test_cases, 1):
        print(f"\n--- Test {i} ---")
        print("Input :", text if text else "(empty)")
        print("Output:", process_request(text))
