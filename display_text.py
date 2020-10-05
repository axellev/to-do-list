# This program display the content of a given todolist. The todolist is chosen
# by giving a todolist ID. Example usage:
#
#   py display_text.py 1
#
# The database can be created manually with:
#
#   sqlite3 example.db < example.sql


import sqlite3
import sys
from db_helpers import dict_factory

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

# execute only if run as a script
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Veuillez donner un argument")
        exit(1)

    i = int(sys.argv[1])

    if i <= 0:
        print("Veuillez rentrer un nombre supérieur à zéro")
        exit(1)

    # connection to to db
    conn = sqlite3.connect('example.db')
    conn.row_factory = dict_factory

    # used to interact with the db
    cursor = conn.cursor()
    args = (i,)
    cursor.execute('''
        SELECT items.id, items.description, items.status, todolists.title
        FROM items, todolists
        WHERE items.todolist=todolists.id
          AND items.todolist=?;
    ''', args)
    items = cursor.fetchall()

    if len(items) == 0:
        print("Il n'y a pas d'items pour cet ID de todolist")
        exit(1)

    # We're sure there is at least one item since we checked above.
    # All of them have the same title.
    print(items[0]["title"])
    # calling function
    display_items(items)
