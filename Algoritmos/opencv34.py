# -*- coding: utf-8 -*-
"""
Created on Wed May 15 12:28:39 2019

@author: tales
"""

import numpy as np
import cv2
from PIL import Image, ImageDraw
import face_recognition

    
cap = cv2.VideoCapture("Anger.mp4")

vid_fps = cap.get(cv2.CAP_PROP_FPS)

frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

print(vid_fps, frame_count)

i = 0

while(True):
    #lê cada quadro do vídeo e carrega na varíavel frame
    _, frame = cap.read()
    
    
    cv2.imshow("frame",frame)
    
    i = i + 1
    
    print(i)
    
    if cv2.waitKey(1)&0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
    
    
        
  
        
        
        