import sqlite3
import uuid


def add_sample_data():
    db = sqlite3.connect("foodDelivery.db")
    cursor = db.cursor()

    restaurants_data = [
        (str(uuid.uuid4()), "kfc", "Finger Lickin' Good", "https://example.com/kfc_logo.png", "kfc1@example.com", "kfc_password"),
        (str(uuid.uuid4()), "pizzahut", "Gather 'Round the Good Stuff", "https://example.com/pizzahut_logo.png", "ph@example.com", "ph_password")
    ]

    items_data = [
        (str(uuid.uuid4()), "Margherita Pizza", 12.99, "veg", "https://example.com/margherita_img.png", "https://example.com/margherita_nutrition.png", restaurants_data[0][0]),
        (str(uuid.uuid4()), "Spicy Chicken Wings", 9.99, "nonVeg", "https://example.com/chicken_wings_img.png", "https://example.com/chicken_wings_nutrition.png", restaurants_data[0][0]),

        (str(uuid.uuid4()), "Classic Pepperoni Pizza", 14.99, "nonVeg", "https://example.com/pepperoni_img.png", "https://example.com/pepperoni_nutrition.png", restaurants_data[1][0]),
        (str(uuid.uuid4()), "Veggie Supreme Pizza", 11.99, "veg", "https://example.com/veggie_supreme_img.png", "https://example.com/veggie_supreme_nutrition.png", restaurants_data[1][0]),
    ]

    for record in restaurants_data:
        cursor.execute("INSERT INTO restaurants (id, name, caption, logoUrl, email, password) VALUES (?, ?, ?, ?, ?, ?)", record)

    for record in items_data:
        cursor.execute("INSERT INTO items (id, name, price, type, imgUrl, nutritionalUrl, restaurant_id) VALUES (?, ?, ?, ?, ?, ?, ?)", record)

    users_data = [
        (str(uuid.uuid4()), "user1@example.com", "user1_password", "John", "Doe", "1234567890", "123 Main St"),
        (str(uuid.uuid4()), "user2@example.com", "user2_password", "Jane", "Smith", "9876543210", "456 Elm St")
    ]

    for record in users_data:
        cursor.execute("INSERT INTO users (id, email, password, first_name, last_name, ph_number, address) VALUES (?, ?, ?, ?, ?, ?, ?)", record)

    db.commit()
    db.close()


