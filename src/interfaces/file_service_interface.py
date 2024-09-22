# src/interfaces/file_service_interface.py
from abc import ABC, abstractmethod

class IFileService(ABC):
    @abstractmethod
    def save_code_to_file(self, code: str, file_path: str) -> None:
        pass
