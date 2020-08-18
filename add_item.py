import jinja2
import sqlite3
import sys

from db_helpers import dict_factory

# execute only if run as a script
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Veuillez donner un argument")
        exit(1)

    i = str(sys.argv[1])
    x = int(sys.argv[2])

    conn = sqlite3.connect('example.db')
    conn.row_factory = dict_factory

    # used to interact with the db---
    cursor = conn.cursor()
    args = (i, x)
    cursor.execute('''
       INSERT into items(description, todolist)
       VALUES(?, ?)
    ''', args)
    conn.commit()
    #return cursor.lastrowid
    #lastrow = cursor.lastrowid

    added_row_count = cursor.rowcount
    if added_row_count == 0:
        print("L'item n'a pas été ajouté")
    else:
        print("L'item: " + str(i)  + " a été ajouté")
 