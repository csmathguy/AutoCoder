# src/main.py

import sys
import os
import uuid  # Import uuid for unique IDs
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from orchestrator.orchestrator import Orchestrator
from tasks.task import Task

if __name__ == '__main__':
    feature_description = input("Please describe the feature you want to add: ")

    orchestrator = Orchestrator()

    # Generate a unique feature ID
    feature_id = f"feature_{uuid.uuid4().hex[:8]}"

    # Create GitHub task to create a feature branch
    branch_name = feature_id
    create_branch_task = Task(
        task_id=1,
        task_type='github',
        params={'action': 'create_branch', 'branch_name': branch_name},
        priority=1
    )
    orchestrator.add_task(create_branch_task)

    # Create code generation task
    code_gen_task = Task(
        task_id=2,
        task_type='code_generation',
        params={'feature_description': feature_description, 'feature_id': feature_id},
        priority=2
    )
    orchestrator.add_task(code_gen_task)

    # Add a task to commit the generated code
    commit_task = Task(
        task_id=3,
        task_type='github',
        params={
            'action': 'commit_code',
            'branch_name': branch_name,
            'file_name': f"{feature_id}.py",
        },
        priority=3
    )
    orchestrator.add_task(commit_task)

    # Add a task to create a pull request
    pr_task = Task(
        task_id=4,
        task_type='github',
        params={
            'action': 'create_pull_request',
            'branch_name': branch_name,
            'title': f"Add feature {feature_id}",
            'body': f"This PR adds the feature: {feature_description}"
        },
        priority=4
    )
    orchestrator.add_task(pr_task)

    orchestrator.execute_tasks()
