import sqlite3
import sys
from display import display_items
from display_from_db import dict_factory

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
        SELECT * FROM items 
        WHERE items.id=?;
    ''', args)
    items = cursor.fetchall()

    if len(items) == 0:
        print("Il n'y a pas d'item pour cet ID")
        exit(1)

    display_items(items)
