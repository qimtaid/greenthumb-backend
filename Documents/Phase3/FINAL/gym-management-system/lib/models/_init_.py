import sqlite3

DATABASE = '../fitness_management.db'

def connect_db():
    return sqlite3.connect(DATABASE)
