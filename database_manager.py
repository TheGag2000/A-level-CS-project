import sqlite3
import Login



def create_table():
    conn = sqlite3.connect('Users.db')

    c = conn.cursor()

    c.execute("""CREATE TABLE Users
     (
     username text,
     password text
     )
     """)
    conn.commit()
    conn.close()