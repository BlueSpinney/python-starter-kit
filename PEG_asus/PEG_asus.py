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
    
def add(raw):
    global count,name,segments,timeframe
    if count == 0:
        b1.configure(text="add name")
        b1.pack_forget()
        e1.pack()
        b1.pack()
        
        count += 1
        
    elif count == 1:
        
        name = raw
        print(name)
        b1.configure(text="add segments")
        b1.pack_forget()
        e1.pack_forget()
        e1.delete(0,END)
        e1.pack()
        b1.pack()   
        count += 1
        
    elif count == 2:
        segments = raw 
        print(segments)
        b1.configure(text="add timeframe")
        b1.pack_forget()
        e1.pack_forget()
        e1.delete(0,END)
        e1.pack()
        b1.pack()   
        count += 1        

    elif count == 3:
        timeframe = raw 
        print(timeframe)
        b1.configure(text="add task")
        b1.pack_forget()
        e1.pack_forget()
        b1.pack()   
        
        print(name)
        print(segments)
        print(timeframe)
        
        task[len(task)] = ctask(name,segments,timeframe)
        for i in range(len(task)):
            t = task[i]
            



        
        name = ""
        segments = ""
        timeframe = ""
        count = 0          

tasks = Label(main,text="")
e1 = Entry(main)
b1 = Button(main,text="add task",command=lambda : add(e1.get()))


b1.pack()
main.mainloop()


