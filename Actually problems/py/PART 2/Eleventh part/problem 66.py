import psycopg2
from psycopg2 import sql

#Connect to the PostgreSQL database
conn = psycopg2.connect(
dbname="postgres",
user="postgres",
password="Andyis",
host="localhost",
port="5432"
)

#Create a cursor object
cur = conn.cursor()

#Create a table
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
id SERIAL PRIMARY KEY,
username VARCHAR(50) NOT NULL,
email VARCHAR(100) NOT NULL
)
""")

#Insert some data
cur.execute("""
INSERT INTO users (username, email) VALUES (%s, %s)
""", ("john_doe", ""))

cur.execute("""
INSERT INTO users (username, email) VALUES (%s, %s)
""", ("jane_doe", ""))

#Commit the transaction
conn.commit()

#Query the data
cur.execute("SELECT * FROM users")
rows = cur.fetchall()

print("All Users:")
for row in rows:
    print(row)

#Close the cursor and the connection
cur.close()
conn.close()