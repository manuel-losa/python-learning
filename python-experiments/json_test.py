import json


task = {
    "title": "Gym",
    "done": False
}

json_task = json.dumps(task)

print(json_task)

python_task = json.loads(json_task)

print(python_task)
print(type(python_task))


tasks = [
    {"title": "Gym", "done": False},
    {"title": "Study", "done": True}
]

with open("tasks.json", "w") as file:
    json.dump(tasks, file)

with open("tasks.json", "r") as file:
    loaded_tasks = json.load(file)

print(loaded_tasks)
print(type(loaded_tasks))