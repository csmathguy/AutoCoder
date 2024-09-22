# src/workers/ai_worker.py
from workers.worker import Worker
from config import openai_api_key  # API key from config
from openai import OpenAI

class AIWorker(Worker):
    def __init__(self):
        self.client = OpenAI(api_key=openai_api_key)  # Use the new OpenAI client

    def perform_task(self, task):
        prompt = task.params.get('prompt', '')
        if prompt:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",  # Specify the model
                messages=[{"role": "user", "content": prompt}]
            )
            print(f"AI Generated Response: {response.choices[0].message.content}")
        else:
            print("No prompt provided for AI task.")
