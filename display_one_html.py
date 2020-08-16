import sqlite3
import sys

from db_helpers import dict_factory
from html_helpers import display_items, html_beginning, html_ending

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
        print(html_beginning)
        print("Il n'y a pas d'item pour cet ID")
        print(html_ending)
        exit(1)

    # We're sure there is exactly one item since we checked above.
    print(html_beginning)
    print("<ul>")
    # calling function
    display_items(items)
    print("</ul>")
    print(html_ending)
