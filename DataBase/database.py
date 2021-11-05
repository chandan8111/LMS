import mysql.connector

config={
    'user':'root',
    'password': 'Maya@786',
    'host': '127.0.0.1',
    'database': 'lms'
}




std=25
conn = mysql.connector.connect(**config)
cursor = conn.cursor()
cursor.execute(f"DELETE FROM student WHERE id={std}")
conn.commit()