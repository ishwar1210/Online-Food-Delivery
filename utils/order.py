from db.database import get_connection
from datetime import datetime

def place_order(user):
    conn = get_connection()
    cursor = conn.cursor()

    cart = user.get('cart', [])
    if not cart:
        print("Cart is empty. Cannot place order.")
        return

    address = input("Enter your delivery address: ")

    total = sum(item['price'] for item in cart)
    order_time = datetime.now()

    # Insert into orders table
    cursor.execute(
        "INSERT INTO orders (user_id, order_time, total_price, address) VALUES (%s, %s, %s, %s)",
        (user['id'], order_time, total, address)
    )
    order_id = cursor.lastrowid

    # Insert items into order_items
    for item in cart:
        cursor.execute(
            "INSERT INTO order_items (order_id, item_name, price) VALUES (%s, %s, %s)",
            (order_id, item['item'], item['price'])
        )

    conn.commit()
    print(f"Order placed successfully! Order ID: {order_id}")

    # Empty the user's cart
    user['cart'] = []
