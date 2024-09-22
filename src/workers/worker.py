# src/worker.py
from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def perform_task(self, task):
        pass
