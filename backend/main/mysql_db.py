import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="207455",
  port="3306",
  auth_plugin="mysql_native_password"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE db_drf_api")