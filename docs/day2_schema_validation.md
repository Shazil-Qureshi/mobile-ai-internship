# Day 2 — Schema & Validation Notes

## Objective
Make LLM output usable by application code through strict JSON structure, required keys, correct data types, allowed values, and safe handling of invalid or ambiguous input.

## Schemas

### 1. Support Triage
Required keys:
- `category`
- `priority`
- `action`
- `clarification_needed`

Allowed category values:
`account`, `billing`, `technical`, `security`, `other`

Allowed priority values:
`low`, `medium`, `high`

### 2. Expense Categorisation
Required keys:
- `category`
- `amount`
- `currency`
- `description`
- `confidence`

Allowed category values:
`food`, `transport`, `shopping`, `bills`, `entertainment`, `healthcare`, `education`, `other`

Allowed confidence values:
`low`, `medium`, `high`

### 3. Product Recommendation
Required keys:
- `product_type`
- `use_cases`
- `budget`
- `currency`
- `portability_preference`
- `performance_preference`
- `additional_requirements`

### 4. Form Extraction
Required keys:
- `name`
- `email`
- `phone`
- `address`
- `education`
- `experience`

## Validation Rules

1. Response must be valid JSON.
2. Required keys must exist.
3. Values must have the expected data types.
4. Enum fields must contain only allowed values.
5. Missing information must use `null` where specified.
6. Lists must remain arrays.
7. Unexpected prose outside the JSON object is a format failure.
8. Ambiguous input must produce a defined safe response rather than invented facts.
9. Invalid output must be rejected before application business logic consumes it.

## Safe Failure Behaviour

If JSON parsing fails, the application should reject the response and use a deterministic fallback such as:
`Unable to process the request. Please try again.`

If required fields are missing or have invalid values, the response should be treated as invalid and sent through the same fallback path.

## Pseudocode

```text
parse response as JSON
if parsing fails:
    return validation_failure

check all required keys
if any required key is missing:
    return validation_failure

check data types
if any type is invalid:
    return validation_failure

check allowed enum values
if any enum value is invalid:
    return validation_failure

return valid_response
```

## Day 2 Acceptance Criteria

- Four prompt templates exist.
- At least 20 tests are recorded.
- Normal cases achieve at least 90% required-structure compliance.
- Invalid and ambiguous inputs have defined safe behaviour.
