import jinja2
import sqlite3
import sys

from db_helpers import dict_factory

# helper function similar to the one provided by Flask.
templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
templateEnv = jinja2.Environment(loader=templateLoader)
def render_template(filename, **args):
    template = templateEnv.get_template(filename)
    return template.render(**args)


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

    print(render_template('todolist.html', title=items[0]["title"], items=items))
