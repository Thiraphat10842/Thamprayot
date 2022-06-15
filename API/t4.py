import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pondpond",
  password="pond10842",
  database="pondpond"
)

mycursor = mydb.cursor()

sql = "DELETE FROM hard_ware WHERE id = 4"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record inserted.")