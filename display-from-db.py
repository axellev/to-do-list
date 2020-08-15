import sqlite3
from display import display_items

# From https://stackoverflow.com/questions/3300464/how-can-i-get-dict-from-sqlite-query
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# execute only if run as a script
if __name__ == "__main__":

    # connection to to db
    conn = sqlite3.connect('example.db')
    conn.row_factory = dict_factory

    # used to interact with the db
    cursor = conn.cursor()
    cursor.execute('select * from items')
    items = cursor.fetchall()

    # calling function
    display_items(items)