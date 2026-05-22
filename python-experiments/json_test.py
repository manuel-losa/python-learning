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