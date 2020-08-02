# Display a single to-do list item given its index.
# The index starts at 1 (instead of 0 in Python).
# Usage:
#   py display-one.py 2
import sys

from examples import todolist_0

if __name__ == "__main__":
    if 2 > len(sys.argv):
        print("Veuillez donner un argument")
        exit(1)

    i = int(sys.argv[1]) - 1

    if i < 0:
        print("Veuillez rentrer un nombre supérieur à zéro")
        exit(1)

    if i >= len(todolist_0["items"]):
        print("La liste ne contient pas cet index")
        exit(1)

    items = todolist_0["items"]
    item = items[i]
    description = item["description"]
    print(description)
