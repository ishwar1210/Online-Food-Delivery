from db.database import save_data, load_data  # Add this import at the top

def get_restaurants():
    return [
        {
            "name": "Pizza Hub",
            "menu": [
                {"item": "Margherita", "price": 199},
                {"item": "Cheese Burst", "price": 249},
                {"item": "Farmhouse", "price": 299},
                {"item": "Pepperoni", "price": 349},
                {"item": "Veggie Supreme", "price": 279},
                {"item": "Paneer Makhani", "price": 319},
                {"item": "BBQ Chicken", "price": 359},
                {"item": "Mexican Green Wave", "price": 289},
                {"item": "Deluxe Veggie", "price": 269},
                {"item": "Chicken Sausage", "price": 329},
                {"item": "Double Cheese", "price": 259},
                {"item": "Spicy Triple Tango", "price": 309},
                {"item": "Classic Corn", "price": 219},
                {"item": "Peri Peri Paneer", "price": 339},
                {"item": "Italiano", "price": 359},
                {"item": "Tandoori Paneer", "price": 349}
            ]
        },
        {
            "name": "Tandoori Express",
            "menu": [
                {"item": "Paneer Tikka", "price": 299},
                {"item": "Chicken Tikka", "price": 349},
                {"item": "Tandoori Mushroom", "price": 259},
                {"item": "Seekh Kebab", "price": 319},
                {"item": "Malai Tikka", "price": 329},
                {"item": "Tandoori Chicken", "price": 399},
                {"item": "Fish Tikka", "price": 379},
                {"item": "Stuffed Aloo", "price": 229},
                {"item": "Paneer Malai", "price": 309},
                {"item": "Chicken Tangdi", "price": 359},
                {"item": "Veg Platter", "price": 399},
                {"item": "Non-Veg Platter", "price": 499},
                {"item": "Tandoori Broccoli", "price": 279},
                {"item": "Tandoori Prawns", "price": 429},
                {"item": "Mutton Seekh", "price": 389},
                {"item": "Tandoori Soya Chaap", "price": 249}
            ]
        },
        {
            "name": "South Spice",
            "menu": [
                {"item": "Masala Dosa", "price": 129},
                {"item": "Plain Dosa", "price": 99},
                {"item": "Rava Dosa", "price": 139},
                {"item": "Onion Uttapam", "price": 149},
                {"item": "Medu Vada", "price": 89},
                {"item": "Idli Sambar", "price": 99},
                {"item": "Pesarattu", "price": 159},
                {"item": "Ghee Roast", "price": 169},
                {"item": "Set Dosa", "price": 119},
                {"item": "Paneer Dosa", "price": 179},
                {"item": "Cheese Uttapam", "price": 159},
                {"item": "Rasam Vada", "price": 109},
                {"item": "Mysore Bonda", "price": 99},
                {"item": "Tomato Rice", "price": 129},
                {"item": "Curd Rice", "price": 119},
                {"item": "Lemon Rice", "price": 119}
            ]
        },
        {
            "name": "Burger Point",
            "menu": [
                {"item": "Classic Veg Burger", "price": 99},
                {"item": "Cheese Burger", "price": 129},
                {"item": "Chicken Burger", "price": 149},
                {"item": "Paneer Burger", "price": 139},
                {"item": "Double Patty Burger", "price": 179},
                {"item": "Aloo Tikki Burger", "price": 109},
                {"item": "Spicy Chicken Burger", "price": 159},
                {"item": "Egg Burger", "price": 119},
                {"item": "Fish Burger", "price": 169},
                {"item": "BBQ Burger", "price": 149},
                {"item": "Veggie Delight", "price": 129},
                {"item": "Crispy Chicken Burger", "price": 159},
                {"item": "Mushroom Burger", "price": 139},
                {"item": "Corn & Cheese Burger", "price": 129},
                {"item": "Peri Peri Burger", "price": 149},
                {"item": "Grilled Chicken Burger", "price": 179}
            ]
        },
        {
            "name": "Chinese Wok",
            "menu": [
                {"item": "Veg Hakka Noodles", "price": 159},
                {"item": "Chicken Fried Rice", "price": 179},
                {"item": "Veg Manchurian", "price": 149},
                {"item": "Chilli Paneer", "price": 169},
                {"item": "Spring Roll", "price": 119},
                {"item": "Chicken Lollipop", "price": 199},
                {"item": "Schezwan Rice", "price": 169},
                {"item": "Paneer Chilli Dry", "price": 179},
                {"item": "Egg Fried Rice", "price": 149},
                {"item": "Veg Momos", "price": 99},
                {"item": "Chicken Momos", "price": 129},
                {"item": "Crispy Corn", "price": 139},
                {"item": "Hot & Sour Soup", "price": 109},
                {"item": "Sweet Corn Soup", "price": 109},
                {"item": "Paneer Fried Rice", "price": 159},
                {"item": "Veg Schezwan Noodles", "price": 169}
            ]
        },
        {
            "name": "Punjabi Dhaba",
            "menu": [
                {"item": "Dal Makhani", "price": 179},
                {"item": "Paneer Butter Masala", "price": 199},
                {"item": "Butter Chicken", "price": 249},
                {"item": "Chole Bhature", "price": 129},
                {"item": "Aloo Paratha", "price": 99},
                {"item": "Rajma Chawal", "price": 139},
                {"item": "Lassi", "price": 59},
                {"item": "Tandoori Roti", "price": 29},
                {"item": "Amritsari Kulcha", "price": 89},
                {"item": "Sarson Da Saag", "price": 159},
                {"item": "Makki Di Roti", "price": 39},
                {"item": "Paneer Tikka Masala", "price": 209},
                {"item": "Chicken Curry", "price": 229},
                {"item": "Jeera Rice", "price": 79},
                {"item": "Mix Veg", "price": 149},
                {"item": "Baingan Bharta", "price": 139}
            ]
        },
        {
            "name": "Biryani House",
            "menu": [
                {"item": "Veg Biryani", "price": 179},
                {"item": "Chicken Biryani", "price": 229},
                {"item": "Mutton Biryani", "price": 279},
                {"item": "Egg Biryani", "price": 199},
                {"item": "Paneer Biryani", "price": 209},
                {"item": "Hyderabadi Biryani", "price": 249},
                {"item": "Dum Biryani", "price": 239},
                {"item": "Fish Biryani", "price": 259},
                {"item": "Prawn Biryani", "price": 269},
                {"item": "Keema Biryani", "price": 259},
                {"item": "Kolkata Biryani", "price": 239},
                {"item": "Lucknowi Biryani", "price": 249},
                {"item": "Soya Biryani", "price": 189},
                {"item": "Tandoori Biryani", "price": 219},
                {"item": "Mushroom Biryani", "price": 199},
                {"item": "Special Biryani", "price": 299}
            ]
        },
        {
            "name": "Sandwich Stop",
            "menu": [
                {"item": "Veg Sandwich", "price": 79},
                {"item": "Cheese Sandwich", "price": 99},
                {"item": "Grilled Sandwich", "price": 119},
                {"item": "Paneer Sandwich", "price": 129},
                {"item": "Chicken Sandwich", "price": 149},
                {"item": "Club Sandwich", "price": 159},
                {"item": "Egg Sandwich", "price": 109},
                {"item": "Corn Sandwich", "price": 99},
                {"item": "Mayo Sandwich", "price": 89},
                {"item": "Chutney Sandwich", "price": 79},
                {"item": "Veggie Delight", "price": 109},
                {"item": "Toasted Sandwich", "price": 119},
                {"item": "Chocolate Sandwich", "price": 99},
                {"item": "Bombay Sandwich", "price": 129},
                {"item": "Spicy Paneer Sandwich", "price": 139},
                {"item": "Tandoori Chicken Sandwich", "price": 159}
            ]
        },
        {
            "name": "Rolls & Wraps",
            "menu": [
                {"item": "Veg Roll", "price": 89},
                {"item": "Paneer Roll", "price": 119},
                {"item": "Chicken Roll", "price": 139},
                {"item": "Egg Roll", "price": 109},
                {"item": "Mutton Roll", "price": 159},
                {"item": "Cheese Roll", "price": 99},
                {"item": "Double Egg Roll", "price": 129},
                {"item": "Aloo Roll", "price": 89},
                {"item": "Soya Roll", "price": 99},
                {"item": "Paneer Tikka Roll", "price": 139},
                {"item": "Chicken Tikka Roll", "price": 159},
                {"item": "Veggie Wrap", "price": 109},
                {"item": "Falafel Wrap", "price": 129},
                {"item": "BBQ Chicken Wrap", "price": 149},
                {"item": "Mushroom Roll", "price": 119},
                {"item": "Corn & Cheese Wrap", "price": 129}
            ]
        },
        {
            "name": "Sweet Treats",
            "menu": [
                {"item": "Gulab Jamun", "price": 59},
                {"item": "Rasgulla", "price": 69},
                {"item": "Jalebi", "price": 79},
                {"item": "Rabri", "price": 99},
                {"item": "Kheer", "price": 89},
                {"item": "Ice Cream", "price": 99},
                {"item": "Brownie", "price": 109},
                {"item": "Cupcake", "price": 69},
                {"item": "Cheesecake", "price": 129},
                {"item": "Chocolate Mousse", "price": 119},
                {"item": "Fruit Salad", "price": 79},
                {"item": "Ladoo", "price": 59},
                {"item": "Barfi", "price": 69},
                {"item": "Peda", "price": 59},
                {"item": "Halwa", "price": 89},
                {"item": "Malpua", "price": 99}
            ]
        },
        {
            "name": "Juice Junction",
            "menu": [
                {"item": "Orange Juice", "price": 59},
                {"item": "Apple Juice", "price": 69},
                {"item": "Mango Juice", "price": 79},
                {"item": "Pineapple Juice", "price": 69},
                {"item": "Watermelon Juice", "price": 59},
                {"item": "Grape Juice", "price": 69},
                {"item": "Lemonade", "price": 49},
                {"item": "Carrot Juice", "price": 59},
                {"item": "Beetroot Juice", "price": 69},
                {"item": "Mixed Fruit Juice", "price": 89},
                {"item": "Pomegranate Juice", "price": 99},
                {"item": "Sweet Lime Juice", "price": 59},
                {"item": "Strawberry Juice", "price": 89},
                {"item": "Banana Shake", "price": 79},
                {"item": "Chikoo Shake", "price": 79},
                {"item": "Cold Coffee", "price": 99}
            ]
        },
        {
            "name": "Pasta Palace",
            "menu": [
                {"item": "White Sauce Pasta", "price": 159},
                {"item": "Red Sauce Pasta", "price": 159},
                {"item": "Pesto Pasta", "price": 179},
                {"item": "Arrabiata Pasta", "price": 169},
                {"item": "Mac & Cheese", "price": 189},
                {"item": "Veggie Pasta", "price": 149},
                {"item": "Chicken Pasta", "price": 199},
                {"item": "Mushroom Pasta", "price": 169},
                {"item": "Spinach Pasta", "price": 159},
                {"item": "Cheese Pasta", "price": 179},
                {"item": "Baked Pasta", "price": 189},
                {"item": "Paneer Pasta", "price": 179},
                {"item": "Corn Pasta", "price": 149},
                {"item": "Broccoli Pasta", "price": 169},
                {"item": "Schezwan Pasta", "price": 159},
                {"item": "Mix Sauce Pasta", "price": 179}
            ]
        }
    ]

def view_restaurants(user):
    restaurants = get_restaurants()
    for idx, rest in enumerate(restaurants, 1):
        print(f"{idx}. {rest['name']}")
    try:
        choice = int(input("Select restaurant: "))
        selected = restaurants[choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return

    print(f"\nMenu for {selected['name']}:")
    for i, item in enumerate(selected['menu'], 1):
        print(f"{i}. {item['item']} - ₹{item['price']}")

    while True:
        item_choice = input("Select menu item to add to cart (0 to exit): ")
        if item_choice == '0':
            break
        try:
            item_idx = int(item_choice) - 1
            menu_item = selected['menu'][item_idx]
            user['cart'].append(menu_item)
            print(f"{menu_item['item']} added to cart.")
            # Save data after adding to cart
            data = load_data()
            for u in data['users']:
                if u['username'] == user['username']:
                    u['cart'] = user['cart']
            save_data(data)
        except (ValueError, IndexError):
            print("Invalid menu item.")
