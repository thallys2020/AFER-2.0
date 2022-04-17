# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 09:57:35 2021

@author: tales
"""


import cv2
import csv
from functions import calculoAU



s = 0

while(True):
    
    nome = input(print("Digite o nome do arquivo csv:"))
    
    f = open(nome + '.csv', 'r')
    
    try:
        reader = csv.reader(f, delimiter = ";")
        for line in reader:
            #line[0] -> ID, line[1] -> gender, line[2] -> folderName, line[3] -> emotionNumber
            #line[4l-> emotionName, line[5] -> AUs detectadas de acordo com o banco, 
            #line[6] ->file name neutra, line[7] ->file name ápice, line[8]-> não classificado
            
            print(line)
            
            if line[2] == '10' or line[2] == '11' or line[2] == '12' or line[2] == '13':
            
                frameNeutro = cv2.imread("/Users/tales/Desktop/Projeto_PIBIC/extended-cohn-kanade-images/cohn-kanade-images" + "/" + str(line[0])+ "/0"+ str(line[2])+ "/"+ str(line[6]) + ".png")
            
                frameApice = cv2.imread("/Users/tales/Desktop/Projeto_PIBIC/extended-cohn-kanade-images/cohn-kanade-images" + "/" + str(line[0])+ "/0"+ str(line[2])+ "/"+ str(line[7]) + ".png")
            else:
                frameNeutro = cv2.imread("/Users/tales/Desktop/Projeto_PIBIC/extended-cohn-kanade-images/cohn-kanade-images" + "/" + str(line[0])+ "/00"+ str(line[2])+ "/"+ str(line[6]) + ".png")
            
                frameApice = cv2.imread("/Users/tales/Desktop/Projeto_PIBIC/extended-cohn-kanade-images/cohn-kanade-images" + "/" + str(line[0])+ "/00"+ str(line[2])+ "/"+ str(line[7]) + ".png")
            
            #emotion number : 1->anger // 2-> contempt // 3-> disgust // 4-> fear // 5-> happiness //
            #6-> sadness // 7-> surprise
            if s > 1 and not(line[9] == "X"):
                neutro = calculoAU(frameNeutro, frameApice)
                
                l = open('NeutroF.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((neutro))
                finally:
                   l.close()
                   
                   
            s = s + 1
            
            print("Sucesso")
            
    finally:
        f.close()
    
    



    
     

