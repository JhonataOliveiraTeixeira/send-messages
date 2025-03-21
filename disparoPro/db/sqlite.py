import sqlite3
from flask import g

def get_db():
    """Obtém a conexão com o banco de dados para a requisição atual."""
    if 'db' not in g:
        g.db = sqlite3.connect('database.db', check_same_thread=False)
        g.db.row_factory = sqlite3.Row  # Para retornar dicionários em vez de tuplas
    return g.db

def close_db(e=None):
    """Fecha a conexão com o banco de dados ao final da requisição."""
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init():
    db = get_db()
    cursor = db.cursor()
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            instance TEXT,
            name TEXT,
            number TEXT,
            error TEXT
        )
    ''')
    db.commit()
    cursor.close()

def insert_contact(instance, name, number):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        'INSERT INTO contacts (instance, name, number) VALUES (?, ?, ?)', 
        (instance, name, number)
    )
    db.commit()
    cursor.close()

def insert_error(instance, name, number, error):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        'INSERT INTO contacts (instance, name, number, error) VALUES (?, ?, ?, ?)', 
        (instance, name, number, error)
    )
    db.commit()
    cursor.close()

def view_errors(instance):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        'SELECT name, number, error FROM contacts WHERE error IS NOT NULL AND instance = ?', 
        (instance,)
    )
    errors = cursor.fetchall()
    cursor.close()
    return errors