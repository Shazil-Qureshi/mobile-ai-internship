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
