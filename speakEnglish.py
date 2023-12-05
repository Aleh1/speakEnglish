#version 1 

import mysql.connector
import pyttsx3 

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
# вытягиваем слово из списка
word = ((myresult[0])[1])
# выводим результат
print(word)

# включаем озвучивание текста
converter = pyttsx3.init() 
# speed 
converter.setProperty('rate', 170) 
# Set volume 0-1 громкость
converter.setProperty('volume', 1) 
converter.say(word)   
converter.runAndWait() 