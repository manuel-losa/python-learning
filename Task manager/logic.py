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


def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            line = f"{task['title']},{task['done']}\n"
            file.write(line)


def get_pending_tasks(tasks):
        pending_tasks = []

        for task in tasks:
            if task["done"] == False:
                pending_tasks.append(task)

        return pending_tasks
    

def get_completed_tasks(tasks):
        completed_tasks = []

        for task in tasks:
            if task["done"] == True:
                completed_tasks.append(task)

        return completed_tasks            


def load_tasks():
    tasks = []

    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                title, done = line.strip().split(",")
                tasks.append({
                    "title": title,
                    "done": done == "True"
                })
    except:
        pass

    return tasks