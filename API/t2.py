from multiprocessing.sharedctypes import Value
from unicodedata import name
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pondpond",
  password="pond10842",
  database="pondpond"
)

mycursor = mydb.cursor(dictionary=True)

sql = "INSERT INTO hard_ware (name, hw_name, status ,Value) VALUES ('A2', 'servo', 'OFF', 0.00)"

mycursor.execute(sql)

mydb.commit()

#ID = mycursor.lastrowid
#print("ID :" + ID)
print(mycursor.rowcount, "record inserted.")
