# src/orchestrator/orchestrator.py
import heapq
from workers.code_generator_worker import CodeGeneratorWorker
from workers.github_worker import GitHubWorker
from services.code_generator_service import CodeGeneratorService
from services.file_service import FileService
from services.github_service import GitHubService

class Orchestrator:
    def __init__(self):
        self.task_queue = []
        self.workers = {
            'code_generation': CodeGeneratorWorker(CodeGeneratorService(), FileService()),
            'github': GitHubWorker(GitHubService()),
        }
        self.feature_count = 0
        self.context = {}  # Shared context

    def add_task(self, task):
        heapq.heappush(self.task_queue, (task.priority, task))

    def execute_tasks(self):
        while self.task_queue:
            priority, task = heapq.heappop(self.task_queue)
            worker = self.workers.get(task.task_type)
            if worker:
                worker.perform_task(task, self.context)
                task.status = 'Completed'
            else:
                print(f"No worker found for task type: {task.task_type}")
                task.status = 'Failed'
