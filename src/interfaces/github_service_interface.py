# src/interfaces/github_service_interface.py
from abc import ABC, abstractmethod

class IGitHubService(ABC):
    @abstractmethod
    def create_branch(self, repo_name: str, branch_name: str) -> None:
        pass

    @abstractmethod
    def commit_file(self, repo_name: str, branch_name: str, file_name: str, content: str) -> None:
        pass
    
    @abstractmethod
    def create_pull_request(
        self,
        repo_name: str,
        title: str,
        body: str,
        head_branch: str,
        base_branch: str = 'main'
    ) -> None:
        pass