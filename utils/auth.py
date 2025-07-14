from db.database import get_connection

def register():
    conn = get_connection()
    cursor = conn.cursor()
    username = input("Enter username: ")
    password = input("Enter password: ")
    phone = input("Enter phone number: ")

    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    if cursor.fetchone():
        print(" Username already exists.")
        return

    cursor.execute(
        "INSERT INTO users (username, password, phone) VALUES (%s, %s, %s)",
        (username, password, phone)
    )
    conn.commit()
    print(" User registered successfully.")

def login():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    username = input("Enter username: ")
    password = input("Enter password: ")

    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    if user:
        print(f" Login successful. Welcome {user['username']}!")
        return user
    else:
        print(" Invalid credentials.")
        return None

