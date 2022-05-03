
import serial
from tkinter import *
import serial.tools.list_ports
import time
ports = serial.tools.list_ports.comports()

portlst = []

for port, desc, hwid in sorted(ports):
    portlst.append(port)
    print("{}: {} [{}]".format(port, desc, hwid))


arduino = serial.Serial(port=port, baudrate=115200, timeout=.1)

main = Tk()

menu= StringVar()
menu.set("Select a port")

count = 0
def sendsimp():
    global count,menu
    print(menu.get())
    arduino = serial.Serial(port=menu.get(), baudrate=115200, timeout=.1)
    if count == 0:
        count = 1
        b1.configure(text="send simple off")
        arduino.write(bytes("1","utf-8"))
    elif count == 1:
        count = 0
        b1.configure(text="send simple on")
        arduino.write(bytes("0","utf-8"))
    time.sleep(0.5)

def send_string(strin):
    arduino = serial.Serial(port=menu.get(), baudrate=115200, timeout=.1)
    arduino.write(bytes(strin,"utf-8"))
    time.sleep(0.5)

b1 = Button(main,text="send simple on",command=sendsimp)
b2 = Button(main,text="send string",command= lambda : send_string(e1.get()))
e1 = Entry(main)
com = OptionMenu(main,menu,*portlst)

b1.pack()
b2.pack()
com.pack()
e1.pack()

main.mainloop()
