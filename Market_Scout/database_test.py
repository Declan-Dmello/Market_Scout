import sqlite3 as sql

conn = sql.connect("signup_login.db")
cur = conn.cursor()
cur.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        email VARCHAR NOT NULL , 
                        password VARCHAR NOT NULL

                    );
                    """)

#cur.execute("INSERT INTO users (first_name , last_name , email , password) VALUES ('Rui' , 'NERD', 'ruinerd123456@gmail.com', 'asdfgh')")
# Make the Email  unique Later


conn.commit()

password1 = "ThePassword"
email = "ruinerd123@gmail.com"
cur.execute("UPDATE users SET password = 'a' WHERE id = (SELECT id FROM users WHERE email = 'ruinerd12345@gmail.com')")
cur.execute("SELECT * FROM users")
results1 = cur.fetchall()
print(results1)
conn.close()
# print(results)
print("Inserted Successfully")


