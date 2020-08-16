from flask import Flask, g, render_template
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

@app.teardown_appcontext
def close_connection(exception):
    conn = getattr(g, '_database', None)
    if conn is not None:
        conn.close()

@app.route('/')
def hello_world():
    items = query("select * from items")
    return render_template('todolist.html', title='Hello, World!', items=items)

@app.route('/item/<int:item_id>')
def display_item(item_id):
    return 'Item %s!' % item_id


if __name__ == "__main__":
    app.run()
