import sqlite3

def create_connection():
    conn = sqlite3.connect("users.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS course (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            unit INTEGER NOT NULL
        )           
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_enrollment (
            user_id INTEGER,
            course_id INTEGER,
            PRIMARY KEY (user_id, course_id),
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (course_id) REFERENCES course(id)
        )
    ''')
    conn.commit()
    conn.close()