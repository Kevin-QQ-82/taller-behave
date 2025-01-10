from datetime import datetime

class TodoList:
    def __init__(self):
        self.tasks = []
        self.creation_date = datetime.now().strftime('%Y-%m-%d')

    def add_task(self, description):
        if any(task['description'] == description for task in self.tasks):
            return "Task already exists"
        self.tasks.append({"description": description, "completed": False})
        return "Task added"

    def list_tasks(self):
        return [task['description'] for task in self.tasks]

    def mark_completed(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['completed'] = True
                return
        raise ValueError("Task not found")

    def delete_task(self, description):
        self.tasks = [task for task in self.tasks if task['description'] != description]
