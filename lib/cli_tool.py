import argparse
from lib.models import Task, User

users = {}  # Stores users dynamically

def add_task(args):
    task = Task(args.title)
    print(f"📌 Task '{task.title}' added globally.")

def complete_task(args):
    for task in Task.all_tasks:
        if task.title == args.title:
            task.complete()
            return
    print("❌ Task not found.")

def list_tasks(args):
    print("\n📋 Task List:")
    for task in Task.all_tasks:
        status = "✅ Completed" if task.completed else "⏳ Pending"
        print(f"- {task.title}: {status}")

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers()

    add_parser = subparsers.add_parser("add-task", help="Add a new task globally")
    add_parser.add_argument("title")
    add_parser.set_defaults(func=add_task)

    complete_parser = subparsers.add_parser("complete-task", help="Complete a task")
    complete_parser.add_argument("title")
    complete_parser.set_defaults(func=complete_task)

    list_parser = subparsers.add_parser("list-tasks", help="List all tasks")
    list_parser.set_defaults(func=list_tasks)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()