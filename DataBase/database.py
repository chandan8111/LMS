import mysql.connector

config={
    'user':'root',
    'password': 'Maya@786',
    'host': '127.0.0.1',
    'database': 'lms'
}

data=(
    "rama",
    "n. raj",
    200,
    34,
    "rsg",
)


std=3457
conn = mysql.connector.connect(**config)
cursor = conn.cursor()
cursor.execute(f"UPDATE book SET title={data[0]},author={data[1]},publishedYear={data[2]},totalPage={data[3]},category={data[4]}  WHERE id={std}")
conn.commit()