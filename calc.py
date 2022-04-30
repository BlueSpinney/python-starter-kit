from tkinter import *


main = Tk()

num_and_for = []

empt_pos = {
    
}

def calculate(formula):
    empty = 0
    print(f"the formula is : {formula} ")
    for i in range(len(formula)):
        if formula[i] == " ":
            empty += 1
            num_and_for.append(formula[i - 1:i])
            empt_pos["empt space " + str(empty)] = [i - 1,i + 1]
    print(f"full list of empty spaces in formula : {empt_pos}")
    print(f"full list of characters between empty :  {num_and_for}")
    

e1 = Entry(main,bd=1)
b1 = Button(main,text="calculate",command= lambda : calculate(formula=e1.get()))

e1.pack()
b1.pack()
main.mainloop()
