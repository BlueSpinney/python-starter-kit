from tkinter import *
import traceback

main = Tk()

# implement a save system

count = 0
name = ""
segments = ""
timeframe = ""
pb = '////////////////////////////////////////////////////////////////////////////////////////////////////'
oplst = []

task = {
    
}

class ctask:
    
    def __init__(self,pname,psegments,ptimeframe,plub,pro):
        self.name = pname
        self.segments = psegments
        self.timeframe = ptimeframe
        self.plub = plub
        self.pro = pro
    
    def finish_the_job(self):
        del self.name

    def returnSefl(self):
        arr = [self.name,self.segments,self.timeframe,self.plub,self.pro]

        return(arr)

def split(word):
    return [char for char in word]

def create(name,segments,timeframe):

    segments = int(segments)

    percent = 100 / segments
    return percent


    
def add(raw):
    global count,name,segments,timeframe,w

    print(variable.get())
    if variable.get() == "null":
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
            

            
            task[len(task)] = ctask(name,segments,timeframe,0,pb)
            
            for i in range(len(task)):
                t = task[i]
                if type(t.segments) != float:
                    one = create(name,t.segments,timeframe)
                    t.segments = one
                    print(f"t {i} is {t.returnSefl()}")
            
            lst = []
            for i in range(len(task)):
                t = task[i]
                tlst = t.returnSefl()
                lst.append(str(tlst[0]) + "\n")
                lst.append(str(tlst[1] * tlst[3]) + "%\n")
                tbar = tlst[4]
                tbar = split(tbar)
                for i in range(int(tlst[1] * tlst[3])):
                    tbar[i] = "#"
                    print(f"tbar is {tbar}")
                tbar = "".join(tbar)
                tlst[4] = tbar
                    
                lst.append(str(tlst[4]) + "\n")
                lst.append(str(tlst[2]) + "\n \n")
            lst = "".join(lst)

            tasks.configure(text=f"{lst}")
            tasks.pack()

            b1.pack()  
            

                
            
            w.destroy
            w = OptionMenu(main, variable, "null",*task)

            w.pack()
            name = ""
            segments = ""
            timeframe = ""
            count = 0    
    else:
        # add one      
        try:
            t = task[int(variable.get())]
            t.plub += 1
            lst = []
            for i in range(len(task)):
                try:
                    t = task[i]
                except:
                    t = task[i - 1]

                tlst = t.returnSefl()
                
                # delete self
                if int(tlst[1] * tlst[3]) == 100:
                    task[i] = task[len(task) - 1]
                    del task[len(task) - 1]
                    w.pack_forget()
                    w.destroy
                    print(*task)
                    w = OptionMenu(main, variable, "null",*task)

                    w.pack()
                    continue
                for i in range(int(tlst[1] * tlst[3])):
                    print(i)
                
                lst.append(str(tlst[0]) + "\n")
                lst.append(str(tlst[1] * tlst[3]) + "%\n")
                tbar = tlst[4]
                tbar = split(tbar)
                for i in range(int(tlst[1] * tlst[3])):
                    tbar[i] = "#"
                    print(f"tbar is {tbar}")
                tbar = "".join(tbar)
                tlst[4] = tbar
                    
                lst.append(str(tlst[4]) + "\n")
                lst.append(str(tlst[2]) + "\n \n")
            lst = "".join(lst)

            tasks.configure(text=f"{lst}")
            tasks.pack()
        except Exception as e:
            print(traceback.format_exc())

tasks = Label(main,text="")
e1 = Entry(main)
b1 = Button(main,text="add task",command=lambda : add(e1.get()))

variable = StringVar(main)
variable.set("null")

w = OptionMenu(main, variable, task)
b1.pack()
w.pack()

main.mainloop()


