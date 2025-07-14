import datetime
import uuid

def generate_id():
    return str(uuid.uuid4())

def create_order(user):
    if not user['cart']:
        print("Cart is empty. Cannot place order.")
        return None

    address = input("Enter your delivery address: ")

    order = {
        "order_id": generate_id(),
        "items": user['cart'],
        "timestamp": str(datetime.datetime.now()),
        "total": sum(item['price'] for item in user['cart']),
        "status": "Confirmed",
        "address": address
    }

    user['orders'].append(order)
    user['cart'] = []  
    print(f"Order placed successfully! Order ID: {order['order_id']}")
    print(f"Total amount: ₹{order['total']}")
    print("Thank you for your order!")
    return order
