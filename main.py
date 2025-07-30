from utils import auth
from utils import cart
from models import restaurant
from models import order  # <-- Add this import


def main():
    print("Welcome to zomato")  # Removed emojis for compatibility
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            auth.register()
        elif choice == '2':
            user = auth.login()
            if user:
                after_login(user)
        elif choice == '3':
            print("Goodbye!")
            break

def after_login(user):
    # Ensure 'cart' key exists for the user
    if 'cart' not in user:
        user['cart'] = []
    if 'orders' not in user:
        user['orders'] = []

    while True:
        print(f"\nHello {user['username']}! What would you like to do?")
        print("1. View Restaurants\n2. View Cart\n3. Place Order\n4. Logout")
        choice = input("Enter choice: ")
        if choice == '1':
            restaurant.view_restaurants(user)
        elif choice == '2':
            cart.view_cart(user)
        elif choice == '3':
            order.create_order(user) 
        elif choice == '4':
            break

if __name__ == "__main__":
    main()
