import json
import msvcrt
from tabulate import tabulate
import os


if "tasks.json" not in os.listdir(os.getcwd()):
    with open("tasks.json", "x") as f:
        json.dump([], f, indent=4)

# text_frame.py


def frame_text(text):
    """
    Function to frame the input text within a dynamically sized box
    with 2 padding spaces on both sides.

    Args:
    - text: The string to be framed.

    Returns:
    - The framed text string with dynamic width and padding.
    """
    # Calculate the dynamic width based on the length of the input text
    # Add 2 padding on each side and 2 for the vertical borders
    width = len(text) + 4  # Adding 4 to account for the padding and vertical borders

    # Prepare the frame
    frame = "+" + "-" * (width - 2) + "+"

    # Frame the text with 2 spaces of padding on each side
    framed_text = frame + "\n"  # Start with the top border
    framed_text += "| " + text + " |\n"  # Text with 2 padding spaces on each side
    framed_text += frame + "\n"  # Bottom border

    return framed_text


# function to load all the tasks
def load_tasks():
    clear_terminal()
    f = open("tasks.json", "r")
    tasks = json.load(f)
    f.close
    return tasks


# function for saving tasks
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)
    clear_terminal()


# function for clearing the terminal
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


# function for creation of task
def create_task():

    # clear the clutter before proceeding
    clear_terminal()

    # input the name of task
    task = input(frame_text("enter task name:"))

    # input the description of task
    description = input(frame_text("enter task description"))

    # load all tasks
    tasks = load_tasks()
    max_id = max(task["id"] for task in tasks) if tasks else 0
    id = max_id + 1
    # append currently created task to existing tasks
    tasks.append({"id": id, "task": task, "description": description})

    # write the appended json to tasks.json file
    save_tasks(tasks)
    list_tasks()


# function for listing tasks
def list_tasks():

    # clear the command line
    clear_terminal()

    # load all tasks
    data = load_tasks()

    # empty dictionary for creating rows
    table_data = []

    # looping through each object{} in dictionary[]
    for task in data:

        # adding values of each task in each row for that table data
        table_data.append(
            [
                # this fetches the values for the specified keys and if the value isn't found, it defaults to empty string ""
                task.get("id", ""),
                task.get("task", ""),
                task.get("description", ""),
            ]
        )

    # now finally printing that key less data with only values and headers from tablute library
    print(
        tabulate(
            table_data,
            headers=["id", "task", "description"],
        )
    )


def list_task(id):

    # clear the command line
    clear_terminal()

    # load all tasks
    data = load_tasks()

    # empty dictionary for creating rows
    table_data = []

    # looping through each object{} in dictionary[]
    for task in data:

        if task["id"] == id:
            # adding values of each task in each row for that table data
            table_data.append(
                [
                    # this fetches the values for the specified keys and if the value isn't found, it defaults to empty string ""
                    task.get("id", ""),
                    task.get("task", ""),
                    task.get("description", ""),
                ]
            )

    # now finally printing that key less data with only values and headers from tablute library
    print(
        tabulate(
            table_data,
            headers=["id", "task", "description"],
        )
    )


# function for taking choice of user actions
def get_choice(sentence: str) -> int:
    print(sentence)
    # wait for key press without requiring enter
    choice = msvcrt.getch()  # this captures a single keypress
    return int(choice.decode("utf-8"))


def find_task(id: int):
    tasks = load_tasks()
    task = {}
    for task in tasks:
        if task["id"] == id:
            return task


def update_task(id):
    while True:

        task: dict | None = {}
        task = find_task(id)
        if type(task) is not dict:
            print(
                "Error in the specified task, either id is incorrect, or there is some issue with the json"
            )

        choice: int = get_choice(
            frame_text(
                "update name(1), update description(2), update both(3), go back(0)"
            )
        )
        if type(choice) is not int:
            print("Incorrect Choice, Please Try Again")
        elif choice is 1:
            new_name = input(frame_text("Enter new name"))
            old_name = task["task"]
        # elif choice is 2:
        # elif choice is 3:
        # elif choice is 0:


def delete_task(id):
    print(id)


def select_task():
    while True:
        clear_terminal()
        id = int(input("enter task id"))
        operation = get_choice(frame_text("edit task(1), delete task(2), go back(0)"))
        if operation == 1:
            update_task(id)
        elif operation == 2:
            delete_task(id)
        elif operation == 0:
            break
        else:
            print("invalid choice please try again")


def app():
    while True:
        list_tasks()
        selection = get_choice(
            frame_text("create new task (1), refresh tasks(2), select task(3), exit(0)")
        )
        if selection == 1:
            create_task()
        elif selection == 2:
            list_tasks()
        elif selection == 3:
            select_task()
        elif selection == 0:
            break
        else:
            print("Invalid Choice")


app()
