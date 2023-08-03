import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost', 
	user = 'root',
	passwd = 'strangeevil123',

	)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE eldenring")

print("All Done!")