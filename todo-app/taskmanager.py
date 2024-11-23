import json
from tabulate import tabulate
import os

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
        task = input(
            """
        enter task name:
        """
        )
        description = input(
            """
        enter task description
        """
        )
        task_json = json.dumps({"task": task, "description": description})

        if "tasks.json" not in os.listdir(os.getcwd()):
            open("tasks.json", "x")

        f = open("tasks.json", "w")
        f.write(task_json)
        f.close()
    elif selection == 2:
        with open("tasks.json", "r") as file:
            data = json.load(file)
            table_data = []
            for task in data:
                table_data = table_data.append(
                    [
                        task.get("id", ""),
                        task.get("name", ""),
                        task.get("description", ""),
                    ]
                )
            print(
                tabulate(
                    table_data,
                    headers=["Id", "Task", "Description"],
                )
            )

            # data = {"name": "lol", "description": "lol"}
            # table_data = [
            #     {data.get("name"), data.get("description")},
            #     {data.get("name"), data.get("description")},
            # ]
            # print(
            #     tabulate(
            #         [
            #             {
            #                 1,
            #                 "House chores",
            #                 "do all the chores and make sure everything is done",
            #             },
            #             {
            #                 2,
            #                 "House chores",
            #                 "do all the chores and make sure everything is done",
            #             },
            #         ],
            #     )
            # )
