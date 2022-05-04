from ast import operator
import random
import os
from tkinter import *
import string




def startup():
    with open("key.txt","w") as key:
        key.write("")
main = Tk()
main.title("pegasus")
def pegasus(peg):
    randint = 0
    pegmax = 16
    alphabet = string.ascii_lowercase
    alphabet = list(alphabet)
    alphabet.append(" ")
    st = 0
    pegl = []
    enclst = []
    for i in range(len(peg)):
        pegl.append(peg[i])
    for i in range(len(pegl)):
        st = alphabet.index(pegl[i])
        randint = random.randint(0,len(alphabet) - st - 1)

        opjuge = random.randint(0,1)
        if opjuge == 0:
            print(randint)
            op = "P"
            st = alphabet.index(pegl[i])
            pegl[i] = alphabet[st + randint]
            with open("key.txt","a") as key:
                key.write(f"{st + randint},{randint},{op},")
            enclst.append(int(st + randint))
            enclst.append(int(randint))
            enclst.append(op)
        
        else:
            randint = random.randint(0,st)
            op = "s"
            st = alphabet.index(pegl[i])
            pegl[i] = alphabet[st - randint]
            with open("key.txt","a") as key:
                key.write(f"{st - randint},{randint},{op},")  
            enclst.append(int(st - randint))
            enclst.append(int(randint))
            enclst.append(op)
        l1.configure(text=enclst)
    print(f"youre key : {enclst}")

    
def Anihalate():
    with open("key.txt","w") as key:
        key.write("")

b1 = Button(main,text="encrypt",command= lambda : pegasus(e1.get()))
b2 = Button(main,text="delete",command = Anihalate)
e1 = Entry(main)

l1 = Label(main)

b1.pack()
e1.pack()
l1.pack()
b2.pack()

main.mainloop()