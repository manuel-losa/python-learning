import json
from datetime import date

def add_task(tasks, title, priority, due_date):
    
    if priority not in ["High", "Medium", "Low"]:
        print("Invalid priority")
        return 
    
    task = {
        "title": title,
        "done": False,
        "priority": priority,
        "due_date": due_date
    }

    tasks.append(task)

    return tasks


def show_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet")
        return

    for i, task in enumerate(tasks):
        status = "Done" if task["done"] else "Pending"
        print(f"{i} - {task['title']} [{status}] [{task['priority']}] [Due: {task['due_date']}]")


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


def get_tasks_by_priority(tasks, priority):
    priority_tasks = []

    for task in tasks:
        if task["priority"] == priority: 
            priority_tasks.append(task)

    return priority_tasks


def get_overdue_tasks(tasks):

    overdue_tasks = []

    today = date.today()

    for task in tasks:

        due_date = task["due_date"]

        parts = due_date.split("-")

        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])

        due_date = date(year, month, day)

        if due_date <= today and task["done"] == False:

            overdue_tasks.append(task)

    return overdue_tasks

def search_tasks(tasks, search):
    matched_tasks = []

    for task in tasks:
        if search in task["title"]:
            matched_tasks.append(task)

    return matched_tasks


def edit_task(tasks, index, new_title):
    if index < 0 or index >= len(tasks):
        print("Invalid index")
        return tasks
    
    tasks[index]["title"] = new_title
    return tasks


def edit_due_date(tasks, index, new_due_date):
    if index < 0 or index >= len(tasks):
        print("Invalid index")
        return tasks
    
    tasks[index]["due_date"] = new_due_date
    return tasks


def get_stats(tasks):

    completed = 0
    pending = 0 

    for task in tasks:

        if task["done"]:
            completed += 1

        else:
            pending += 1

    return completed, pending

def sort_tasks_by_priority(tasks):
    priority_order = {
        "High" : 1,
        "Medium" : 2,
        "Low" : 3
    }

    sorted_tasks = sorted(
        tasks,
        key=lambda task: priority_order[task["priority"]]
    )

    return sorted_tasks


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