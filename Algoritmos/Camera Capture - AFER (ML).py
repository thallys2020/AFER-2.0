# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 23:06:24 2021

@author: tales
"""

import cv2
from functions import calculoAU, Anger, Hapiness, Surprise, Sadness, Fear, Disgust
import face_recognition
import pickle
import pandas as pd
import mysql.connector

"""banco = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "32331716",
        database = "afer"
)

cursor = banco.cursor()"""

model = input(print("Dgite qual modelo você quer usar: "))

modelo = open(str(model),'rb')

new = pickle.load(modelo)

modelo.close()

cap = cv2.VideoCapture(0)

while(True):
    #lê cada quadro do vídeo e carrega na varíavel frame
    _, frame = cap.read()
  
    cv2.imshow("Pressione S para Capturar a emocao Neutra",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('s'): #save on pressing 'y' 
        referencia = frame
        cv2.destroyAllWindows()
        break

cap.release()  

cap = cv2.VideoCapture(0)
i=0
while(True):
    #lê cada quadro do vídeo e carrega na varíavel frame
    _, frame = cap.read()
    
    #vid_fps = cap.get(cv2.CAP_PROP_FPS)
    if face_recognition.face_landmarks(frame):
        
        result = list(calculoAU(referencia, frame))
        
        entrada = [result]
        
        if new.predict(entrada)[0] == 1:
            a = "Raiva"
        elif new.predict(entrada)[0] == 3:
            a = "Nojo"
        elif new.predict(entrada)[0] == 4:
            a = "Medo"
        elif new.predict(entrada)[0] == 5:
            a = "Alegria"
        elif new.predict(entrada)[0] == 6:
            a = "Tristeza"
        elif new.predict(entrada)[0] == 7:
            a = "Surpresa"
        elif new.predict(entrada)[0] == 8:
            a = "Neutro"
        
        print(a)
        
        #comando_SQL = "INSERT INTO results (idresults, frame, emoção) VALUES (%s, %s, %s)"

        #dados = (i,i, a)

        #cursor.execute(comando_SQL, dados)

        #banco.commit()
    i=i+1  
    cv2.imshow("Captura",frame)
      
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() 

cv2.destroyAllWindows()