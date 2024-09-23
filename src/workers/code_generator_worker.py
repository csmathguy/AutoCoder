# src/workers/code_generator_worker.py
import os
from workers.worker import Worker
from interfaces.code_generator_service_interface import ICodeGeneratorService
from interfaces.file_service_interface import IFileService

class CodeGeneratorWorker(Worker):
    def __init__(self, code_generator_service: ICodeGeneratorService, file_service: IFileService):
        self.code_generator_service = code_generator_service
        self.file_service = file_service

    def perform_task(self, task, context):
        feature_description = task.params.get('feature_description')
        feature_id = task.params.get('feature_id')
        if feature_description and feature_id:
            # Generate code
            code = self.code_generator_service.generate_code(feature_description)
            # Save code to file using feature_id
            file_name = f"{feature_id}.json"
            self.file_service.save_code_to_file(code, file_name)
            print(f"Generated code saved to 'features/{file_name}'.")
            # Store code in context
            context['generated_code'] = code
            context['file_path'] = os.path.join('features', file_name)
        else:
            print("Feature description or feature ID missing for code generation task.")
