import sqlite3

def create_tables():
    conn = sqlite3.connect('../fitness_management.db')
    c = conn.cursor()

    # Create members table
    c.execute('''CREATE TABLE IF NOT EXISTS members (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    gender TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    join_date TEXT NOT NULL,
                    contact INTEGER NOT NULL
                )''')

    # Create trainers table
    c.execute('''DROP TABLE IF EXISTS trainers''')

    # Create attendance table
    c.execute('''CREATE TABLE IF NOT EXISTS attendance (
                    id INTEGER PRIMARY KEY,
                    member_id INTEGER NOT NULL,
                    class_id INTEGER NOT NULL,
                    date TEXT NOT NULL,
                    FOREIGN KEY (member_id) REFERENCES members(id),
                    FOREIGN KEY (class_id) REFERENCES fitness_classes(id)
                )''')

    # Create fitness_classes table
    c.execute('''CREATE TABLE IF NOT EXISTS fitness_classes (
                    class_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT NOT NULL,
                    duration INTEGER NOT NULL,
                    difficulty TEXT NOT NULL,
                    trainer_id INTEGER NOT NULL,
                    FOREIGN KEY(trainer_id) REFERENCES trainers(trainer_id)
                )''')

    # Create payments table
    c.execute('''CREATE TABLE IF NOT EXISTS payments (
                    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    member_id INTEGER NOT NULL,
                    amount REAL NOT NULL,
                    date TEXT NOT NULL,
                    method TEXT NOT NULL,
                    FOREIGN KEY(member_id) REFERENCES members(member_id)
                )''')

    conn.commit()
    conn.close()

# Function to create the tables
create_tables()
