# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 19:14:08 2021

@author: tales
"""

import cv2
from functions import calculoAU, Anger, Hapiness, Surprise, Sadness, Fear, Disgust, EmotionMasculino, EmotionFeminino
import face_recognition
import csv

csvHeader = ['Emotion', 'Frame']

csvHeader2= ['Frame','AU1Variation', 'AU11Variation', 'AU21Variation', 'AU22Variation', 'AU4Variation', 'AU51Variation', 'AU52Variation', 'AU61Variation', 'AU62Variation', 'AU91Variation', 'AU92Variation', 'AU10Variation', 'AU12Variation', 'AU151Variation', 'AU152Variation', 'AU17Variation', 'AU20Variation', 'AU23Variation', 'AU24Variation', 'AU25Variation', 'AU26Variation', 'AU27Variation']

f = open('S05MAnger.csv', 'w', newline='', encoding='utf-8')

with open('S05MAnger.csv', 'w', newline='') as file:
    
    writer = csv.writer(file)
    
    writer.writerow(csvHeader)

f.close() 

f = open('S05MAnger.csv', 'w', newline='', encoding='utf-8')

with open('S05MAngerAUs.csv', 'w', newline='') as file:
    
    writer = csv.writer(file)
    
    writer.writerow(csvHeader2)

f.close() 

f = open('S05MAngerLandmarks.csv', 'w', newline='', encoding='utf-8')


cap = cv2.VideoCapture("Test Videos/S05/Anger.mp4")

rval, referencia = cap.read()

vid_fps = cap.get(cv2.CAP_PROP_FPS)

frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

print(vid_fps, frame_count)

i = 0 

while(True):
    #lê cada quadro do vídeo e carrega na varíavel frame
    _, frame = cap.read()
    
    i = i + 1 

    #vid_fps = cap.get(cv2.CAP_PROP_FPS)
    if face_recognition.face_landmarks(frame):
        
        r = open('S05MAngerLandmarks.csv', 'a', newline = '')
        try:
            writer = csv.writer(r, delimiter = ";")
            writer.writerow((i,face_recognition.face_landmarks(frame)))
        finally:
            r.close()
        
        result = calculoAU(referencia, frame)
        
        a = EmotionFeminino(result)
        
        if a == None:
            a = 'NEUTRAL'
        if a == 1:
            a = 'ANGER'
        if a == 3:
            a = 'DISGUST'
        if a == 4:
            a = 'FEAR'
        if a == 5:
            a = 'HAPPINESS'
        if a == 6:
            a = 'SADNESS'
        if a == 7:
            a = 'SURPRISE'
            
        
        print(a,i)
        
        l = open('S05MAnger.csv', 'a', newline = '')
        try:
            writer = csv.writer(l, delimiter = ";")
            writer.writerow((a,i))
        finally:
            l.close()
            
        f = open('S05MAngerAUs.csv', 'a', newline = '')
        try:
            writer = csv.writer(f, delimiter = ";")
            writer.writerow((i,result))
        finally:
            l.close()
            
    cv2.imshow("Captura",frame)
    
    cv2.imwrite('Frames5M/Anger/frame '+str(i)+".png", frame)
    
    
    if cv2.waitKey(17) & 0xFF == ord('q'):
        break

cap.release() 

cv2.destroyAllWindows()  
