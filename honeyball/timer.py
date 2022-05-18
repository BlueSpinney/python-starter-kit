from tkinter import *

from pynput import keyboard


last_key = ""
time = [0,0,":",0,0,":",0,0]
strlst = []
i = 0

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
            
            global i,strlst,time
            if i > len(time) - 1:
                i = 0
                strlst = []
                time = [0,0,":",0,0,":",0,0]
            print("hi")
            k = event.char
            if k == "backspace":
                i -= 1
                time[i] = 0
            if time[i] == ":":
                i += 1
            time[i] = k
            i += 1

            for l in range(len(time)):
                strlst.append(str(time[l]))
            t1.configure(text="".join(strlst[::-1]))
            t1.pack()
            strlst = []


        main.attributes("-topmost", True)

        main.bind('<Key>',input)
        
        t1 = Label(main,text="")


        main.mainloop()



    last_key = k

    

    print(k)
    print(last_key)
    

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join() 
