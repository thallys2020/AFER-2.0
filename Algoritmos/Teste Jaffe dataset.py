# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 15:41:26 2021

@author: tales
"""

import cv2
from functions import calculoAU, EmotionMasculino, EmotionFeminino
import face_recognition
import csv
import pickle



model = input(print("Dgite qual modelo você quer usar: "))

modelo = open(str(model),'rb')

new = pickle.load(modelo)

modelo.close()

s = 0 

i = 0.
j = 0.


while(True):
    
    nome = input(print("Digite o nome do arquivo csv:"))
    
    f = open(nome + '.csv', 'r')
    
    try:
        reader = csv.reader(f, delimiter = ";")
        for line in reader:
            #line[0] -> ID, line[1] -> gender, line[2] -> emotion number, line[3] -> file name neutro
            #line[4l-> file name ápice
            if s > 1:
                frameNeutro = cv2.imread(str(line[3])+ ".jpg")
                
                frameApice = cv2.imread(str(line[4])+".jpg")
                
                result = calculoAU(frameNeutro, frameApice)
                
                entrada = [result]
        
                print(line[0],line[2],new.predict(entrada)[0])
                    
                if line[2] == str(new.predict(entrada)[0]):
                    i = i + 1
                
                j = j + 1  
                        
            
            s = s + 1 
            
    finally:
        f.close()
    break

print(i/j*100, '%')