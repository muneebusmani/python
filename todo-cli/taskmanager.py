import json
import msvcrt
from tabulate import tabulate
import os


if "tasks.json" not in os.listdir(os.getcwd()):
    with open("tasks.json", "x") as f:
        json.dump([], f, indent=4)


def load_tasks():
    clear_terminal()
    f = open("tasks.json", "r")
    tasks = json.load(f)
    f.close
    return tasks


# Function for saving tasks
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)
    clear_terminal()


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def create_task():

    # clear the clutter before proceeding
    clear_terminal()

    # Input the Name of Task
    task = input(
        """
        -------------------
        | Enter task name:|
        -------------------
        """
    )

    # Input the Description of Task
    description = input(
        """
        -------------------------
        | Enter task description|
        -------------------------
        """
    )

    # Load all tasks
    tasks = load_tasks()
    max_id = max(task["id"] for task in tasks) if tasks else 0
    id = max_id + 1
    # Append currently created task to existing tasks
    tasks.append({"Id": id, "task": task, "description": description})

    # Write the appended json to tasks.json file
    save_tasks(tasks)
    list_tasks()


def list_tasks():

    # clear the command line
    clear_terminal()

    # Load all Tasks
    data = load_tasks()

    # Empty Dictionary for creating rows
    table_data = []

    # Looping through each object{} in dictionary[]
    for task in data:

        # Adding values of each task in each row for that table data
        table_data.append(
            [
                # This fetches the values for the specified keys and if the value isn't found, it defaults to empty string ""
                task.get("id", ""),
                task.get("task", ""),
                task.get("description", ""),
            ]
        )

    # Now finally printing that key less data with only values and headers from tablute library
    print(
        tabulate(
            table_data,
            headers=["Id", "Task", "Description"],
        )
    )


def get_choice():
    print(
        """
----------------------------------------------------------------------------------
| Create new Task (1), Refresh Tasks(2), Update Task(3), Delete Task(4), exit(0) |
----------------------------------------------------------------------------------
"""
    )
    # Wait for key press without requiring Enter
    choice = msvcrt.getch()  # This captures a single keypress
    return int(choice.decode("utf-8"))


def update_task():
    print("hello")


def delete_task():
    print("hello")


while True:
    list_tasks()
    selection = get_choice()
    if selection == 1:
        create_task()
    elif selection == 2:
        list_tasks()
    elif selection == 3:
        update_task()
    elif selection == 4:
        delete_task()
    elif selection == 0:
        break
