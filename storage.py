import json
from models import Task


def save_tasks(file_path: str, tasks):
    data = [task.__dict__ for task in tasks]
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def load_tasks(file_path: str):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return [Task(**item) for item in data]