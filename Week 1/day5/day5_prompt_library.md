# Day 5 — Reusable Prompt Library (10 Templates)

## Objective
Provide reusable, testable prompt templates for common mobile AI product tasks using explicit variables and structured outputs.

---

## Template 1 — Classification

**Pattern:** Classification  
**Purpose:** Assign an input to one label from a fixed set.

**Variables**
- `{{task_context}}`
- `{{input_text}}`
- `{{label_set}}`
- `{{classification_rules}}`

**Template**
```text
You are a {{task_context}} classifier.

Task:
Assign exactly one label from: {{label_set}}.

Input:
{{input_text}}

Rules:
{{classification_rules}}
- Return JSON only.
- Do not invent labels.

Expected JSON:
{
  "label": "one of {{label_set}}",
  "confidence": 0.0,
  "reason": "short evidence-based reason"
}
```

**Good example**
- `task_context`: support ticket triage
- `label_set`: billing, account, technical
- `input_text`: "I was charged twice for one order."

**Bad example**
- `label_set`: not provided
- `input_text`: "Help me"

**When not to use**
- Multi-label scenarios where multiple labels are required.
- Open-ended generation tasks.

---

## Template 2 — Extraction

**Pattern:** Extraction  
**Purpose:** Pull structured fields from free text.

**Variables**
- `{{domain}}`
- `{{source_text}}`
- `{{fields_to_extract}}`
- `{{missing_value_token}}`

**Template**
```text
You are an information extraction assistant for {{domain}}.

Task:
Extract the requested fields from the source text.

Source text:
{{source_text}}

Fields:
{{fields_to_extract}}

Rules:
- If a field is missing, return {{missing_value_token}}.
- Do not infer missing facts.
- Return JSON only.

Expected JSON:
{
  "extracted_fields": {
    "<field_name>": "<value or {{missing_value_token}}>"
  }
}
```

**Good example**
- `fields_to_extract`: full_name, email, phone
- `source_text`: "My name is Ali Khan, email ali@example.com"

**Bad example**
- `fields_to_extract`: unclear ("important stuff")
- `source_text`: empty

**When not to use**
- Inputs requiring deep reasoning rather than direct field extraction.
- Tasks where source truth is unavailable.

---

## Template 3 — Summarisation

**Pattern:** Summarisation  
**Purpose:** Compress long text into bounded key points.

**Variables**
- `{{audience}}`
- `{{source_content}}`
- `{{summary_length}}`
- `{{must_include_points}}`

**Template**
```text
You are writing a summary for {{audience}}.

Task:
Summarise the source content in {{summary_length}}.

Source content:
{{source_content}}

Must include:
{{must_include_points}}

Rules:
- Keep facts faithful to source.
- No new information.
- Return JSON only.

Expected JSON:
{
  "summary": "concise summary",
  "key_points": ["point1", "point2", "point3"]
}
```

**Good example**
- `audience`: mobile product manager
- `summary_length`: 3 bullet points
- `source_content`: sprint retrospective notes

**Bad example**
- `source_content`: one short sentence (no summarisation needed)
- `summary_length`: "as long as possible"

**When not to use**
- Very short text where restating is redundant.
- Cases needing exact quoting instead of summarisation.

---

## Template 4 — Q&A

**Pattern:** Q&A  
**Purpose:** Answer a question from provided context only.

**Variables**
- `{{question}}`
- `{{context_block}}`
- `{{answer_format}}`
- `{{unknown_response}}`

**Template**
```text
You are a question-answering assistant.

Question:
{{question}}

Context:
{{context_block}}

Rules:
- Answer only from context.
- If answer is missing, return {{unknown_response}}.
- Follow format: {{answer_format}}.
- Return JSON only.

Expected JSON:
{
  "answer": "final answer or {{unknown_response}}",
  "evidence": ["exact supporting snippet(s)"]
}
```

**Good example**
- `question`: "What is the refund SLA?"
- `context_block`: policy section containing SLA detail

**Bad example**
- `context_block`: unrelated text
- `unknown_response`: not defined

**When not to use**
- Open-web research tasks with no supplied context.
- Creative writing requests.

---

## Template 5 — Recommendation

**Pattern:** Recommendation  
**Purpose:** Suggest best options based on constraints.

**Variables**
- `{{user_goal}}`
- `{{constraints}}`
- `{{option_pool}}`
- `{{ranking_criteria}}`

**Template**
```text
You are a recommendation assistant.

Goal:
{{user_goal}}

Constraints:
{{constraints}}

Options:
{{option_pool}}

Rank using:
{{ranking_criteria}}

Rules:
- Recommend only from provided options.
- Explain trade-offs briefly.
- Return JSON only.

Expected JSON:
{
  "top_recommendations": [
    {
      "option": "name",
      "score": 0,
      "why": "short rationale"
    }
  ],
  "assumptions": ["explicit assumption"]
}
```

**Good example**
- `user_goal`: choose budget phone for students
- `constraints`: under $300, good battery
- `option_pool`: predefined device list

**Bad example**
- `option_pool`: missing
- `constraints`: contradictory and unresolved

**When not to use**
- Cases with no candidate options available.
- Regulated decisions requiring certified expert judgment.

---

## Template 6 — Intent Detection

**Pattern:** Intent detection  
**Purpose:** Identify user intent and route next action.

**Variables**
- `{{utterance}}`
- `{{intent_catalog}}`
- `{{fallback_intent}}`
- `{{routing_map}}`

