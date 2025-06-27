from models import order
from db.database import load_data, save_data

def place_order(user):
    data = load_data()
    user_record = next((u for u in data['users'] if u['username'] == user['username']), None)
    if not user_record:
        print("User not found in database.")
        return

    new_order = order.create_order(user_record)
    if new_order:
        save_data(data)

def view_orders(user):
    if not user['orders']:
        print("No orders placed yet.")
        return
    for idx, ord in enumerate(user['orders'], 1):
        print(f"\nOrder {idx}:")
        for item in ord['items']:
            print(f"- {item['item']} - ₹{item['price']}")
        print(f"Total: ₹{ord['total']} | Status: {ord['status']} | Placed on: {ord['timestamp']}")
