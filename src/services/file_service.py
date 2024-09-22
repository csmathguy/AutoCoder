# src/services/file_service.py
from interfaces.file_service_interface import IFileService
import os

class FileService(IFileService):
    def save_code_to_file(self, code: str, file_path: str) -> None:
        # Ensure the 'features' directory exists
        features_dir = 'features'
        os.makedirs(features_dir, exist_ok=True)
        
        # Construct the full file path
        full_file_path = os.path.join(features_dir, file_path)
        
        # Save the code to the file
        with open(full_file_path, 'w') as file:
            file.write(code)
