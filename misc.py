import sqlite3

def verify_database_data(db_path: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM members_data")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

verify_database_data("data/gym_data.sqlite")
