# src/workers/github_worker.py

import os
from workers.worker import Worker
from interfaces.github_service_interface import IGitHubService

class GitHubWorker(Worker):
    def __init__(self, github_service: IGitHubService):
        self.github_service = github_service
        self.repo_name = "csmathguy/AutoCoder"  # Replace with your repository

    def perform_task(self, task, context):
        action = task.params.get('action')
        print(f"GitHubWorker: Starting action '{action}'.")

        if action == 'create_branch':
            branch_name = task.params.get('branch_name')
            print(f"GitHubWorker: Creating branch '{branch_name}'.")
            self.github_service.create_branch(self.repo_name, branch_name)
            print(f"GitHubWorker: Finished creating branch '{branch_name}'.")

        elif action == 'commit_code':
            branch_name = task.params.get('branch_name')
            file_name = task.params.get('file_name')
            code = context.get('generated_code')
            if not code:
                print("No code available to commit.")
                return
            file_path = os.path.join('features', file_name)
            print(f"GitHubWorker: Committing file '{file_path}' to branch '{branch_name}'.")
            self.github_service.commit_file(self.repo_name, branch_name, file_path, code)
            print(f"GitHubWorker: Finished committing file '{file_path}'.")

        elif action == 'create_pull_request':
            title = task.params.get('title')
            body = task.params.get('body')
            head_branch = task.params.get('branch_name')
            base_branch = task.params.get('base_branch', 'main')

            print(f"GitHubWorker: Creating pull request from '{head_branch}' to '{base_branch}' with title '{title}'.")
            self.github_service.create_pull_request(
                repo_name=self.repo_name,
                title=title,
                body=body,
                head_branch=head_branch,
                base_branch=base_branch
            )

        elif action == 'notify_user':
            branch_name = task.params.get('branch_name')
            print(f"Code is ready for review in branch '{branch_name}'.")

        else:
            print(f"Action '{action}' not supported by GitHubWorker.")