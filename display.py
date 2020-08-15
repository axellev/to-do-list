from examples import todolist_0

def status_to_string(status):
    if status == "done":
        return " (DONE)"
    elif status == "todo":
        return ""
    else:
        raise Exception("Unexpected status value: should be either done or todo")

def display_items(items):
    for item in items:
      s = status_to_string(item["status"])
      print(str(item["id"]) + ". " + item["description"] + s)

if __name__ == "__main__":
    print(todolist_0["title"])
    display_items(todolist_0["items"])