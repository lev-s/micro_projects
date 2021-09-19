#github.com/lev-s

#Install cv2(OpenCV) and pyAutoGUI packages before using

#cmd code to install cv2:
#py -m pip install opencv-python

#cmd code to install pyautogui:
#py -m pip install pyautogui

##################################################################

import cv2
import numpy as np
import pyautogui

SCREEN_SIZE = (1920, 1080)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("ouput.avi", fourcc, 20.0, (SCREEN_SIZE))

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    #if user clicks q, it exits
    if cv2.waitKey(1) == ord("q"):
        break
    
cv2.destroyAllWindows()
out.release()   