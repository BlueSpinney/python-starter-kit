

from tkinter import *
import string

main = Tk()
main.title("unicorn")


def moveval(index,newindex,arr):
    oldv = arr[index]
    oldv2 = arr[newindex]
    
    for i in range(len(arr)):
        if i == newindex:
            arr[i] = int(arr[i])
            arr[i] = oldv
        if i == index:
            arr[i] = oldv2
    
    return arr

def unicorn(uni,unico,unicorn):
    unicorn = unicorn.strip('][').split(', ')
    uni = uni.strip('][').split(', ')
    unico = unico.strip('][').split(', ')
    for i in range(len(unicorn) - 1):
        uni = moveval(int(unicorn[i + 1]),int(unicorn[i]),uni)
    
    
    
    
    sup = 0
    print(unico)
    if unico != ['']:
        for each in range(len(unico ) - sup):
            print(unico[each])
            print(f"removed : {uni[int(unico[each]) - sup]} {uni[int(unico[each]) + 1- sup]} {uni[int(unico[each]) + 2- sup]}")
            del uni[(int(unico[each]) - sup)]
            print(uni)
            del uni[(int(unico[each])- sup)]
            print(uni)
            del uni[(int(unico[each])- sup)]
            sup = sup + 3
        print(uni)

    count = 0
    alphabet = string.ascii_lowercase
    alphabet = alphabet + " "
    realletter = ""
    realletterl = []
    for i in range(len(uni)):
        print(uni[i])
        if count == 0:
            pointer2 = uni[i]
            pointer2 = int(str(pointer2))
            count += 1
        elif count == 1:
            pointer = uni[i]
            pointer = int(str(pointer))
            count += 1    
        elif count == 2:
            if uni[i] == "'P'":
                realletter = alphabet[pointer2 - pointer]
            elif uni[i] == "'s'":
                realletter = alphabet[pointer2 + pointer]
            
            realletterl.append(realletter)
            
            count = 0
            l1.configure(text="the message is : {}".format("".join(realletterl)))
            l1.pack()
    

b1 = Button(main,text="decrypt",command=lambda : unicorn(e1.get(),e2.get(),e3.get()))    
inf = Label(main,text="key")
e1 = Entry(main)
inf2 = Label(main,text="salt")
e2 = Entry(main)
inf3 = Label(main,text="hash")
e3 = Entry(main)
l1 = Label(main,text="")

b1.pack()
inf.pack()
e1.pack()
inf2.pack()
e2.pack()
inf3.pack()
e3.pack()
main.mainloop()
