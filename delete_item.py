import jinja2
import sqlite3
import sys

from db_helpers import dict_factory



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

    # used to interact with the db---
    cursor = conn.cursor()
    args = (i,)
    cursor.execute('''
        DELETE FROM items
        WHERE items.id=?;
    ''', args)
    conn.commit()
    deleted_row_count = cursor.rowcount
    if deleted_row_count == 0:
        print("L'item n'existe pas")
    else:
        print("L'item n°" + str(i) + " a été supprimé")
 
    
