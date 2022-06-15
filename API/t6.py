import  mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="pondpond",
    password="pond10842",
    database="pondpond",
)
        
mycursor = mydb.cursor(dictionary=True)
sql = "SELECT * FROM hard_ware WHERE id = (SELECT MIN(id) FROM hard_ware)"
mycursor.execute(sql)
data = mycursor.fetchall()
mycursor.close()
mydb.close()
print (data)

    
