from tkinter import *
import os
from turtle import st


o_prol = 1

progressl = [":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",]

main = Tk()

def getgoal():
    global goal
    goal = e2.get()
    with open("safe.txt","w") as safe_file:
        safe_file.write(goal)
    startup()
    
def add():
    with open("safepro.txt","r") as safe_file:
        integer = safe_file.read()
        integer = int(integer)
        integer = integer + int(e1.get())
        integer = str(integer)

    with open("safepro.txt","w") as safe_file:
        safe_file.write(integer)
    startup()

progressbar = Label(main,text="")
progressinper = Label(main,text="")
proinbr = Label(main,text="")

l1 = Label(main,text="add")
e1 = Entry(main,bd=2)
l2 = Label(main,text="set goal")
e2 = Entry(main,bd=2)

b1 = Button(main,text="add",command=add)
b2 = Button(main,text="set goal",command=getgoal)

file_path = os.path.realpath(__file__)
serch = len(file_path) - 9
file_path = file_path[0:serch]
goal = 0

progress = 0
opro = 0
def startup():

    global goal,progress,opro,o_prol,progressl
    
    with open("safe.txt","r") as safe_file:
        goal = safe_file.read()
    if (goal != ""):
        try:
            goal = int(goal)

        except:
            with open("safe.txt","w") as safe_file:
                safe_file.write("please enter a valid int as goal \n(not float or string) old value (" + str(goal) + ")")
            os.chdir(file_path)
            os.system('cmd /k "safe.txt && exit"')
            
        with open("safepro.txt","r") as safe_file:
            progress = int(safe_file.read())
            opro = progress
            progress = progress / goal
            progress = progress * 100
            progress = int(progress)
            for i in range(progress):
                o_prol = i
                progressl[i] = "/"
            o_prol = o_prol + 1
            while True:
                if progress == 0:
                    progressl = [":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",":",]
                    break
                try:
                    progressl[o_prol] = ":"
                    o_prol = o_prol + 1
                except:
                    break
            print(progressl)
            print(len(progressl))
                

    progressbar.configure(text="".join(progressl))
    progressinper.configure(text=str(progress) + " %")
    proinbr.configure(text=str(opro) + "/" + str(goal)) 

    progressbar.pack()
    progressinper.pack()
    proinbr.pack()
    
    l1.pack()
    e1.pack()
    l2.pack()
    e2.pack()

    b1.pack()
    b2.pack()
                
                
                
        
            
    
startup()


main.mainloop()