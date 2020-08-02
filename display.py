# An example to-do list.
todolist_0 = {
    "title": "courses",
    "items": [
        {"description": "legumes", "is_done": False},
        {"description": "fruits", "is_done": True},
        {"description": "viande", "is_done": False},
    ]
}

if __name__ == "__main__":
    # Afficher une to-do list avec des indices en utilisant enumerate (mettre
    # tout entre parenthese dico + liste).
    print(todolist_0["title"])
    for (i, item) in enumerate(todolist_0["items"]):
      if item["is_done"]:
        s = " (DONE)"
      else:
        s = ""
      print(str(i+1) + ". " + item["description"] + s)
