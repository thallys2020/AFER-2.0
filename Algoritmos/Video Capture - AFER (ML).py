# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 19:14:08 2021

@author: tales
"""

import cv2
from functions import calculoAU, Anger, Hapiness, Surprise, Sadness, Fear, Disgust, EmotionMasculino
import face_recognition
import csv
import pickle
import pandas as pd

model = input(print("Dgite qual modelo você quer usar: "))

modelo = open(str(model),'rb')

new = pickle.load(modelo)

modelo.close()

cap = cv2.VideoCapture("Test Videos/S02/Happiness.mp4")

rval, referencia = cap.read()

while(True):
    _, frame = cap.read()

    if face_recognition.face_landmarks(frame):
           
        result = calculoAU(referencia, frame)
        
        entrada = [result]
        
        print(new.predict(entrada)[0])
           
    cv2.imshow("Captura",frame)
     
    if cv2.waitKey(17) & 0xFF == ord('q'):
        break

cap.release() 

cv2.destroyAllWindows()  
