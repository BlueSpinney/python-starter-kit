from tkinter import *
import numpy

main = Tk()

count = 0
name = ""
segments = ""
timeframe = ""

task = {
    
}

class ctask:
    
    def __init__(self,pname,psegments,ptimeframe):
        self.name = pname
        self.segments = psegments
        self.timeframe = ptimeframe
    
    def delSelf(self):
        del self.name

    def returnSefl(self):
        arr = [self.name,self.segments,self.timeframe]

        return(arr)

def create(name,segments,timeframe):

    pb = '////////////////////////////////////////////////////////////////////////////////////////////////////'

    segments = int(segments)

    percent = 100 / segments
    return percent


    
def add(raw):
    global count,name,segments,timeframe
    if count == 0:
        b1.configure(text="add name")
        b1.pack_forget()
        w.pack_forget()
        e1.pack()
        b1.pack()
        w.pack()
        
        count += 1
        
    elif count == 1:
        
        name = raw
        print(name)
        b1.configure(text="add segments")
        b1.pack_forget()
        e1.pack_forget()
        w.pack_forget()
        e1.delete(0,END)
        e1.pack()
        b1.pack()   
        w.pack()
        count += 1
        
    elif count == 2:
        segments = raw 
        print(segments)
        b1.configure(text="add timeframe")
        b1.pack_forget()
        e1.pack_forget()
        w.pack_forget()
        e1.delete(0,END)
        e1.pack()
        b1.pack()   
        w.pack()
        count += 1        

    elif count == 3:
        timeframe = raw 
        print(timeframe)
        b1.configure(text="add task")
        b1.pack_forget()
        e1.pack_forget()
        w.pack_forget()
        

        
        task[len(task)] = ctask(name,segments,timeframe)
        lst = []
        for i in range(len(task)):
            t = task[i]
            tlst = t.returnSefl()
            lst.append(tlst[0] + "\n")
            lst.append(tlst[1] + "\n")
            lst.append(tlst[2] + "\n \n")
        lst = "".join(lst)

        tasks.configure(text=f"{lst}")
        tasks.pack()

        b1.pack()   
        w.pack()
            

        create(name,segments,timeframe)
        name = ""
        segments = ""
        timeframe = ""
        count = 0          

tasks = Label(main,text="")
e1 = Entry(main)
b1 = Button(main,text="add task",command=lambda : add(e1.get()))

variable = StringVar(main)
variable.set("null") # default value

w = OptionMenu(main, variable, "null")
b1.pack()
w.pack()

main.mainloop()


