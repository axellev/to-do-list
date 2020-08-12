# Filter and display the items at the status "to-do".
from examples import todolist_0

items = todolist_0["items"]
todos = []

for item in items:
    if not item["is_done"]:
        todos.append(item)

print(todos)
