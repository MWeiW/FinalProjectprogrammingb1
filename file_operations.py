import json
import os

FILE_NAME = "tasks.txt"

def load_tasks():
    tasks = []
    if not os.path.exists(FILE_NAME):
        return tasks

    with open(FILE_NAME, "r") as file:
        for line in file:
            if line.strip():
                tasks.append(json.loads(line.strip()))
    return tasks


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(json.dumps(task) + "\n")
