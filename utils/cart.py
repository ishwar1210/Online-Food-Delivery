def view_cart(user):
    if not user['cart']:
        print("Your cart is empty.")
        return
    print("\nYour Cart:")
    total = 0
    for idx, item in enumerate(user['cart'], 1):
        print(f"{idx}. {item['item']} - ₹{item['price']}")
        total += item['price']
    print(f"Total: ₹{total}")
