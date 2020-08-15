from examples import todolist_0

def display_items(items):
    for item in items:
      if item["is_done"]:
        s = " (DONE)"
      else:
        s = ""
      print(str(item["id"]) + ". " + item["description"] + s)

if __name__ == "__main__":
    print(todolist_0["title"])
    display_items(todolist_0["items"])