import sqlite3

def create_db():
    conn = sqlite3.connect('events.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            date TEXT NOT NULL,
            location TEXT NOT NULL
        )
    ''')

    # Seed sample events
    sample_events = [
        ('Sydney Opera Concert', '2025-05-30', 'Sydney'),
        ('Sydney Jazz Festival', '2025-06-15', 'Sydney'),
        ('Bondi Beach Music Fest', '2025-07-20', 'Sydney'),
        ('Melbourne Art Expo', '2025-07-01', 'Melbourne'),
        ('Brisbane Food Carnival', '2025-08-05', 'Brisbane'),
        ('Perth Cultural Fest', '2025-09-10', 'Perth'),
        ('Adelaide Wine Tasting', '2025-10-12', 'Adelaide'),
    ]

    c.executemany('INSERT INTO events (title, date, location) VALUES (?, ?, ?)', sample_events)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()
    print("Database created and seeded successfully.")
