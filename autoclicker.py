from tkinter import *
import pyautogui
import time

count = 0

main = Tk()
pos = []

main.title = "auto click"
main.attributes("-topmost", True)
main.geometry("200x25")

def clicker():
    time.sleep(3)
    global pos,count
    if count == 0:
        print("hello")
        b1.configure(text="stop auto clicker")
        click()
        count = 1
    elif count == 1:
        b1.configure(text="start auto clicker")
        count = 0

def click():
    global count,pos
    pos = pyautogui.position()
    
    if count == 1:
        print("hi")
        pyautogui.click(pos)
    b1.after(10,click)
    
    

b1 = Button(main,text="start auto clicker",command=clicker)


b1.pack()
main.mainloop()
