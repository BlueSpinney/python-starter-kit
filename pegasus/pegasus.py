from ast import operator
import random
import os
from tkinter import *
import string

def move(val,pos,array):
    oldarr = array
    newarr = []
    for i in range(len(array)):
        if pos == i:
            newarr.append(val)
        newarr.append(oldarr[i])    
    return newarr

def moveval(index,newindex,arr):
    oldv = arr[index]
    oldv2 = arr[newindex]
    
    for i in range(len(arr)):
        if i == newindex:
            arr[i] = oldv
        if i == index:
            arr[i] = oldv2
    
    return arr


def startup():
    with open("key.txt","w") as key:
        key.write("")
main = Tk()
main.title("pegasus")
def pegasus(peg):
    randint = 0
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
    hash(enclst)

def hash(lst):
    hashpack = []
    hash = []
    for i in range(len(lst)):
        rand = random.randint(0,len(lst) - 1)
        if random.randint(0,3) == 3:
            lst = moveval(i,rand,lst)
            hash.append(i)
            hash.append(rand)
    print(f"hash list : {hash}")
        
    
    
    salt(lst,hash)

def salt(lst,hash):
    saltlst = []
    REE = 0
    for BEE in range(int(len(lst) / 3)):
        REE = REE + 3
        if random.randint(0,5) != 1:
            ch = random.randint(0,1)
            fnum = random.randint(0,27)
            fval = random.randint(0,16)
            if ch == 0:
                fop = "P"
                lst.insert(REE,fnum + fval)
                lst.insert(REE + 1,fval)
                lst.insert(REE + 2,fop)
                print(ch)
                saltlst.append(REE)
            elif ch ==1:
                fop = "s"
                lst.insert(REE,fnum - fval)
                lst.insert(REE + 1,fval)
                lst.insert(REE + 2,fop)
                print(ch)
                saltlst.append(REE)
    print(f"youre saltet key : {lst}")
    print(f"youre salt : {saltlst}")
    print(f"youre hash : {hash}")
            
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
