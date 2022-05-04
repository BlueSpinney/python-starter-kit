
from tkinter import *
import string

main = Tk()
main.title("unicorn")

def unicorn(uni):
    uni = uni.strip('][').split(', ')

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
    

b1 = Button(main,text="decrypt",command=lambda : unicorn(e1.get()))
e1 = Entry(main)
l1 = Label(main,text="")

b1.pack()
e1.pack()
main.mainloop()