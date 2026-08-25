#!/usr/bin/env python3
"""
Simple validator for Week 1 test vectors (tests/tests_week1.json).
Checks basic structure and expected value domains.
Exits with code 0 on success, 1 on failure.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEST_FILE = ROOT / "tests" / "tests_week1.json"

ALLOWED_CATEGORIES = {"account", "billing", "technical", "security", "other"}
ALLOWED_PRIORITIES = {"low", "medium", "high"}


def main():
    if not TEST_FILE.exists():
        print(f"ERROR: test file not found: {TEST_FILE}")
        sys.exit(1)

    data = json.loads(TEST_FILE.read_text(encoding="utf-8"))
    failures = []

    if not isinstance(data, list):
        print("ERROR: top-level JSON must be a list of test vectors")
        sys.exit(1)

    for i, t in enumerate(data):
        prefix = f"[{i}]"
        if not isinstance(t, dict):
            failures.append(f"{prefix} test vector must be an object")
            continue
        for field in ("id", "input", "expected_category", "expected_priority", "expected_clarification", "expected_action_hint"):
            if field not in t:
                failures.append(f"{prefix} missing required field: {field}")
        # field value checks
        cat = t.get("expected_category")
        if cat not in ALLOWED_CATEGORIES:
            failures.append(f"{prefix} expected_category '{cat}' not in allowed categories")
        pri = t.get("expected_priority")
        if pri not in ALLOWED_PRIORITIES:
            failures.append(f"{prefix} expected_priority '{pri}' not in allowed priorities")
        clar = t.get("expected_clarification")
        if not isinstance(clar, bool):
            failures.append(f"{prefix} expected_clarification must be boolean, got {type(clar).__name__}")
        action = t.get("expected_action_hint")
        if not isinstance(action, str) or len(action.strip()) == 0:
            failures.append(f"{prefix} expected_action_hint must be a non-empty string")

    if failures:
        print("Validation FAILED:\n")
        for f in failures:
            print(" - ", f)
        sys.exit(1)

    print("All Week 1 test vectors passed structural validation.")
    sys.exit(0)


if __name__ == '__main__':
    main()
