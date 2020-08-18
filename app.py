from flask import Flask, g, render_template, request
import sqlite3

from db_helpers import dict_factory

app = Flask(__name__)


DATABASE = './example.db'

# This is explained in Flask documentation:
# https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/
def get_conn():
    conn = getattr(g, '_database', None)
    if conn is None:
        conn = g._database = sqlite3.connect(DATABASE)
        conn.row_factory = dict_factory
    return conn

def query(query, args=()):
    cursor = get_conn().execute(query, args)
    records = cursor.fetchall()
    cursor.close()
    return records

def commit():
    get_conn().commit()

@app.teardown_appcontext
def close_connection(exception):
    conn = getattr(g, '_database', None)
    if conn is not None:
        conn.close()

@app.route('/todolist/<int:todolist_id>')
def display_todolist(todolist_id):
    items = query("""
        SELECT items.id, items.description, items.status, todolists.title
        FROM items, todolists
        WHERE items.todolist=todolists.id
          AND items.todolist=?;""", (todolist_id,))
    if len(items) == 0:
        return "Il n'y a pas de to -do list correspondant à cet ID"
    return render_template('todolist.html', title=items[0]["title"], todolist_id=todolist_id, items=items)
    

@app.route('/item/<int:item_id>')
def display_item(item_id):
    items = query("""
        SELECT *
        FROM items
        WHERE items.id=?;""", (item_id,))
    if len(items) == 0:
        return "Il n'y a pas d'item pour cet ID"
    return render_template('item.html', item=items[0])

@app.route('/')
def display_todolists():
    todolists = query("select * from todolists")
    return render_template("listtodolists.html", todolists=todolists)

@app.route('/todolist/<int:todolist_id>/new')
def new_item(todolist_id):
    return render_template('newItem.html', todolist_id=todolist_id)

@app.route('/todolist/<int:todolist_id>/add', methods=["POST"])
def add_new_item(todolist_id):

    if 'description' not in request.form:
        return 'Error: the field "description" is missing.'

    description = request.form['description']

    if len(description) < 5:
        return 'Error: the field "description" is too short.'

    query("""
        INSERT INTO items (description, todolist)
        VALUES (?, ?)""", (description, todolist_id))
    commit()
    return "Voila."

if __name__ == "__main__":
    app.run()
