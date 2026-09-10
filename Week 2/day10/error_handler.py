"""
Day 10 — Error handling + limited retry logic
Example implementation for the triage service.
"""

import time
from enum import Enum
from typing import Callable, Any


class ErrorType(str, Enum):
    TIMEOUT = "timeout"
    RATE_LIMIT = "rate_limit"
    INVALID_JSON = "invalid_json"
    EMPTY_RESPONSE = "empty_response"
    PROVIDER_ERROR = "provider_error"
    INVALID_INPUT = "invalid_input"
    NETWORK_ERROR = "network_error"
    UNKNOWN = "unknown"


# User-facing messages (mobile)
USER_MESSAGES = {
    ErrorType.TIMEOUT: "Something went wrong on our side. Please try again.",
    ErrorType.RATE_LIMIT: "Too many requests. Please wait a moment and try again.",
    ErrorType.INVALID_JSON: "We couldn’t process the response. Please try again.",
    ErrorType.EMPTY_RESPONSE: "We couldn’t process the response. Please try again.",
    ErrorType.PROVIDER_ERROR: "Service temporarily unavailable. Please try again.",
    ErrorType.INVALID_INPUT: "Please describe your issue so we can help.",
    ErrorType.NETWORK_ERROR: "Network error. Please check your connection.",
    ErrorType.UNKNOWN: "Something went wrong. Please try again.",
}

# Only these are retryable
RETRYABLE = {
    ErrorType.TIMEOUT,
    ErrorType.RATE_LIMIT,
    ErrorType.PROVIDER_ERROR,
    ErrorType.NETWORK_ERROR,
}

MAX_RETRIES = 2
RETRY_DELAY_SECONDS = 1.5


def build_error_response(error_type: ErrorType) -> dict:
    return {
        "success": False,
        "error_type": error_type.value,
        "message": USER_MESSAGES[error_type],
        "retryable": error_type in RETRYABLE,
    }


def validate_input(user_message: str) -> dict | None:
    """Return an error response if input is invalid, else None."""
    if user_message is None or not str(user_message).strip():
        return build_error_response(ErrorType.INVALID_INPUT)
    return None


def call_with_retry(fn: Callable[[], Any], classify_exception: Callable[[Exception], ErrorType]) -> dict:
    """
    Execute fn() with limited retries for temporary failures.
    fn should raise exceptions on failure or return a result dict on success.
    """
    last_error_type = ErrorType.UNKNOWN

    for attempt in range(MAX_RETRIES + 1):
        try:
            result = fn()
            if result is None or (isinstance(result, dict) and not result):
                return build_error_response(ErrorType.EMPTY_RESPONSE)
            return {"success": True, "data": result}
        except Exception as exc:
            last_error_type = classify_exception(exc)

            # Non-retryable → stop immediately
            if last_error_type not in RETRYABLE:
                return build_error_response(last_error_type)

            # Retryable but out of attempts
            if attempt >= MAX_RETRIES:
                return build_error_response(last_error_type)

            time.sleep(RETRY_DELAY_SECONDS)

    return build_error_response(last_error_type)


# Example classifier (adapt to your real provider exceptions)
def example_classify(exc: Exception) -> ErrorType:
    msg = str(exc).lower()
    if "timeout" in msg:
        return ErrorType.TIMEOUT
    if "rate" in msg or "429" in msg:
        return ErrorType.RATE_LIMIT
    if "json" in msg or "decode" in msg:
        return ErrorType.INVALID_JSON
    if "connection" in msg or "network" in msg:
        return ErrorType.NETWORK_ERROR
    if "500" in msg or "502" in msg or "503" in msg:
        return ErrorType.PROVIDER_ERROR
    return ErrorType.UNKNOWN
