# src/task.py

class Task:
    def __init__(self, task_id, task_type, params=None, priority=0):
        self.task_id = task_id
        self.task_type = task_type
        self.params = params or {}
        self.priority = priority
        self.status = 'Pending'

    def __repr__(self):
        return f"Task({self.task_id}, {self.task_type}, {self.priority})"
