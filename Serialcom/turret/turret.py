import cv2
import sys
import serial
import serial.tools.list_ports
import time
from tkinter import *
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
ports = serial.tools.list_ports.comports()

portlst = []
duino = False
port = ""
y = input()

if y == "n":
    exit()

for port, desc, hwid in sorted(ports):
    portlst.append(port)
    print("{}: {} [{}]".format(port, desc, hwid))
    port = port

if bool(port) != False:
    arduino = serial.Serial(port=port, baudrate=115200, timeout=.1)
    duino = True

cascPath = r'C:\Users\Jerome\Desktop\python\turret\haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

st = 0

while True:
    now = datetime.now()
    curlst = []
    rc = ['','']

    current_time = now.strftime("%H:%M:%S")
    for i in range(len(current_time)):
        curlst.append(current_time[i])
    rc[0] = curlst[len(curlst) - 1]
    rc[1] = curlst[len(curlst) - 2]
    rc = rc[::-1]
    print(f"{curlst}")
    print(f"the current seconds{rc}")
    intrc = "".join(rc)
    intrc = int(intrc)
    print(f"current start time {st}")

    if intrc - 2== st or intrc < st:
        duino = True


    xcor = 0
    ycor = 0
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        print(f"the x y coardinates are {x} {y}")
        xcor = x
        ycor = y
    xcor = xcor / 500
    xcor = xcor * 180
    ycor = ycor / 300
    ycor = ycor * 180  
    xcor = int(xcor)
    ycor = int(ycor)
    corlst = [xcor,ycor]
    print(f"the x y coardinates are {corlst}")  
    if xcor > 180 or ycor > 180:
        continue
    if duino == True:
        arduino.write(bytes(str(corlst),"utf-8"))
        duino = False
        st = int("".join(rc))



    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
