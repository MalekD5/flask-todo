import sqlite3 as sql

def create_table(conn):
    # todo table
    conn.execute('''CREATE TABLE IF NOT EXISTS todo (id INTEGER PRIMARY KEY, name TEXT, completed INTEGER)''')
    conn.commit()

conn = sql.connect('db.db')
create_table(conn)

def getConn():
    return conn