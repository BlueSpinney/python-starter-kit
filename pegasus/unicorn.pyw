
from tkinter import *
import string

main = Tk()
main.title("unicorn")

def unicorn(uni,unico):
    sup = 0
    uni = uni.strip('][').split(', ')
    unico = unico.strip('][').split(', ')
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
    

b1 = Button(main,text="decrypt",command=lambda : unicorn(e1.get(),e2.get()))    
inf = Label(main,text="key")
e1 = Entry(main)
inf2 = Label(main,text="salt")
e2 = Entry(main)
l1 = Label(main,text="")

b1.pack()
inf.pack()
e1.pack()
inf2.pack()
e2.pack()
main.mainloop()