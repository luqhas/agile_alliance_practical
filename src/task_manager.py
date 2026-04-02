class Task:
    def __init__(self, title: str, done: bool = False):
        self.title = title
        self.done = done

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title: str):
        self.tasks.append(Task(title))

    def complete_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].done = True

    def remove_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def get_tasks(self):
        return self.tasks

    def get_pending_tasks(self):
        return [t for t in self.tasks if not t.done]