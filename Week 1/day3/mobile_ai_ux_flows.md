# Day 3 — Mobile AI UX Mini User Flows

## 1. Chat
**User action:** User enters a message and taps Send.  
**App input:** User message.  
**Backend request:** Send the user message with required conversation context.  
**AI task:** Understand the request and generate a useful response.  
**Structured response:** `answer`, `confidence`, `needs_clarification`.

**UI states**
- Loading: progress indicator; prevent duplicate submission.
- Empty: show a start-conversation state.
- Error: controlled failure message.
- Retry: allow retry.
- Low confidence: indicate uncertainty and offer clarification.

**Fallback:** Invalid response → do not show raw model output; show safe error and retry/clarification.

## 2. Smart Search
**User action:** User enters a natural-language query and taps Search.  
**App input:** Search text and optional filters.  
**Backend request:** Send query and selected filters.  
**AI task:** Interpret search intent and identify relevant results.  
**Structured response:** `query`, `results[]`, `confidence`.

**UI states**
- Loading: search progress.
- Empty: no-results message and query refinement.
- Error: temporary search error.
- Retry: retry action.
- Low confidence: show results cautiously and suggest refining the query.

**Fallback:** Invalid response → controlled error instead of raw AI text.

## 3. Extraction
**User action:** User provides text/document and taps Extract.  
**App input:** User-provided content.  
**Backend request:** Send permitted input to extraction service.  
**AI task:** Extract required fields.  
**Structured response:** `fields`, `missing_fields`, `confidence`.

**UI states**
- Loading: extraction progress.
- Empty: request content.
- Error: extraction failure message.
- Retry: allow another attempt.
- Low confidence: highlight fields needing review.

**Fallback:** Invalid output → retry or manual entry; never display uncontrolled raw output.

## 4. Recommendation
**User action:** User describes what they need and requests recommendations.  
**App input:** Requirements, preferences, constraints.  
**Backend request:** Send structured requirements.  
**AI task:** Match requirements to suitable options.  
**Structured response:** `recommendations[]`, `confidence`.

**UI states**
- Loading: recommendation progress.
- Empty: request additional requirements or explain no suitable option was found.
- Error: temporary error.
- Retry: retry action.
- Low confidence: label suggestions as uncertain.

**Fallback:** Invalid response → controlled message and requirement refinement.

## 5. Assistant / Form Help
**User action:** User asks for help completing a form field.  
**App input:** Current field, question, and relevant permitted context.  
**Backend request:** Send only required context.  
**AI task:** Explain the field or guide the user.  
**Structured response:** `guidance`, `suggested_value`, `needs_clarification`, `confidence`.

**UI states**
- Loading: inline loading state.
- Empty: basic field instructions.
- Error: temporary failure message.
- Retry: request help again.
- Low confidence: ask a clarifying question instead of presenting an uncertain value as fact.

**Fallback:** Invalid/uncertain response → keep form usable and allow manual entry.
