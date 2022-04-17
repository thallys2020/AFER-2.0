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


while(True):
    
    nome = input(print("Digite o nome do arquivo csv:"))
    
    f = open(nome + '.csv', 'r')
    
    try:
        reader = csv.reader(f, delimiter = ";")
        for line in reader:
            #line[0] -> ID, line[1] -> gender, line[2] -> folderName, line[3] -> emotionNumber
            #line[4l-> emotionName, line[5] -> AUs detectadas de acordo com o banco, 
            #line[6] ->file name neutra, line[7] ->file name ápice, line[8]-> não classificado
            if s > 1:
                
                frameNeutro = cv2.imread("/Users/tales/Desktop/Projeto_PIBIC/jaffedbase"+"/"+str(line[0])+"/"+str(line[3])+ ".tiff")
                
                frameApice = cv2.imread("/Users/tales/Desktop/Projeto_PIBIC/jaffedbase"+"/"+str(line[0])+"/"+str(line[4])+".tiff")
                
               
                result = calculoAU(frameNeutro, frameApice)
                    
                if not(EmotionFeminino(result) == None):
                    print(line[0], line[2], EmotionFeminino(result))
                        
                                              
                    if line[2] == str(EmotionFeminino(result)):
                        i = i + 1
                    j = j + 1  
                        
                    
                    
        
            
            s = s + 1 
            
    finally:
        f.close()
    break

print(i/j*100, '%')
















