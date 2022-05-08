import numpy as np
import cv2 as cv

green = [140, 7, 163]

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break
    
    cv.circle(frame, (400,300), 100,green,60)
    
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break


cap.release()
cv.destroyAllWindows()
