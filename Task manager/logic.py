def add_task(tasks, title):
    task = {
        "title": title,
        "done": False
    }

    tasks.append(task)
    return tasks


def show_tasks(tasks):
    if len(tasks) == 0:
        print("No task yet")
        return
    
    for i, task in enumerate(tasks):
        status = "Done" if task["done"] else "Pending"
        print(f"{i} - {task['title']} [{status}]")


def complete_task(tasks, index):
    if index < 0 or index >= len(tasks):
        print("Invalid index")
        return tasks
    
    tasks[index]["Done"] = True
    return tasks


def delete_task(tasks, index):
    if index < 0 or index >= len(tasks):
        print("Invalid index")
        return tasks
    
    tasks.pop(index)
    return tasks
