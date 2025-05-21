import sqlite3

conn = sqlite3.connect("events.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()

if not rows:
    print("No events found in database.")
else:
    for row in rows:
        print(f"Title: {row[0]}\nDate: {row[1]}\nLink: {row[2]}\n---")

conn.close()
