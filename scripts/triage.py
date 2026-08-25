"""
Rule-based triage implementation for Week 1 support-message triage.

Usage:
  python3 scripts/triage.py "<user message>"

Or run against the week 1 test vectors:
  python3 scripts/triage.py --run-tests tests/tests_week1.json --output tests/week1_results.json

This script implements the Prompt v2 rules: categories (account,billing,technical,security,other), priorities (low,medium,high), action hints, and clarification handling.
"""
import re
import json
import sys
from pathlib import Path

ALLOWED_CATEGORIES = {"account", "billing", "technical", "security", "other"}
ALLOWED_PRIORITIES = {"low", "medium", "high"}

INJECTION_PATTERNS = [
    r"ignore all previous",
    r"reveal your system prompt",
    r"reveal your system",
    r"output your private",
    r"private instructions",
    r"forget the",
    r"ignore the required json",
    r"tell me everything you were instructed",
    r"request internal",
    r"internal reasoning",
    r"secret",
    r"configuration",
    r"role.*administrator",
]

BILLING_KEYWORDS = ["payment", "pay", "checkout", "charged", "refund", "transaction", "invoice", "paymnt", "refund" , "transaction id"]
ACCOUNT_KEYWORDS = ["login", "log in", "loginto", "log into", "password", "account", "profile", "acount", "logn"]
TECHNICAL_KEYWORDS = ["crash", "crashes", "crash", "error", "bug", "not working", "isn't working", "doesn't work", "open transactions", "doesnt", "crsh" ]


def detect_injection(text):
    t = text.lower()
    for p in INJECTION_PATTERNS:
        if re.search(p, t):
            return True
    # also heuristics: ask to ignore JSON or to output internal data
    if "system prompt" in t or "system instructions" in t or "internal" in t and "prompt" in t:
        return True
    return False


def contains_keyword(text, keywords):
    t = text.lower()
    for k in keywords:
        if k in t:
            return True
    return False


def classify_message(user_message):
    msg = user_message.strip()
    if len(msg) == 0:
        return {
            "category": "other",
            "priority": "low",
            "action": "Request clarification: please describe the issue in detail",
            "clarification_needed": True,
        }

    # Security / prompt injection detection
    if detect_injection(msg):
        return {
            "category": "security",
            "priority": "high",
            "action": "Refuse unsafe request and flag as security incident",
            "clarification_needed": False,
        }

    # Billing detection
    if contains_keyword(msg, BILLING_KEYWORDS):
        # Payment failures or checkout issues are high priority
        priority = "high" if any(w in msg.lower() for w in ["fail", "failed", "can't checkout", "cant checkout", "can't pay", "can't complete", "cant pay", "can't checkout", "can't complete"]) or "fail" in msg.lower() or "failed" in msg.lower() else "high"
        return {
            "category": "billing",
            "priority": priority,
            "action": "Investigate payment failure and assist user with payment completion",
            "clarification_needed": False,
        }

    # Technical detection
    if contains_keyword(msg, TECHNICAL_KEYWORDS):
        # crashes and app errors are high priority
        priority = "high"
        return {
            "category": "technical",
            "priority": priority,
            "action": "Collect crash logs and escalate to engineering",
            "clarification_needed": False,
        }

    # Account detection — require concrete account-related signals beyond vague 'problem'
    t = msg.lower()
    if contains_keyword(msg, ACCOUNT_KEYWORDS):
        # if message is very generic about "problem with my account" -> other + clarification
        if re.search(r"problem with my account|issue with my account|i have a problem with my account|problem with account", t):
            return {
                "category": "other",
                "priority": "low",
                "action": "Ask user to describe the account issue and provide examples or screenshots",
                "clarification_needed": True,
            }
        # otherwise treat as account issue
        priority = "medium"
        # escalate to high if contains lockout words
        if any(w in t for w in ["locked", "lockout", "locked out", "cannot access", "can't access", "cant access"]):
            priority = "high"
        return {
            "category": "account",
            "priority": priority,
            "action": "Provide account recovery steps (password reset) and verify account status",
            "clarification_needed": False,
        }

    # Vague or other
    # If contains general urgency words but no specifics -> other + clarification, low priority
    if re.search(r"please fix|fix this asap|asap|urgent|please help", t):
        return {
            "category": "other",
            "priority": "low",
            "action": "Request specific details; do not escalate based on urgency words alone",
            "clarification_needed": True,
        }

    # Fallback
    return {
        "category": "other",
        "priority": "low",
        "action": "Request clarification: please describe the issue in detail",
        "clarification_needed": True,
    }


def run_tests(input_path, output_path=None):
    p = Path(input_path)
    if not p.exists():
        print(f"Test vectors not found: {input_path}")
        return 1
    vectors = json.loads(p.read_text(encoding="utf-8"))
    results = []
    for v in vectors:
        out = classify_message(v.get("input", ""))
        results.append({"id": v.get("id"), "input": v.get("input"), **out})
    if output_path:
        Path(output_path).write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Wrote results to {output_path}")
    else:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('message', nargs='?', help='Optional single message to classify')
    parser.add_argument('--run-tests', help='Path to JSON test vectors')
    parser.add_argument('--output', help='Output path for test results JSON')
    args = parser.parse_args()

    if args.run_tests:
        sys.exit(run_tests(args.run_tests, args.output))
    if args.message:
        print(json.dumps(classify_message(args.message), indent=2))
        sys.exit(0)
    parser.print_help()
