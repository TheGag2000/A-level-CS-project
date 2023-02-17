import sqlite3


def create_table():
    conn = sqlite3.connect('Users.db')

    c = conn.cursor()

    c.execute("""CREATE TABLE flashcards
     (
     question text,
     answer text,
     difficulty integer
     )
     """)
    conn.commit()
    conn.close()


