from tkinter import *


main = Tk()

num_and_for = []
Oplace = 0
opt = False
operators = ["+", "-", "*", "/"]
calcl = []
empt_pos = {
    
}

def calculate(stri):
    global Oplace,opt,num_and_for
    empty = 0
    Oplace = 0
    num_and_for = []
    solution = 0
    print(f"the formula is : {str} ")
    for i in range(len(stri)):
        if stri[i] == " ":
            empty += 1
            num_and_for.append(stri[Oplace:i])
            empt_pos["empt space " + str(empty)] = [i - 1,i + 1]
            Oplace = i
    print(f"full list of empty spaces in String : {empt_pos}")
    print(f"full list of words in String :  {num_and_for}")
    solution = eval("".join(num_and_for))
    print(f"the solution is {solution}")
    return solution , num_and_for


        
e1 = Entry(main,bd=1)
b1 = Button(main,text="calculate",command= lambda : calculate(stri=e1.get() + " "))

e1.pack()
b1.pack()
main.mainloop()
