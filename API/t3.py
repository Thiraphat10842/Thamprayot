import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pondpond",
  password="pond10842",
  database="pondpond"
)

mycursor = mydb.cursor()

sql = "UPDATE hard_ware SET status = 'OFF' WHERE name = 'B1'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record inserted.")