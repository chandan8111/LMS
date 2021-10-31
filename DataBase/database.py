import mysql.connector

config={
    'user':'root',
    'password': 'Maya@786',
    'host': '127.0.0.1',
    'database': 'lms'
}
std=5
conn = mysql.connector.connect(**config)
cursor = conn.cursor()
cursor.execute(f"SELECT * FROM student where id={std}")
resu=cursor.fetchall()
print(resu)
print(resu[0][0])
conn.commit()