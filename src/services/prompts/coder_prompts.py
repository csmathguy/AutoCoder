# src/services/prompts/coder_prompts.py

def coder_prompt(user_input: str) -> str:
    return f"""
As an expert Python developer, generate code for the following feature request while adhering to these guidelines:

- Follow Python best practices and PEP 8 style guidelines.
- Apply SOLID principles.
- Utilize Gang of Four design patterns where appropriate.
- Ensure the code is well-documented with comments and docstrings.
- **Output the result in valid JSON format with the code as a single string where newlines (`\\n`) and indentation are represented by escape sequences.**
- **Make sure to properly escape any special characters like quotes within the code string to produce valid JSON.**

Example format:

{{
    "file": "path/to/file.py",
    "type": "create",  // options: 'create', 'update', 'delete'
    "location": "function_or_class_name",  // Optional
    "code": "<code_snippet_with_escaped_characters>"
}}

Feature Request:
{user_input}
"""
