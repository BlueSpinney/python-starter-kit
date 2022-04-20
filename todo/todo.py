from tkinter import *
import linecache
from tracemalloc import start

lines = 0
count = 1
empty = ""
tlist = []
rt = ""
num = []
ltlist= []

tasks = {}

main = Tk()
l1 = Label(main,text=rt)



def startup():
    global lines,count,empty,tlist,rt,num,ltlist
    lines = []
    with open('safe.txt') as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        count += 1
        num.append(count)
        print(f'line {count}: {line}')  
        tasks["line " + str(count)] = f'{line}'


    count = 0
    while True:
        try:
            count += 1
            tlist.append(tasks["line " + str(count)])
        except Exception as e:
            print(e)
            break

    rt = empty.join(tlist)
    l1.configure(text="")
    l1.configure(text=rt)
    ltlist = tlist
    print(f"last T list : {ltlist}")
    rt = ""
    tlist = []
    
startup()
    

def createTask():
    task = e1.get()
    with open('safe.txt','a') as f:
        f.write('\n  ' + task + '  ')
    startup()
def deleteTask():
    global lines,count,empty,tlist,rt,num,ltlist
    
    print(f"last T list : {ltlist}")
    ltlist.pop(len(ltlist) - 1)
    rt = empty.join(ltlist)
    l1.configure(text="")
    l1.configure(text=rt)
    with open('safe.txt','w') as f:
        f.write("".join(ltlist))

        
    
    

    
b1 = Button(main,text="create task",command=createTask)
b2 = Button(main,text="remove task",command=deleteTask)

e1 = Entry(main)


l1.pack()
b1.pack()
b2.pack()
e1.pack()
main.mainloop()