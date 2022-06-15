from this import d
from anyio import run_async_from_thread
import mysql.connector

def con():
    mydb = mysql.connector.connect(
    host="localhost",
    user="pondpond",
    password="pond10842",
    database="pondpond"
    )
    return mydb

class Getdata:
    
    def getData():
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "SELECT * FROM users "

        mycursor.execute(sql)

        data = mycursor.fetchall()

        return data

    def getDataByID(ID):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "SELECT * FROM users WHERE ID = {} ".format(ID)

        mycursor.execute(sql)

        data = mycursor.fetchall()

        return data

    def insertHw(name, hw_name, status, value):

        mydb = con()
        mycursor = mydb.cursor(dictionary=True)

        sql = "INSERT INTO hard_ware (name, hw_name, status ,Value) VALUES ('{}', '{}', '{}', {})".format(name, hw_name, status, value)

        mycursor.execute(sql)

        mydb.commit()

        ID = mycursor.lastrowid

        return ID

    def updateHW(ID, status, value):
       
        mydb =con()
        mycursor = mydb.cursor(dictionary=True)

        sql = "UPDATE hard_ware SET status = '{}', value = {} WHERE ID = {}".format(status, value, ID)

        mycursor.execute(sql)

        mydb.commit()

        return True

    def deleteHW():
        mydb =con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "DELETE FROM hard_ware  WHERE id = 6"
        mycursor.execute(sql)
        mydb.commit()
        return True

        







