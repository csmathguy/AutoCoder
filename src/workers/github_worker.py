# src/workers/github_worker.py
import os
from workers.worker import Worker
from interfaces.github_service_interface import IGitHubService

class GitHubWorker(Worker):
    def __init__(self, github_service: IGitHubService):
        self.github_service = github_service
        self.repo_name = "csmathguy/AutoCoder"

    def perform_task(self, task, context):
        action = task.params.get('action')
        branch_name = task.params.get('branch_name')

        if action == 'create_branch':
            self.github_service.create_branch(self.repo_name, branch_name)
        elif action == 'commit_code':
            file_name = task.params.get('file_name')
            # Get the generated code from context
            code = context.get('generated_code')
            if not code:
                print("No code available to commit.")
                return
            # Update the file path to include 'features/'
            file_path = os.path.join('features', file_name)
            # Read the code from the file to ensure consistency
            with open(file_path, 'r') as file:
                content = file.read()
            self.github_service.commit_file(self.repo_name, branch_name, file_path, content)
        elif action == 'notify_user':
            print(f"Code is ready for review in branch '{branch_name}'.")
        else:
            print(f"Action '{action}' not supported.")
