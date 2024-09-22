# src/interfaces/code_generator_service_interface.py
from abc import ABC, abstractmethod

class ICodeGeneratorService(ABC):
    @abstractmethod
    def generate_code(self, feature_description: str) -> str:
        pass
