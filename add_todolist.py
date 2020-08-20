import jinja2
import sqlite3
import sys

from db_helpers import dict_factory

# execute only if run as a script
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Give an argument")
        exit(1)


    i = str(sys.argv[1])

    conn = sqlite3.connect('example.db')
    conn.row_factory = dict_factory

    # used to interact with the db---
    cursor = conn.cursor()
    args = (i,)
    cursor.execute('''
       INSERT INTO todolists (title)
       VALUES (?)
    ''', args)
    conn.commit()
    #return cursor.lastrowid
    #lastrow = cursor.lastrowid

    added_row_count = cursor.rowcount
    if added_row_count == 0:
        print("The to-do list wasn't created")
    else:
        print("The to-do list: " + str(i)  + " was created")
 