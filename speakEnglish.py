#version 1 

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mynewpassword",
  database = "speakEnglish"
)

mycursor = mydb.cursor()
# ввод в ручном режиме
username = input("Введите номер от 1 до 2: ")
input_namber = "select  * from words where id =" + username 
mycursor.execute(input_namber)
myresult = mycursor.fetchall()
word = ((myresult[0])[1])
# выводим результат
print(word)