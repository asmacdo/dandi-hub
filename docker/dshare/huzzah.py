# This can be used to prove connection
# pip install mysql-connector-python
import mysql.connector

hhh = mysql.connector.connect(user="root", password="tutorial", host="localhost")
print("No error on sql connect")
print(hhh)
