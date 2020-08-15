import sqlite3

# From https://stackoverflow.com/questions/3300464/how-can-i-get-dict-from-sqlite-query
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
    

conn = sqlite3.connect('example.db')
conn.row_factory = dict_factory

# used to interact with the db
cursor = conn.cursor()


cursor.execute('select * from items')
records = cursor.fetchall()

for record in records:
    print(str(record.get("id")) + ". " + record.get("description") + " " + record.get("status"))


        

