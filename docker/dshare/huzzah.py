import mysql.connector

hhh = mysql.connector.connect(user="root", host="localhost")
print("No error on sql connect")
print(hhh)
