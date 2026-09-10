# Day 3 — AI-to-UI Response Contracts

## 1. Chat
| Field | Type | Allowed / Expected |
|---|---|---|
| answer | string | Validated response text |
| confidence | string | high, medium, low |
| needs_clarification | boolean | true or false |

**UI rule:** Never render an unvalidated raw model response.

## 2. Smart Search
| Field | Type | Allowed / Expected |
|---|---|---|
| query | string | Interpreted search query |
| results | array | Zero or more validated result objects |
| results[].id | string | Application result identifier |
| results[].title | string | Display title |
| results[].reason | string | Short explanation |
| confidence | string | high, medium, low |

**UI rule:** Empty results require an intentional empty state.

## 3. Extraction
| Field | Type | Allowed / Expected |
|---|---|---|
| fields | object | Extracted field/value pairs |
| missing_fields | array | Field names still required |
| confidence | string | high, medium, low |

**UI rule:** Low-confidence fields require user review.

## 4. Recommendation
| Field | Type | Allowed / Expected |
|---|---|---|
| recommendations | array | Zero or more validated recommendations |
| recommendations[].id | string | Application item identifier |
| recommendations[].title | string | Display title |
| recommendations[].reason | string | Recommendation reason |
| confidence | string | high, medium, low |

**UI rule:** Recommendations are suggestions, not guaranteed facts.

## 5. Assistant / Form Help
| Field | Type | Allowed / Expected |
|---|---|---|
| guidance | string | User-facing guidance |
| suggested_value | string or null | Optional suggestion |
| needs_clarification | boolean | true or false |
| confidence | string | high, medium, low |

**UI rule:** Low-confidence guidance should request clarification rather than silently filling a form.

## Common Failure Contract
```json
{
  "status": "error",
  "message": "We couldn't process that request. Please try again.",
  "retry_available": true
}
```

The UI should never depend on displaying uncontrolled raw model text.
