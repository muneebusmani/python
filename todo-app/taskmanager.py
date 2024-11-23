import json
import os
from enum import Enum

from tabulate import tabulate


# Enum definitions for Status and Priority
class Status(Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    ON_HOLD = "on_hold"
    PAUSED = "paused"
    COMPLETE = "complete"


class Priority(Enum):
    LOW = "low"
    HIGH = "high"
    NORMAL = "normal"
    URGENT = "urgent"


class Task_type(Enum):
    TASK = "task"
    APPROVAL = "approval"
    MILESTONE = "milestone"


def clear_terminal():
    if os.name == "nt":  # For Windows
        os.system("cls")
    else:
        os.system("clear")  # For Mac/Linux


def create():
    clear_terminal()
    # Input collection
    print("Enter Title of Task:")
    title = input()

    print("Enter Description of Task:")
    description = input()

    print("Enter Priority of Task (low, high, normal, urgent):")
    priority = input().lower()

    print("Enter status (todo, in_progress, on_hold, paused, complete):")
    status = input().lower()

    print("Enter the type (task, milestone, approval):")
    task_type = input().lower()

    # Validate priority and status against the Enum values
    if priority not in [p.value for p in Priority]:
        print("Invalid priority!")
        return  # Exit the function if priority is invalid

    if status not in [s.value for s in Status]:
        print("Invalid status!")
        return  # Exit the function if status is invalid

    if task_type not in [t.value for t in Task_type]:
        print("Invalid type!")
        return  # Exit the function if status is invalid

    # Create the task dictionary
    task_json = {
        "name": title,
        "description": description,
        "priority": priority,
        "status": status,
        "type": task_type,
    }

    # Read existing tasks from the JSON file
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []  # If the file is empty or malformed, start with an empty list
    else:
        data = []  # If the file doesn't exist, create a new list

    # Append the new task to the data
    data.append(task_json)

    # Write updated data back to the JSON file
    with open("tasks.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Task added successfully!")


def list_tasks():
    clear_terminal()
    # Read the tasks from tasks.json
    try:
        with open("tasks.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("The tasks.json file does not exist.")
        return
    except json.JSONDecodeError:
        print("Error reading tasks.json. It may be malformed.")
        return

    # Prepare data for the table
    table_data = []
    for task in data:
        # Extracting each field in the task and adding it as a row for the table
        table_data.append(
            [
                task.get("name", ""),
                task.get("description", ""),
                task.get("priority", ""),
                task.get("status", ""),
                task.get("type", ""),
            ]
        )

    # Define headers
    headers = ["Title", "Description", "Priority", "Status", "Type"]

    # Print the table
    print(tabulate(table_data, headers=headers, tablefmt="pretty"))


def list_task():
    print("task create")


def update_task():
    print("task create")


def delete_task():
    print("task create")


while True:
    print(
        """
    1. Create a new task
    2. List all task
    3. List a specific task
    4. Update a specific task
    5. Delete a specific task
    0. Exit
    """
    )
    selection = int(input())
    if selection == 1:
        create()
    elif selection == 2:
        list_tasks()
    elif selection == 3:
        list_task()
    elif selection == 4:
        update_task()
    elif selection == 5:
        delete_task()
    elif selection == 0:
        break
    else:
        continue
