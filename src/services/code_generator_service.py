# src/services/code_generator_service.py
from interfaces.code_generator_service_interface import ICodeGeneratorService
import openai
from config import openai_api_key
from src.services.prompts.coder_prompts import coder_prompt

class CodeGeneratorService(ICodeGeneratorService):
    def __init__(self):
        self.client = openai.OpenAI(api_key=openai_api_key)

    def generate_code(self, feature_description: str) -> str:
        # Use the API endpoint for chat completions
        prompt = coder_prompt(feature_description)
        if prompt:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",  # Specify the model
                messages=[{"role": "user", "content": prompt}]
            )
        # Access the content using dot notation
        code = response.choices[0].message.content.strip()
        return code
