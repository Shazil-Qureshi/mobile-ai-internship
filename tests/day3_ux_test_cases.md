# Day 3 — Mobile AI UX Test Cases

## 1. Objective

Test mobile AI interaction patterns to ensure that AI-powered features provide clear, reliable, and safe user experiences.

Testing focuses on:
- Loading states
- Empty states
- Error states
- Retry behaviour
- Low-confidence responses
- Clear AI output presentation
- Safe fallback behaviour
- Confirmation before destructive actions

## 2. Use Cases

1. Chat
2. Smart Search
3. Extraction
4. Recommendation
5. Assistant / Form Help

## 3. Common AI Interaction Flow

```text
User Action
    ↓
Mobile App Input
    ↓
Backend Request
    ↓
AI Task
    ↓
Structured AI Response
    ↓
Response Validation
    ↓
UI State
    ↓
User Action / Next Step
```

The application should not display uncontrolled raw model output directly to the user.

## 4. Required UX States

### Loading
- Show a loading indicator.
- Keep the user informed.
- Do not display incomplete AI output.

### Empty
- Explain what is missing.
- Provide a useful next action.
- Do not show an unexplained blank screen.

### Error
- Show a clear error message.
- Do not expose raw technical errors.
- Provide Retry where appropriate.

Example:
```text
Something went wrong.

Please try again.
[Retry]
```

### Retry
```text
Request failed
     ↓
Show error
     ↓
User selects Retry
     ↓
Request is sent again
     ↓
Loading state
     ↓
Success or Error
```

### Low Confidence
- Clearly communicate uncertainty.
- Ask for clarification when necessary.
- Do not invent missing information.

Example:
```text
I'm not sure what you mean.

Could you provide more details?
```

## 5. Fallback Principle

If an AI response is invalid, incomplete, empty, unclear, low-confidence, or unavailable, the application should not render uncontrolled raw model text.

Possible fallbacks:
- Retry
- Clarification
- Manual entry
- Alternative search
- User confirmation

# 6. UX Test Cases

## TC01 — Chat Loading State

**Input:** `What is artificial intelligence?`

**Expected Behaviour:**
- Message is submitted.
- Loading indicator appears.
- Incomplete AI output is not shown.
- Final response appears after processing.

**Status:** PASS

## TC02 — Chat Empty Input

**Input:** Blank message.

**Expected Behaviour:**
- Empty request is not sent.
- User is informed that a message is required.
- Input remains available.

**Status:** PASS

## TC03 — Chat Error State

**Input:** `Explain machine learning.`

**Expected Behaviour:**
- Controlled error message is displayed.
- Raw backend/model errors are not displayed.
- Retry is available.

**Status:** PASS

## TC04 — Chat Retry

**Scenario:** First AI request fails and the user selects Retry.

**Expected Behaviour:**
```text
Error → Retry → Loading → AI Response
```

**Status:** PASS

## TC05 — Smart Search Loading

**Input:** `Find laptops suitable for programming.`

**Expected Behaviour:**
- Search starts.
- Loading state is displayed.
- Results appear after processing.

**Status:** PASS

## TC06 — Smart Search Empty Results

**Input:** `Find something that does not exist.`

**Expected Behaviour:**
- Empty state is displayed.
- User receives guidance to change the search.
- Blank/confusing result screen is avoided.

**Status:** PASS

## TC07 — Extraction Success

**Input:** `My name is Ali and my email is ali@example.com.`

**Expected Behaviour:**
```text
Name: Ali
Email: ali@example.com
```

Information is displayed in structured fields.

**Status:** PASS

## TC08 — Extraction Missing Information

**Input:** `My name is Ali.`

**Expected Behaviour:**
```text
Name: Ali
Email: Not provided
```

Missing information must not be invented.

**Status:** PASS

## TC09 — Recommendation Success

**Input:** `I need a laptop for programming and university work.`

**Expected Behaviour:**
- Relevant requirements are identified.
- Recommendations are clearly displayed.
- Unsupported assumptions are avoided.

**Status:** PASS

## TC10 — Recommendation Low Confidence

**Input:** `I need something good.`

**Expected Behaviour:**
- Do not make an overly specific recommendation.
- Ask for clarification.

Example:
```text
I'd like to help.

What will you mainly use it for?
```

**Status:** PASS

## TC11 — Assistant / Form Help

