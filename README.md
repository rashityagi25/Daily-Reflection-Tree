# Daily-Reflection-Tree
# Daily Reflection Decision Tree

## Objective
To build a deterministic decision tree that suggests daily reflection activities based on user input.

## Inputs
- Mood: Happy / Sad / Stressed
- Energy Level: High / Low
- Goal: Productivity / Relaxation / Self-growth

## Decision Tree Logic

IF Mood = Sad AND Energy = Low
→ Suggest: Write 3 things you are grateful for

IF Mood = Stressed AND Energy = High
→ Suggest: Go for a walk and do breathing exercises

IF Mood = Happy
→ Suggest: Write today's achievements

## Output
Each input combination produces a fixed, predefined output.

## Why Deterministic?
The system always gives the same output for the same input. No randomness is used.

## Guardrails for AI
- Only predefined responses are used
- No random or creative outputs allowed
- Avoid vague suggestions
- Responses are manually verified

## Negative Prompting
- Do NOT generate random suggestions
- Only select from fixed outputs
- Stay within mental wellness context

- This implementation ensures determinism by using fixed conditional logic.
No probabilistic or AI-based responses are used in Part A.
