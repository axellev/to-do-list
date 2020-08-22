from flask import Flask, g, render_template, request, url_for, redirect
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

# Custom 404 page, see
# https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error.html', message='Not Found'), 404

@app.route('/todolist/<int:todolist_id>')
def display_todolist(todolist_id):
    items = query("""
        SELECT items.id, items.description, items.status, todolists.title
        FROM items, todolists
        WHERE items.todolist=todolists.id
          AND items.todolist=?;""", (todolist_id,))
    if len(items) == 0:
        todolists = query("select * from todolists where id=?", (todolist_id,))
        if len(todolists) == 0:
            return render_template('error.html', message="This todolist doesn't exist."), 404
        return render_template('todolist.html', title=todolists[0]["title"], todolist_id=todolist_id, items=[])   
    return render_template('todolist.html', title=items[0]["title"], todolist_id=todolist_id, items=items)

@app.route('/item/<int:item_id>')
def display_item(item_id):
    items = query("""
        SELECT *
        FROM items
        WHERE items.id=?;""", (item_id,))
    if len(items) == 0:
        return render_template('error.html', message="This item doesn't exist."), 404
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
        return render_template('error.html', message='Error: the field "description" is too short.'), 400

    description = request.form['description']

    if len(description) < 5:
        return render_template('error.html', message='Error: the field "description" is too short.'), 400

    query("""
        INSERT INTO items (description, todolist)
        VALUES (?, ?)""", (description, todolist_id))
    commit()
    
    return render_template('itemAdded.html')

@app.route('/new')
def new_todolist():
    return render_template('newTodolist.html')

@app.route('/add', methods=["POST"])
def add_todolist():
    
    if 'title' not in request.form:
        return render_template('error.html', message='Error: the field "title" is missing.'), 400

    title = request.form['title']

    if len(title) < 1:
        return render_template('error.html', message='Error: the field "title" is too short.'), 400

    query("""
        INSERT INTO todolists (title)
        VALUES (?)""", (title,))
    commit()
    return redirect(url_for('add_new_item'))





if __name__ == "__main__":
    app.run()
