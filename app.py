from flask import Flask, g, render_template, request, url_for, redirect, session
import os
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash

from db_helpers import dict_factory

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

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

def query_one(query, args=()):
    cursor = get_conn().execute(query, args)
    record = cursor.fetchone()
    cursor.close()
    return record

# Useful for inserts. This returns the last row ID.
def query_with_lastrowid(query, args=()):
    cursor = get_conn().execute(query, args)
    lastrowid = cursor.lastrowid
    cursor.close()
    return lastrowid

# Useful for deletes. This returns how many rows are touched.
def query_with_rowcount(query, args=()):
    cursor = get_conn().execute(query, args)
    rowcount = cursor.rowcount
    cursor.close()
    return rowcount

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
        return render_template('error.html', message='Error: the field "description" is missing.'), 400

    description = request.form['description']

    if len(description) < 5:
        return render_template('error.html', message='Error: the field "description" is too short.'), 400

    query("""
        INSERT INTO items (description, todolist)
        VALUES (?, ?)""", (description, todolist_id))
    commit()
    return redirect(url_for('display_todolist', todolist_id=todolist_id))

@app.route('/todolist/<int:todolist_id>/delete_form/<int:item_id>')
def delete_item_form(todolist_id, item_id):
    return render_template('deleteItem.html', todolist_id=todolist_id, item_id=item_id)

@app.route('/item/<int:item_id>/delete', methods=["POST"])
def delete_item(item_id):
    if 'todolist_id' not in request.form:
        return render_template('error.html', message='Error: the field "todolist_id" is missing.'), 400

    todolist_id = request.form['todolist_id']

    try:
        todolist_id = int(todolist_id)
    except ValueError:
        return render_template('error.html', message='Error: the field "todolist_id" is not a integer.'), 400

    args = (item_id,)
    rowcount = query_with_rowcount('''
        DELETE FROM items
        WHERE items.id=?;
    ''', args)
    commit()

    if rowcount:
        return redirect(url_for('display_todolist', todolist_id=todolist_id))
    else:
        return render_template('error.html', message="Error: the item doesn't exist."), 400

@app.route('/item/<int:item_id>/done', methods=["POST"])
def done_item(item_id):
    if 'todolist_id' not in request.form:
        return render_template('error.html', message='Error: the field "todolist_id" is missing.'), 400

    todolist_id = request.form['todolist_id']

    try:
        todolist_id = int(todolist_id)
    except ValueError:
        return render_template('error.html', message='Error: the field "todolist_id" is not a integer.'), 400

    args = (item_id,)
    rowcount = query_with_rowcount('''
        UPDATE items
        SET status='done'
        WHERE items.id=?;
    ''', args)
    commit()

    if rowcount:
        return redirect(url_for('display_todolist', todolist_id=todolist_id))
    else:
        return render_template('error.html', message="Error: the item doesn't exist."), 400

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

    lastrowid = query_with_lastrowid("""
        INSERT INTO todolists (title)
        VALUES (?);""", (title,))
    commit()
    return redirect(url_for('display_todolist', todolist_id=lastrowid))

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = False
        user = query_one("""
            SELECT * FROM users WHERE username=?
        """, (username,))

        if user:
            if check_password_hash(user['hashed_password'], password):
                session['username'] = username
                return redirect(url_for('login'))
            else:
                return render_template('error.html', message="Login or password mismatch.")
        else:
            # The user doesn't exist, but don't reveal this fact.
            return render_template('error.html', message="Login or password mismatch.")

    else:
        return render_template('formUsers.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        if not username:
            return render_template('error.html', message="Username cannot be empty")
        elif not password:
            return render_template('error.html', message="Paswword cannot be empty")
        elif not email:
            return render_template('error.html', message="Email cannot be empty")

        hashed_password = generate_password_hash(password)
        query("""
            INSERT INTO users (username, hashed_password, email)
            VALUES (?,?,?)""", (username, hashed_password, email))
        commit()
        # TODO Check the return value of the INSERT (e.g. the username or the email already exist).
        return redirect(url_for('display_todolists'))
    else:
        return render_template('formRegister.html')

if __name__ == "__main__":
    # Create the example database if it doesn't exist.
    if not os.path.isfile(DATABASE):
        sql = open('example.sql', 'r').read()
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.executescript(sql)
        cursor.close()
        conn.commit()

    if 'PORT' in os.environ:
        port = os.environ['PORT']
    else:
        port = 5000

    app.run(host='0.0.0.0', port=port)
