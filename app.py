import mysql.connector
import time

while True:
    try:
        db = mysql.connector.connect(
            host="db",
            user="root",
            password="db_pass123",
        )
        print("Connected to MySQL successfully!")
        break
    except mysql.connector.Error as err:
        print("❌ Connection failed, retrying in 3s:", err)
        time.sleep(3)

