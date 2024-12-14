import mysql.connector

conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='maktabkhooneh')

cursor = conn.cursor(dictionary=True)
cursor.execute('SELECT * FROM employees order by height DESC, weight ASC')

result = cursor.fetchall()

for x in result:
  print(x["name"], x["height"], x["weight"])

conn.close()
