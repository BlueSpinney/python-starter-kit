# Importing Libraries
import serial
import time
from tkinter import *

main = Tk()
arduino = serial.Serial(port='COM9', baudrate=115200, timeout=.1)

main.geometry('1480x1020')
main.configure(bg="black")
main.title("hannes ist cool")

def on():
    print("hi mom")
    arduino.write(bytes("1", 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

def off():
    print("hi mom")
    arduino.write(bytes("0", 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data    

b1 = Button(main,text="pogchamp",command=on,height= 30, width=80)
b2 = Button(main,text="poggers",command=off,height= 30, width=80)

b2.place(x=827,y=100)
b1.place(x=170,y=100)


main.mainloop()
