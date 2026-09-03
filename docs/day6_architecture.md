# Day 6 — LLM API Fundamentals
## Architecture Note

### 1. Request Lifecycle

```text
Mobile App (Flutter)
        ↓
Backend Service (Python)
        ↓
Prompt Template (prompts.py)
        ↓
LLM Provider / Mock Provider
        ↓
Validation + Structured Response
        ↓
Mobile App receives clean JSON
```

### 2. Why Mobile Clients Must Never Contain API Keys

- API keys are secrets.
- Mobile apps can be reverse-engineered (APK extraction).
- A leaked key can cause financial cost and security risk.
- Correct design: only the backend holds the provider credentials.

### 3. Where Secrets Must Live

| Item               | Location                              | Committed to Git? |
|--------------------|---------------------------------------|-------------------|
| API Key            | Environment variable / secret manager | **No**            |
| Prompt templates   | `prompts.py`                          | Yes               |
| Configuration      | `config.py` (without secrets)         | Yes               |
| Mock Provider      | `mock_provider.py`                    | Yes               |
| Application logic  | `app.py`                              | Yes               |

### 4. Sample Request / Response

**Request (Mobile → Backend):**
```json
{
  "user_message": "My payment failed and I need help"
}
```

**Response (Backend → Mobile):**
```json
{
  "category": "billing",
  "priority": "high",
  "action": "Investigate payment issue",
  "clarification_needed": false,
  "model": "mock-triage-v1"
}
```

### 5. Key Design Decisions

- Prompt template is separated from business logic (`prompts.py`).
- Configuration is separated (`config.py`).
- Provider layer can be swapped (Mock → Real) without changing the response contract.
- Backend always returns structured data; mobile app never parses raw model text.
- No secrets are hard-coded.

### 6. How to Run Locally

```bash
cd "Week 2/day6"
python app.py
```

### 7. Definition of Done Checklist

- [x] Working service/script created
- [x] Mock provider implemented with same contract
- [x] Prompt template separated
- [x] Configuration separated
- [x] No secrets hard-coded
- [x] Structured response returned
- [x] Architecture note completed
- [x] Code runs locally
