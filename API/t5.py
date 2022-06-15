import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pondpond",
  password="pond10842",
  database="pondpond"
)

def getData():
    mycursor = mydb.cursor(dictionary=True)

    sql = "SELECT * FROM users "

    mycursor.execute(sql)

    data = mycursor.fetchall()

    return data

def DatabyID():
    mycursor = mydb.cursor(dictionary=True)

    sql = "SELECT * FROM users ID= 1".format(ID)

    mycursor.execute(sql)

    data = mycursor.fetchall()

    return data


