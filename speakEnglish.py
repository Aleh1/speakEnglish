#version 1 

import mysql.connector
import pyttsx3 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mynewpassword",
  database = "speakEnglish"
)

while True:
    print('1 программа изучения слов')
    print('2 программа озвучивания текста')

    command = input('Выберите пункт: ')
    if command == '1':

        while True:
            mycursor = mydb.cursor()
            # ввод в ручном режиме
            username = input("Введите номер от 1 до 2: ")
            input_namber = "select * from words where id =" + username 
            mycursor.execute(input_namber)
            myresult = mycursor.fetchall()
            # вытягиваем слово из списка
            word = ((myresult[0])[1])
            # выводим результат
            print(word)

            # включаем озвучивание текста
            converter = pyttsx3.init() 
            # speed 
            converter.setProperty('rate', 110) 
            # Set volume 0-1 громкость
            converter.setProperty('volume', 1) 
            converter.say(word)   
            converter.runAndWait() 
    
    elif command == '2':
        #print('Находится в разработке')
        speak = input('Введите текст и нажмите Enter: ')
        # включаем озвучивание текста
        converter = pyttsx3.init() 
        # speed 50-3000
        converter.setProperty('rate', 70) 
        # Set volume 0-1 громкость
        converter.setProperty('volume', 1) 
        converter.say(speak)   
        converter.runAndWait() 
        break
    else:
        print('Вы ввели не правильное значение')