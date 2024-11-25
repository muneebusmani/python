import json
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

    # Input the Name of Task
    task = input(
        """
        enter task name:
        """
    )

    # Input the Description of Task
    description = input(
        """
        enter task description
        """
    )

    # Load all tasks
    data = load_tasks()

    # Append currently created task to existing tasks
    data.append({"task": task, "description": description})

    # Write the appended json to tasks.json file
    save_tasks(data)
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


while True:
    selection = int(
        input(
            """
        1. Create a Task
        2. List all Task
    """
        )
    )
    if selection == 1:
        create_task()
    elif selection == 2:
        list_tasks()
