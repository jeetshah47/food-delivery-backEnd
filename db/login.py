import sqlite3
from db.restaurant import fetch_restaurant_by_id
from db.user import fetch_user_by_id


def check_credentials_restaurant(email, password):
    db = sqlite3.connect("foodDelivery.db")
    cursor = db.cursor()

    cursor.execute("SELECT * FROM restaurants WHERE email = ?", (email,))
    record = cursor.fetchone()

    if record and record[5] == password:
        db.close()
        return True, fetch_restaurant_by_id(record[0])
    else:
        db.close()
        return False, "invalid"


def check_credentials_user(email, password):
    db = sqlite3.connect("foodDelivery.db")
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    record = cursor.fetchone()

    if record and record[2] == password:
        db.close()
        return True, fetch_user_by_id(record[0])
    else:
        db.close()
        return False, "invalid"
