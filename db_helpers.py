# From https://stackoverflow.com/questions/3300464/how-can-i-get-dict-from-sqlite-query
# The Flask documentation as an alternative definition:
# https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
