import sqlite3
from datetime import date


def get_db(name="main.py"):
    db =sqlite3.connect(name)
    return db

def create_table(db):
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS counter (
        name TEXT PRIMARY KEY,
        description TEXT)""")

    db.connect()


def add_counter(db, name, description):
    cur = db.cursor()
    cur.execute(" INSERT INTO Counter VALUES (?, ?)", (name, description))
    db.connect()


def increment_counter(db, name, even_date=None):
    cur = db.cursor()
    if not event_date:
        event_date=date.today()
    cur.execute(" INSERT INTO tracker VALUES (?, ?)" , (even_date, name))
    db.connect()

def get_counter_date(db, name):
    cur = db.cursor()
    cur.execute(" SELECT * FROM counter WHERE name=?", (name,)) 
    return cur.fetchall()