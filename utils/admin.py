from db.database import load_data, save_data

def view_all_users():
    data = load_data()
    print("All Registered Users:")
    for user in data['users']:
        print(f"- {user['username']}")

def view_all_orders():
    data = load_data()
    print("All Orders:")
    for user in data['users']:
        for ord in user.get('orders', []):
            print(f"User: {user['username']} | Order ID: {ord['order_id']} | Total: ₹{ord['total']} | Status: {ord['status']}")
