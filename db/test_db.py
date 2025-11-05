import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="558732",   # your MySQL password
        database="car_sales_db"
    )

try:
    conn = get_db_connection()
    cursor = conn.cursor()

    # ✅ Check which database you’re connected to
    cursor.execute("SELECT DATABASE();")
    print("Connected to database:", cursor.fetchone()[0])

    # ✅ List all tables in that database
    cursor.execute("SHOW TABLES;")
    print("Tables:", cursor.fetchall())

    # ✅ Describe the 'sales' table
    cursor.execute("DESCRIBE sales;")
    print("\nColumns in 'sales':")
    for row in cursor.fetchall():
        print(row)

    # ✅ Try reading data
    cursor.execute("SELECT * FROM sales ORDER BY sale_id DESC LIMIT 5;")
    print("\nSample rows:")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()

except mysql.connector.Error as e:
    print("❌ MySQL Error:", e)
