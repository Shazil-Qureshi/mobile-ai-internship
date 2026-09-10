# Configuration settings for Day 6 LLM service
# Secrets (API keys) must NEVER be stored here or committed to Git.
# Use environment variables for real credentials.

USE_MOCK = True              # Set to False when connecting a real LLM provider
MODEL_NAME = "mock-triage-v1"
MAX_RETRIES = 2
REQUEST_TIMEOUT_SECONDS = 15
