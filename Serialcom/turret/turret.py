import cv2 as cv
import serial
import serial.tools.list_ports
import time
ports = serial.tools.list_ports.comports()

portlst = []

for port, desc, hwid in sorted(ports):
    portlst.append(port)
    print("{}: {} [{}]".format(port, desc, hwid))


arduino = serial.Serial(port=port, baudrate=115200, timeout=.1)

cap = cv.VideoCapture(0)
xcor = 0
ycor = 0
while True:
    ret,frame = cap.read()
    
    arduino.write(bytes(xcor,"utf-8"))
    time.sleep(0.05)
    arduino.write(bytes(ycor,"uft-8"))
    time.sleep(0.05)
    
    cv.imshow("frame",frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
