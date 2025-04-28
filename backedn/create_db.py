import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create the `user` table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        userid TEXT NOT NULL UNIQUE,
        address TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Insert sample data
sample_data = [
    ('test1', '123 Elm Street', 'password123'),
    ('test2', '456 Oak Avenue', 'password123'),
    ('test3', '789 Pine Road', 'password123')
]

cursor.executemany('''
    INSERT OR IGNORE INTO users (userid, address, password)
    VALUES (?, ?, ?)
''', sample_data)

# Commit the changes
conn.commit()
conn.close()

print("Database and table created successfully with sample data.")