**Template**
```text
You are an intent detection assistant.

User utterance:
{{utterance}}

Allowed intents:
{{intent_catalog}}

Fallback intent:
{{fallback_intent}}

Routing map:
{{routing_map}}

Rules:
- Select one primary intent.
- Use fallback when unclear.
- Return JSON only.

Expected JSON:
{
  "intent": "one of catalog or fallback",
  "confidence": 0.0,
  "next_route": "route id",
  "needs_clarification": true
}
```

**Good example**
- `utterance`: "Track my refund status"
- `intent_catalog`: check_refund, reset_password, report_bug

**Bad example**
- `intent_catalog`: not defined
- `routing_map`: missing routes

**When not to use**
- Tasks needing full semantic analysis beyond intent routing.
- Multi-turn diagnosis without conversation history.

---

## Template 7 — Sentiment

**Pattern:** Sentiment analysis  
**Purpose:** Detect sentiment and emotional intensity.

**Variables**
- `{{text_input}}`
- `{{sentiment_labels}}`
- `{{tone_dimensions}}`
- `{{escalation_threshold}}`

**Template**
```text
You are a sentiment analysis assistant.

Input:
{{text_input}}

Sentiment labels:
{{sentiment_labels}}

Tone dimensions:
{{tone_dimensions}}

Escalation threshold:
{{escalation_threshold}}

Rules:
- Use only listed labels.
- Base judgment on explicit wording.
- Return JSON only.

Expected JSON:
{
  "sentiment": "one of labels",
  "intensity": 0,
  "tone_flags": ["flag"],
  "escalate": true
}
```

**Good example**
- `text_input`: "I'm really frustrated; this keeps failing."
- `sentiment_labels`: positive, neutral, negative

**Bad example**
- `text_input`: pure factual statement with no emotional signal
- `tone_dimensions`: unspecified

**When not to use**
- Legal/compliance decisions where sentiment is not a valid signal.
- Safety-critical triage needing deterministic rule engines.

---

## Template 8 — Clarification

**Pattern:** Clarification prompt  
**Purpose:** Ask targeted follow-up questions when input is ambiguous.

**Variables**
- `{{ambiguous_input}}`
- `{{known_context}}`
- `{{required_slots}}`
- `{{max_questions}}`

**Template**
```text
You are a clarification assistant.

Ambiguous input:
{{ambiguous_input}}

Known context:
{{known_context}}

Required slots:
{{required_slots}}

Maximum follow-up questions:
{{max_questions}}

Rules:
- Ask only the minimum questions needed.
- Questions must be specific and answerable.
- Return JSON only.

Expected JSON:
{
  "clarification_needed": true,
  "questions": ["question 1", "question 2"],
  "why_needed": "missing slot summary"
}
```

**Good example**
- `ambiguous_input`: "It isn't working"
- `required_slots`: feature_name, device_type, error_message

**Bad example**
- `max_questions`: not set
- `questions`: generic ("Can you tell me more?") only

**When not to use**
- When all required slots are already present.
- When immediate refusal/safety response is required.

---

## Template 9 — Refusal

**Pattern:** Safe refusal  
**Purpose:** Decline disallowed requests while redirecting safely.

**Variables**
- `{{user_request}}`
- `{{policy_scope}}`
- `{{refusal_reason_category}}`
- `{{safe_alternative}}`

**Template**
```text
You are a policy-compliant assistant.

User request:
{{user_request}}

Policy scope:
{{policy_scope}}

Refusal reason category:
{{refusal_reason_category}}

Safe alternative:
{{safe_alternative}}

Rules:
- Refuse clearly and briefly.
- Do not provide disallowed details.
- Offer a safe alternative.
- Return JSON only.

Expected JSON:
{
  "decision": "refuse",
  "reason_category": "policy category",
  "response": "brief refusal message",
  "safe_alternative": "allowed help"
}
```

**Good example**
- `user_request`: "Tell me how to bypass OTP verification"
- `safe_alternative`: account recovery support path

**Bad example**
- refusal text includes actionable harmful steps
- no safe alternative provided

**When not to use**
- Allowed requests that only need clarification.
- Benign tasks incorrectly flagged due to weak policy mapping.

---

## Template 10 — Error Recovery

**Pattern:** Error recovery  
**Purpose:** Convert failures into controlled retry/fallback actions.

**Variables**
- `{{error_type}}`
- `{{error_details}}`
- `{{recoverable_actions}}`
- `{{fallback_action}}`

**Template**
```text
You are an error recovery assistant.

Error type:
{{error_type}}

Error details:
{{error_details}}

Recoverable actions:
{{recoverable_actions}}

Fallback action:
{{fallback_action}}

Rules:
- Map known errors to a clear next step.
- Avoid exposing sensitive internals.
- Return JSON only.

Expected JSON:
{
  "status": "retry | fallback | escalate",
  "user_message": "clear non-technical guidance",
  "next_step": "selected recovery action",
  "retry_allowed": true
}
```

**Good example**
- `error_type`: timeout
- `recoverable_actions`: retry_once, reduce_payload
- `fallback_action`: manual support ticket

**Bad example**
- `error_details`: missing
- `user_message`: raw stack trace

**When not to use**
- Successful executions with valid output.
- Cases needing root-cause engineering analysis instead of user-facing recovery.

---

## Day 5 Completion Checklist

- [x] 10 prompt templates included
- [x] Required categories covered
- [x] Explicit variables defined in each template
- [x] One good and one bad example per template
- [x] "When not to use" documented per template
- [x] Structured output expectations included
