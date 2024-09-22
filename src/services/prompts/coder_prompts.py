# src/services/prompts/coder_prompts.py
def coder_prompt(user_input: str) -> str:
    return f"Generate Python code for the following feature:\n{user_input}"