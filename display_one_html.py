import sqlite3
import sys

from db_helpers import dict_factory
from display_html import render_template

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
        print(render_template('error.html', message="This item doesn't exist."))
        exit(1)

    # We're sure there is exactly one item since we checked above.
    print(render_template('item.html', item=items[0]))
