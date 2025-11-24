import sqlite3

# 1. Create / connect to SQLite database (file will be created in your system)
connection = sqlite3.connect("my_database.db")   # Creates my_database.db in current folder
cursor = connection.cursor()

# 2. Create two tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    product TEXT,
    amount INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
""")

# 3. Insert 3 rows into users table
cursor.executemany("""
INSERT INTO users (name, email) VALUES (?, ?)
""", [
    ("Alice", "alice@example.com"),
    ("Bob", "bob@example.com"),
    ("Charlie", "charlie@example.com")
])

# 4. Insert 3 rows into orders table
cursor.executemany("""
INSERT INTO orders (user_id, product, amount) VALUES (?, ?, ?)
""", [
    (1, "Laptop", 1200),
    (2, "Headphones", 200),
    (3, "Monitor", 300)
])

# 5. Commit changes and close connection
connection.commit()

print("Database created and data inserted successfully!")
