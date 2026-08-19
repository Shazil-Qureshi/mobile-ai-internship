# Day 1 — Prompt Engineering Fundamentals

## 1. System, Developer and User Instructions
- System instruction: establishes high-level behaviour and boundaries for the AI.
- Developer instruction: defines application-level requirements and constraints.
- User instruction: contains the user's immediate request or input.

## 2. Zero-Shot Prompting
A task is given without providing task-specific examples.

Example:
> Classify the support message as billing, account, technical, or other.

## 3. Few-Shot Prompting
A task is given together with examples that demonstrate the expected behaviour.

Example:
> “I cannot log in” → account
> “My payment failed” → billing
> “The app crashes” → technical

Then classify a new message.

## 4. Constraints
Constraints define rules the model must follow, such as allowed categories, length limits, prohibited behaviour, and data-handling requirements.

## 5. Output Specification
The expected response structure should be explicitly defined. For application-facing features, structured output such as JSON can make AI responses easier to validate and consume.

## 6. Failure Behaviour
A reliable prompt should define what happens when input is missing, ambiguous, unsupported or invalid. The system should avoid guessing when the task cannot be completed confidently.

## Day 1 Prompt Structure
1. Role / Context
2. Task
3. Inputs
4. Constraints
5. Output Format
6. Failure Behaviour
