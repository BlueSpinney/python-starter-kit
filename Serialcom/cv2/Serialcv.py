import cv2
import numpy as np
import pyautogui
import time
import serial
import serial.tools.list_ports
ports = serial.tools.list_ports.comports()
for i in range(10):
    time.sleep(1)
    print(f"start in {10 - i}")

portlst = []
port = ""
duino = False
for port, desc, hwid in sorted(ports):
    portlst.append(port)
    print("{}: {} [{}]".format(port, desc, hwid))

if port != "":
    arduino = serial.Serial(port=port, baudrate=115200, timeout=.1)
    duino = True

count = 0

while True:
    print("searching")
    ss = pyautogui.screenshot()
    ss.save(r'D:\echairC\sadL.png')
    img_rgb = cv2.imread('sadL.png')
    template = cv2.imread('sadboy.png')
    w, h = template.shape[:-1]

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    threshold = .3
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]): 
        print("found")
        if count == 0 and duino == True:
            print("b")
            arduino.write(bytes("1","utf-8"))
            time.sleep(10)
        count += 1
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
    count = 0

    cv2.imwrite('result.png', img_rgb)

    time.sleep(0.1)
