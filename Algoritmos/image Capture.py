# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 10:14:24 2021

@author: tales
"""

import cv2
from functions_sem_outliers import calculoAU, EmotionMasculino, EmotionFeminino
import face_recognition
import csv

s = 0 

i = 0.
j = 0.

csvHeader = ['ID', 'Gender', 'EmotionNumber', 'Result']

f = open('ExpectedResults FEEDTUM M.csv', 'w', newline='', encoding='utf-8')

with open('ExpectedResults FEEDTUM M.csv', 'w', newline='') as file:
    
    writer = csv.writer(file)
    
    writer.writerow(csvHeader)

f.close() 

while(True):
    
    nome = input(print("Digite o nome do arquivo csv:"))
    
    f = open("/Users/tales/Desktop/Projeto_PIBIC/Bases Masculina/"+ nome + '.csv', 'r')
    
    try:
        reader = csv.reader(f, delimiter = ";")
        for line in reader:
            #line[0] -> ID, line[1] -> gender, line[2] -> folderName, line[3] -> emotionNumber
            #line[4l-> emotionName, line[5] -> AUs detectadas de acordo com o banco, 
            #line[6] ->file name neutra, line[7] ->file name ápice, line[8]-> não classificado
            if s > 0:
                
                #if line[2] == '10' or line[2] == '11' or line[2] == '12' or line[2] == '13':
            
                    #frameNeutro = cv2.imread("/Users/tales/Desktop/Projeto_PIBIC/extended-cohn-kanade-images/cohn-kanade-images" + "/" + str(line[0])+ "/0"+ str(line[2])+ "/"+ str(line[6]) + ".png")
            
                    #frameApice = cv2.imread("/Users/tales/Desktop/Projeto_PIBIC/extended-cohn-kanade-images/cohn-kanade-images" + "/" + str(line[0])+ "/0"+ str(line[2])+ "/"+ str(line[7]) + ".png")
                #else:
                Neutro = cv2.imread(str(line[3]) + ".jpg")
            
                Apice = cv2.imread(str(line[4]) + ".jpg")
                
                frameNeutro = Neutro[30:240, 55:250]
                
                frameApice = Apice[30:240, 55:250]
            
                
                #if (not line[8] == "X") and (not line[2] == "2") :
                result = calculoAU(frameNeutro, frameApice)
                    
                if not(EmotionMasculino(result) == None):
                    print(line[0], line[1], line[2], EmotionMasculino(result))
                        
                    l = open('ExpectedResults FEEDTUM M.csv', 'a', newline = '')
                    try:
                        writer = csv.writer(l, delimiter = ";")
                        writer.writerow((line[0], line[1], line[2], EmotionMasculino(result)))
                    finally:
                        l.close()
                        
                    if line[2] == str(EmotionMasculino(result)):
                        i = i + 1
                    j = j + 1  
                        
                    
                    
        
            
            s = s + 1 
            
    finally:
        f.close()
    break

print(i/j*100, '%')
















