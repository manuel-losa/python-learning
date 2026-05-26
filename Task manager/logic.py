import json

def add_task(tasks, title):
    task = {
        "title": title,
        "done": False
    }

    tasks.append(task)
    return tasks


def show_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet")
        return

    for i, task in enumerate(tasks):
        status = "Done" if task["done"] else "Pending"
        print(f"{i} - {task['title']} [{status}]")


def complete_task(tasks, index):
    if index < 0 or index >= len(tasks):
        print("Invalid index")
        return tasks

    tasks[index]["done"] = True
    return tasks


def delete_task(tasks, index):
    if index < 0 or index >= len(tasks):
        print("Invalid index")
        return tasks

    tasks.pop(index)
    return tasks


def get_tasks_by_status(tasks, status):
    filtered_tasks = []

    for task in tasks:
        if task["done"] == status:
            filtered_tasks.append(task)

    return filtered_tasks


def search_tasks(tasks, search):
    matched_tasks = []

    for task in tasks:
        if search in task["title"]:
            matched_tasks.append(task)

    return matched_tasks


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

        return tasks
    
    except:
        return[]