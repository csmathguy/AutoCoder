# src/services/github_service.py
from interfaces.github_service_interface import IGitHubService
from config import github_token
from github import Github, GithubException

class GitHubService(IGitHubService):
    def __init__(self):
        self.github = Github(github_token)

    def create_branch(self, repo_name: str, branch_name: str) -> None:
        try:
            repo = self.github.get_repo(repo_name)
            # Check if the branch already exists
            try:
                repo.get_branch(branch_name)
                print(f"Branch '{branch_name}' already exists.")
                return
            except GithubException as e:
                if e.status != 404:
                    raise e  # Re-raise if it's not a 404 error
            source_branch = repo.get_branch('main')
            ref = f"refs/heads/{branch_name}"
            repo.create_git_ref(ref=ref, sha=source_branch.commit.sha)
            print(f"Branch '{branch_name}' created successfully.")
        except GithubException as e:
            print(f"Error creating branch: {e}")

    def commit_file(self, repo_name: str, branch_name: str, file_path: str, content: str) -> None:
        try:
            repo = self.github.get_repo(repo_name)
            repo.create_file(
                path=file_path,
                message=f"Add {file_path}",
                content=content,
                branch=branch_name
            )
            print(f"File '{file_path}' committed to branch '{branch_name}'.")
        except GithubException as e:
            print(f"Error committing code: {e}")
