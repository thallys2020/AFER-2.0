# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 14:13:43 2021

@author: tales
"""
import cv2, numpy
from functions import calculoAU, EmotionMasculino, EmotionFeminino
import face_recognition
import pandas as pd


lista=[]
s=1

frameNeutro = cv2.imread("/Users/tales/Desktop/Projeto_PIBIC/extended-cohn-kanade-images/cohn-kanade-images" + "/" +'S011'+'/'+'003'+'/'+'S011_003_0000000' +str(s)+ ".png")

for s in range (1,15):
    print(s)

    if s > 9:
        frameApice = cv2.imread("/Users/tales/Desktop/Projeto_PIBIC/extended-cohn-kanade-images/cohn-kanade-images" + "/" +'S011'+'/'+'003'+'/'+'S011_003_000000' +str(s)+ ".png")
        result = calculoAU(frameNeutro, frameApice)
        lista.append(result)
    else:
        frameApice = cv2.imread("/Users/tales/Desktop/Projeto_PIBIC/extended-cohn-kanade-images/cohn-kanade-images" + "/" +'S011'+'/'+'003'+'/'+'S011_003_0000000' +str(s)+ ".png")
        result = calculoAU(frameNeutro, frameApice)
        lista.append(result)
        
print(lista)

lista = numpy.array(lista)

dataFrame = pd.DataFrame(lista)

print(dataFrame)

dataFrame.to_csv('Medo Feminino.csv')



