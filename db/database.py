import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3308,  
        user="root",
        password="Sanku@940",
        database="zomato_python"
    )

