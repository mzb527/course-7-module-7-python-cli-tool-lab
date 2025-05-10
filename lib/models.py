class Task:
    all_tasks = []  # Store tasks globally

    def __init__(self, title):
        self.title = title
        self.completed = False
        Task.all_tasks.append(self)  # Add task to global list

    def complete(self):
        self.completed = True
        print(f"✅ Task '{self.title}' completed.")

class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"📌 Task '{task.title}' added to {self.name}.")