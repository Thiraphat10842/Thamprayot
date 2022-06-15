import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pondpond",
  password="pond10842",
  database="pondpond"
)

mycursor = mydb.cursor()

#sql = "SELECT * FROM name, hw_name, status, value, id FROM hard_ware"
sql = "SELECT * FROM hard_ware"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)