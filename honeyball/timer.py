from tkinter import *

from pynput import keyboard
import logging
import threading



last_key = ""
time = [0,0,":",0,0,":",0,0,""]
strlst = []
i = 0
eventlst = ["|"]

def merge(time,eventlst):
    pointer = 0
    eventlst[::-1]
    
    for l in range(len(eventlst)):
        print(time[l])
        if time[l] == ":" or l == 4:
            pointer += 1
            time[pointer] = eventlst[l]
            if l == 4:
                pointer -= 1
        else:
            time[pointer] = eventlst[l]

        pointer += 1

def on_press(key):
    global last_key,time
    if key == keyboard.Key.esc:
        return False 
    try:
        k = key.char
    except:
        k = key.name
    combo = last_key + k

    if combo == "alt_l4":
        main = Tk()
        
        def input(event):
            k = event.char
            
            global i,strlst,time,eventlst

            eventlst.insert(0,k)
            print(eventlst)
            if i > len(time) - 1:
                i = 0
                strlst = []
                time = [0,0,":",0,0,":",0,0]

            if k == "backspace":
                i -= 1
                eventlst[i] = 0


            merge(time,eventlst)
            try:
                time[i] = time[i]

            except:
                i = 0
                print("stack overflow")

            for l in range(len(time)):
                strlst.append(str(time[l]))
            t1.configure(text="".join(strlst[::-1]))
            t1.pack()
            b1.pack()
            strlst = []

        def start(timelst):
            timelst = timelst[::-1]
            for l in range(len(timelst) - 1):
                if timelst[l] == "|":
                    timelst[l] = 0
                if timelst[l] == '':
                    timelst.pop(l)
            print(f"time lst 1{timelst}")

            constlst = []
            finconst = []
            for l in range(len(timelst)):
                try:
                    if timelst[l + 1]== ":":
                        finconst.append(constlst)
                        timelst = []
                    
                    constlst.append(timelst[l])
                except:
                    finconst.append(constlst)
                    timelst = []    
            finconst = finconst[::-1]
            ti = 0
            
            for l in range(len(finconst)): 
                templst = finconst[l]
                tempt = "".join(str(templst))
                tempt = int(tempt)
                if l == 0:
                    ti += l
                if l == 1:
                    ti += l * 60
                if l <= 2:
                    ti += l * 600
                event = threading.Event()
                for l in range(ti):
                    event.wait(1)
                    print(l)
                    
                    


        main.attributes("-topmost", True)

        main.bind('<Key>',input)
        
        t1 = Label(main,text="")
        b1 = Button(main,text="start timer",command=lambda : start(time))


        main.mainloop()
        last_key = ""
        time = [0,0,":",0,0,":",0,0]
        strlst = []
        i = 0
        eventlst = []



    last_key = k

    

    

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join() 
