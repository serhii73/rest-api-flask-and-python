import sqlite3

conection = sqlite3.connect("data.db")

cursor = conection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"

cursor.execute(create_table)

user = (1, "serhii", "asdf")

insert_query = "INSERT INTO users VALUES (?, ?, ?)"

cursor.execute(insert_query, user)

users = [(2, "bob", "zxcv"), (3, "alex", "ghjy")]
cursor.executemany(insert_query, users)

select_qery = "SELECT * FROM users"
for i in cursor.execute(select_qery):
    print(i)

conection.commit()
conection.close()

