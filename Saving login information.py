import mysql.connector
import re

conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='maktabkhooneh')

cursor = conn.cursor()

email = input("Enter your email: ")

while not re.search(r'^[a-zA-Z0-9]+@[a-zA-Z]+[.][a-zA-Z]+', email):
  print("Email is invalid!")
  print("Valid email is like example@gmail.com")
  email = input("Enter your email again: ")

password = input("Enter your password: ")

cursor.execute('INSERT INTO users values (\''+email+'\', \''+password+'\')')
conn.commit()

print("Inserted successfully.")

conn.close()
