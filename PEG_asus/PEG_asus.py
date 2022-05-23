from tkinter import *
import traceback
from datetime import datetime
import webbrowser
import atexit
import time

main = Tk()

variable = StringVar(main)
variable.set("add task")

tasks = Label(main,text="")

pb = '////////////////////////////////////////////////////////////////////////////////////////////////////'

count = 0
name = ""
segments = ""
timeframe = ""
oplst = []

task = {
    
}

def split(word):
    return [char for char in word]

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

def startup():
    global tasks
    flst = []
    relst = []
    passer = 0
    with open("safe.txt","r") as safe:
        flst = safe.read()
        flst = flst.replace("'","")
        flst = flst.strip("][").split(', ')
    for i in range(len(flst)):
        con = flst[i]
        print(f"con is {con}")
        relst.append(con)
        if con.find("////////////////////////////////////////////////////////////////////////////////////////////////////") >= 0:
            relst = ", ".join(relst)
            relst = relst.strip("][").split(', ')
            
            print(f"final reanimatet list : {relst}")
            task[len(task)] = ctask(relst[0],float(relst[1]),relst[2],int(relst[3]),pb)
            print(task)
            relst = []

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
            
        if len(tlst[2]) > 3:
            ntlst = str(tlst[2])
            ntlst = split(ntlst)
            ntlst.insert(2,":")
            ntlst = "".join(ntlst)
        elif len(tlst[2]) > 2:
            ntlst = str(tlst[2])
            ntlst = split(ntlst)
            ntlst.insert(1,":")
            ntlst = "".join(ntlst)
        else:
            ntlst = tlst[2]
        lst.append(str(tlst[4]) + "\n")
        lst.append(str(ntlst) + "\n \n")
    lst = "".join(lst)

    tasks.configure(text=f"{lst}")
    tasks.pack()

        
    

startup()



    
    

def check_time():
    global task,tasks,w
    ct = datetime.now()
    print(ct)
    for i in range(len(task)):
        ct = datetime.now()
        try:
            ct = int(str(ct.hour) + str(ct.minute))
            print(f"acc ct : {ct}")
            t = task[i]
            t = t.timeframe
            t = int(t)
            if ct < t:
                continue
            else:
                # Serial comunication code comes here /////////////////////////////////////////////////////////////////////////////////////////
                task[i] = task[len(task) - 1]
                del task[len(task) - 1]
                w.pack_forget()
                w.destroy
                print(*task)
                w = OptionMenu(main, variable, "add task",*task)

                w.pack()
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
                        
                    if len(tlst[2]) > 3:
                        ntlst = str(tlst[2])
                        ntlst = split(ntlst)
                        ntlst.insert(2,":")
                        ntlst = "".join(ntlst)
                    elif len(tlst[2]) > 2:
                        ntlst = str(tlst[2])
                        ntlst = split(ntlst)
                        ntlst.insert(1,":")
                        ntlst = "".join(ntlst)
                    else:
                        ntlst = tlst[2]
                    lst.append(str(tlst[4]) + "\n")
                    lst.append(str(ntlst) + "\n \n")
                lst = "".join(lst)
                
                tasks.configure(text=f"{lst}")
                tasks.pack()
                for i in range(10):
                    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
                    time.sleep(0.1)
                continue                
            
        except Exception as e: 
            print(traceback.format_exc())
    main.after(1000,check_time)
        

def create(name,segments,timeframe):

    segments = int(segments)

    percent = 100 / segments
    return percent


    
def add(raw):
    global count,name,segments,timeframe,w

    print(variable.get())
    if variable.get() == "add task":
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
            e1.delete(0,END)

            
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
                    
                if len(tlst[2]) > 3:
                    ntlst = str(tlst[2])
                    ntlst = split(ntlst)
                    ntlst.insert(2,":")
                    ntlst = "".join(ntlst)
                elif len(tlst[2]) > 2:
                    ntlst = str(tlst[2])
                    ntlst = split(ntlst)
                    ntlst.insert(1,":")
                    ntlst = "".join(ntlst)
                else:
                    ntlst = tlst[2]
                lst.append(str(tlst[4]) + "\n")
                lst.append(str(ntlst) + "\n \n")
            lst = "".join(lst)

            tasks.configure(text=f"{lst}")
            tasks.pack()

            b1.pack()  
            

                
            
            w.destroy
            w = OptionMenu(main, variable, "add task",*task)

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
                    w = OptionMenu(main, variable, "add task",*task)

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
                    
                if len(tlst[2]) > 3:
                    ntlst = str(tlst[2])
                    ntlst = split(ntlst)
                    ntlst.insert(2,":")
                    ntlst = "".join(ntlst)
                elif len(tlst[2]) > 2:
                    ntlst = str(tlst[2])
                    ntlst = split(ntlst)
                    ntlst.insert(1,":")
                    ntlst = "".join(ntlst)
                else:
                    ntlst = tlst[2]
                lst.append(str(tlst[4]) + "\n")
                lst.append(str(ntlst) + "\n \n")
            lst = "".join(lst)

            tasks.configure(text=f"{lst}")
            tasks.pack()
        except Exception as e:
            print(traceback.format_exc())

check_time()
e1 = Entry(main)
b1 = Button(main,text="add",command=lambda : add(e1.get()))


w = OptionMenu(main, variable, "add task",*task)
b1.pack()
w.pack()


def the_last_dab():
    dab = []
    for i in range(len(task)):
        t = task[i]
        t = t.returnSefl()
        print(t)
        dab.append(t)
        
    print(dab)
    with open("safe.txt","w") as safe:
        safe.write(str(dab))


atexit.register(the_last_dab)
main.mainloop()


