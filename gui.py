from tkinter import *
import random
import mysql.connector
import pyttsx3 
import random

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mynewpassword",
  database = "speakEnglish"
)

root=Tk()
root.geometry('750x750')
root.title('button')

label=Label(root,text='',font=('times',20)) #шрифт 


def roll():


    mycursor = mydb.cursor()
            # ввод в рандомном режиме
    value = random.randint(1,20)
            #print(value)
    input_namber = "select * from words where id =" + str(value) 
    mycursor.execute(input_namber)
    myresult = mycursor.fetchall()
            # вытягиваем слово из списка
    word = ((myresult[0])[1])
            
    print(word)
    
    dice = word 
    
    print(dice)
    label.configure(text=dice)
    label.pack()

    # включаем озвучивание текста
    converter = pyttsx3.init() 
            # speed 
    converter.setProperty('rate', 110) 
            # Set volume 0-1 громкость
    converter.setProperty('volume', 1) 
    converter.say(word)   
    converter.runAndWait()

button=Button(root,text="BUTTON", width=20, height=5, font=5, bg="PaleTurquoise",bd=2,command=roll)
#button=Button(root,text="lets roll...",)
button.pack(padx=10,pady=10)
root.mainloop()

# включаем озвучивание текста
##converter = pyttsx3.init() 
            # speed 
#converter.setProperty('rate', 110) 
            # Set volume 0-1 громкость
#converter.setProperty('volume', 1) 
#converter.say(dice)   
#converter.runAndWait()