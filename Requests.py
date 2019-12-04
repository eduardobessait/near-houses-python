import mysql.connector

connection = mysql.connector.connect(host="localhost", user="Admin", passwd="Vush@w123")

query = connection.cursor()

query.execute("select * from urbiwise.users")

for user in query:
    print(user)