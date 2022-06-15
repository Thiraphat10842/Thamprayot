from getData import Getdata

name = input("name")
hw_name = input("hw_name")
status = input("status")
value = input("value")

data = Getdata.insertHw(name, hw_name, status, value)
#print(f"ID {ID}")



#data =Getdata. updateHW(id, status, value)

#data = Getdata.getDataByID(ID)

print (data)

