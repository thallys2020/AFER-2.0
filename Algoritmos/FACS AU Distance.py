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
            
            
            if s > 1:
                Neutro = cv2.imread(str(line[3])+".jpg")
            
                Apice = cv2.imread(str(line[4])+".jpg")
            
            #Image Cropped
                frameNeutro = Neutro[30:240, 55:250]
            
                frameApice = Apice[30:240, 55:250]
            
            
            #emotion number : 1->anger // 2-> contempt // 3-> disgust // 4-> fear // 5-> happiness //
            #6-> sadness // 7-> surprise
            if line[2] == '1' and line[1] == 'M' and s > 1:
                anger = calculoAU(frameNeutro, frameApice)
                
                l = open('angerM FEEDTUM.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((anger))
                finally:
                   l.close()
                   
            elif line[2] == '1' and line[1] == 'F' and s > 1:
                anger = calculoAU(frameNeutro, frameApice)
                
                l = open('angerF FEEDTUM.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((anger))
                finally:
                   l.close()
                   
            elif line[2] == '2' and line[1] == 'M' and s > 1:
                emotion = calculoAU(frameNeutro, frameApice)
                l = open('contemptM FEEDTUM.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((emotion))
                finally:
                   l.close()
                   
            elif line[2] == '2' and line[1] == 'F' and s > 1:
                emotion = calculoAU(frameNeutro, frameApice)
                l = open('contemptF FEEDTUM.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((emotion))
                finally:
                   l.close()
                
            elif line[2] == '3' and line[1] == 'M' and s > 1:
                disgust = calculoAU(frameNeutro, frameApice)
                l = open('disgustM FEEDTUM.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((disgust))
                finally:
                   l.close()
                   
            elif line[2] == '3' and line[1] == 'F' and s > 1:
                disgust = calculoAU(frameNeutro, frameApice)
                l = open('disgustF FEEDTUM.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((disgust))
                finally:
                   l.close()
                
            elif line[2] == '4' and line[1] == 'M' and s > 1:
                fear = calculoAU(frameNeutro, frameApice)
                l = open('fearM FEEDTUM.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((fear))
                finally:
                   l.close()
            
            elif line[2] == '4' and line[1] == 'F' and s > 1:
                fear = calculoAU(frameNeutro, frameApice)
                l = open('fearF FEEDTUM.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((fear))
                finally:
                   l.close()
                
            elif line[2] == '5' and line[1] == 'M' and s > 1:
                happiness = calculoAU(frameNeutro, frameApice)
                l = open('happinessM FEEDTUM.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((happiness))
                finally:
                   l.close()
                   
            elif line[2] == '5' and line[1] == 'F' and s > 1:
                happiness = calculoAU(frameNeutro, frameApice)
                l = open('happinessF FEEDTUM.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((happiness))
                finally:
                   l.close()
                
            elif line[2] == '6' and line[1] == 'M' and s > 1:
                sadness = calculoAU(frameNeutro, frameApice)
                l = open('sadnessM FEEDTUM.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((sadness))
                finally:
                   l.close()
                   
            elif line[2] == '6' and line[1] == 'F' and s > 1:
                sadness = calculoAU(frameNeutro, frameApice)
                l = open('sadnessF FEEDTUM.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((sadness))
                finally:
                   l.close()
                
            elif line[2] == '7' and line[1] == 'M' and s > 1:
                surprise = calculoAU(frameNeutro, frameApice)
                l = open('surpriseM FEEDTUM.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((surprise))
                finally:
                   l.close()
                   
            elif line[2] == '7' and line[1] == 'F' and s > 1:
                surprise = calculoAU(frameNeutro, frameApice)
                l = open('surpriseF FEEDTUM.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((surprise))
                finally:
                   l.close()
                   
            s = s + 1
            
            print("Sucesso")
            
    finally:
        f.close()
    
    



    
     