**Input:** `Help me fill out this form.`

**Expected Behaviour:**
- Explain required information.
- Ask for missing information.
- Present extracted information clearly.
- Do not submit anything without appropriate user confirmation.

**Status:** PASS

## TC12 — Invalid AI Response

**Scenario:** Backend returns an invalid or incomplete AI response.

**Expected Behaviour:**
- Response is validated.
- Invalid structure is rejected.
- Raw output is not displayed.
- Controlled fallback is shown.

**Status:** PASS

## TC13 — Network / Backend Failure

**Scenario:** AI service is unavailable.

**Expected Behaviour:**
- User-friendly error is shown.
- Technical details are hidden.
- Retry is available where appropriate.
- User input is preserved where possible.

**Status:** PASS

## TC14 — Confirmation Before Destructive Action

**Scenario:** AI suggests an action that could remove or permanently change user data.

**Expected Behaviour:**
- Action is not performed immediately.
- User confirmation is required.

Example:
```text
Are you sure you want to delete this item?

[Cancel] [Confirm]
```

**Status:** PASS

## TC15 — Clear AI Output Presentation

**Scenario:** AI returns a long response.

**Expected Behaviour:**
- Use headings, lists, short paragraphs, and structured fields.
- Keep actions clear.
- Avoid displaying an unreadable block of raw model output.

**Status:** PASS

# 7. Test Result Summary

| Test Case | Scenario | Expected Result | Status |
|---|---|---|---|
| TC01 | Chat loading | Loading state displayed | PASS |
| TC02 | Chat empty input | Empty input handled safely | PASS |
| TC03 | Chat error | Controlled error shown | PASS |
| TC04 | Chat retry | Request can be retried | PASS |
| TC05 | Smart Search loading | Loading state displayed | PASS |
| TC06 | Smart Search empty results | Empty state displayed | PASS |
| TC07 | Extraction success | Structured fields displayed | PASS |
| TC08 | Missing extraction data | Missing data not invented | PASS |
| TC09 | Recommendation success | Requirements and result displayed | PASS |
| TC10 | Low-confidence recommendation | Clarification requested | PASS |
| TC11 | Form help | Controlled assistance provided | PASS |
| TC12 | Invalid AI response | Invalid response rejected | PASS |
| TC13 | Backend failure | Safe fallback displayed | PASS |
| TC14 | Destructive action | Confirmation required | PASS |
| TC15 | Long AI output | Readable mobile presentation | PASS |

# 8. UX Validation Checklist

## Loading
- [x] Loading state exists.
- [x] User understands processing is in progress.
- [x] Incomplete AI output is not displayed.

## Empty
- [x] Empty input is handled.
- [x] Empty results have an explanation.
- [x] User receives a useful next action.

## Error
- [x] AI failures have a controlled error state.
- [x] Raw technical errors are not displayed.
- [x] Retry is available where appropriate.

## Low Confidence
- [x] Uncertain AI output is not presented as fact.
- [x] Clarification can be requested.
- [x] Missing information is not invented.

## Safety
- [x] Destructive actions require confirmation.
- [x] AI output is validated before rendering.
- [x] Invalid responses have controlled fallback behaviour.

## Presentation
- [x] AI output is structured.
- [x] Long responses remain readable.
- [x] Actions are clear.
- [x] Mobile users can understand results quickly.

# 9. Acceptance Criteria

- [x] Five AI mobile use cases are documented.
- [x] Loading behaviour is defined.
- [x] Empty behaviour is defined.
- [x] Error behaviour is defined.
- [x] Retry behaviour is defined.
- [x] Low-confidence behaviour is defined.
- [x] Fallback behaviour is defined.
- [x] Destructive actions require confirmation.
- [x] At least 10 UX test cases are documented.
- [x] Test results are recorded.
- [x] AI output is presented in a structured and readable manner.

# 10. Final Result

Day 3 demonstrates how AI capabilities can be converted into clear, reliable, and safe mobile interactions.

The key design principle is:

```text
AI Model
   ↓
Structured Response
   ↓
Response Validation
   ↓
UI State
   ↓
User Action
```

AI output should never be treated as automatically valid.

The mobile application should validate AI responses and provide controlled fallback behaviour for loading, empty, error, retry, and low-confidence states.

The completed UX patterns help ensure that AI features remain understandable, predictable, and safe for mobile users.
