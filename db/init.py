import sqlite3


def startDb():
    create_restaurants_table()
    create_items_table()
    create_users_table()


def create_restaurants_table():
    db = sqlite3.connect("foodDelivery.db")
    cursor = db.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='restaurants'")
    table_exists = cursor.fetchone()

    if table_exists:
        cursor.execute("DROP TABLE restaurants")

    cursor.execute('''CREATE TABLE restaurants (
        id TEXT PRIMARY KEY,
        name TEXT,
        caption TEXT,
        logoUrl TEXT,
        email TEXT UNIQUE,
        password TEXT,
        city TEXT 
    )''')

    db.commit()
    db.close()


def create_items_table():
    db = sqlite3.connect("foodDelivery.db")
    cursor = db.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='items'")
    table_exists = cursor.fetchone()

    if table_exists:
        cursor.execute("DROP TABLE items")

    cursor.execute('''CREATE TABLE items (
        id TEXT PRIMARY KEY,
        name TEXT,
        price REAL,
        type TEXT,
        imgUrl TEXT,
        nutritionalUrl TEXT,
        restaurant_id TEXT,
        FOREIGN KEY (restaurant_id) REFERENCES restaurants (id)
    )''')

    db.commit()
    db.close()


def create_users_table():
    db = sqlite3.connect("foodDelivery.db")
    cursor = db.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    table_exists = cursor.fetchone()

    if table_exists:
        cursor.execute("DROP TABLE users")

    cursor.execute('''CREATE TABLE users (
        id TEXT PRIMARY KEY,
        email TEXT UNIQUE,
        password TEXT,
        first_name TEXT,
        last_name TEXT,
        ph_number TEXT,
        address TEXT
    )''')

    db.commit()
    db.close()

