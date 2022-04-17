# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 22:58:51 2021

@author: tales
"""

import cv2
import numpy as np
import face_recognition

imagem = cv2.imread("6.png")

face_landmarks_list_apice = face_recognition.face_landmarks(imagem)

vermelho = (0,0,255)
#Pontos 
cv2.circle(imagem,(face_landmarks_list_apice[0]['left_eyebrow'][4][0], face_landmarks_list_apice[0]['left_eyebrow'][4][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['left_eye'][3][0], face_landmarks_list_apice[0]['left_eye'][3][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['right_eyebrow'][0][0], face_landmarks_list_apice[0]['right_eyebrow'][0][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['right_eye'][0][0], face_landmarks_list_apice[0]['right_eye'][0][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['left_eyebrow'][1][0], face_landmarks_list_apice[0]['left_eyebrow'][1][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['left_eye'][3][0], face_landmarks_list_apice[0]['left_eye'][3][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['right_eyebrow'][3][0], face_landmarks_list_apice[0]['right_eyebrow'][3][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['right_eye'][0][0], face_landmarks_list_apice[0]['right_eye'][0][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['left_eyebrow'][4][0], face_landmarks_list_apice[0]['left_eyebrow'][4][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['right_eyebrow'][0][0], face_landmarks_list_apice[0]['right_eyebrow'][0][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['left_eye'][2][0], face_landmarks_list_apice[0]['left_eye'][2][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['left_eye'][4][0], face_landmarks_list_apice[0]['left_eye'][4][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['right_eye'][1][0], face_landmarks_list_apice[0]['right_eye'][1][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['right_eye'][5][0], face_landmarks_list_apice[0]['left_eye'][5][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['left_eyebrow'][4][0], face_landmarks_list_apice[0]['left_eyebrow'][4][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['nose_tip'][0][0], face_landmarks_list_apice[0]['nose_tip'][0][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['right_eyebrow'][0][0], face_landmarks_list_apice[0]['right_eyebrow'][0][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['nose_tip'][4][0], face_landmarks_list_apice[0]['nose_tip'][4][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['top_lip'][3][0], face_landmarks_list_apice[0]['top_lip'][3][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['nose_tip'][2][0], face_landmarks_list_apice[0]['nose_tip'][2][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['top_lip'][0][0], face_landmarks_list_apice[0]['top_lip'][0][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['top_lip'][6][0], face_landmarks_list_apice[0]['top_lip'][6][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['nose_tip'][0][0], face_landmarks_list_apice[0]['nose_tip'][0][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['top_lip'][0][0], face_landmarks_list_apice[0]['top_lip'][0][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['nose_tip'][4][0], face_landmarks_list_apice[0]['nose_tip'][4][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['top_lip'][6][0], face_landmarks_list_apice[0]['top_lip'][6][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['bottom_lip'][3][0], face_landmarks_list_apice[0]['bottom_lip'][3][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['nose_tip'][2][0], face_landmarks_list_apice[0]['nose_tip'][2][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['bottom_lip'][3][0], face_landmarks_list_apice[0]['bottom_lip'][3][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['chin'][8][0], face_landmarks_list_apice[0]['chin'][8][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['top_lip'][0][0], face_landmarks_list_apice[0]['top_lip'][0][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['top_lip'][6][0], face_landmarks_list_apice[0]['top_lip'][6][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['top_lip'][3][0], face_landmarks_list_apice[0]['top_lip'][3][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['bottom_lip'][3][0], face_landmarks_list_apice[0]['bottom_lip'][3][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['top_lip'][9][0], face_landmarks_list_apice[0]['top_lip'][9][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['bottom_lip'][9][0], face_landmarks_list_apice[0]['bottom_lip'][9][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['chin'][8][0], face_landmarks_list_apice[0]['chin'][8][1]), 5,(0,255,0), -1)
cv2.circle(imagem,(face_landmarks_list_apice[0]['nose_tip'][2][0], face_landmarks_list_apice[0]['nose_tip'][2][1]), 5,(0,255,0), -1)

#Linhas
cv2.line(imagem, (face_landmarks_list_apice[0]['left_eyebrow'][4][0], face_landmarks_list_apice[0]['left_eyebrow'][4][1]), (face_landmarks_list_apice[0]['left_eye'][3][0], face_landmarks_list_apice[0]['left_eye'][3][1]), vermelho,2)
cv2.line(imagem, (face_landmarks_list_apice[0]['right_eyebrow'][0][0], face_landmarks_list_apice[0]['right_eyebrow'][0][1]),(face_landmarks_list_apice[0]['right_eye'][0][0], face_landmarks_list_apice[0]['right_eye'][0][1]), vermelho,2)
cv2.line(imagem, (face_landmarks_list_apice[0]['left_eyebrow'][1][0], face_landmarks_list_apice[0]['left_eyebrow'][1][1]),(face_landmarks_list_apice[0]['left_eye'][3][0], face_landmarks_list_apice[0]['left_eye'][3][1]), vermelho,2)
cv2.line(imagem, (face_landmarks_list_apice[0]['right_eyebrow'][3][0], face_landmarks_list_apice[0]['right_eyebrow'][3][1]), (face_landmarks_list_apice[0]['right_eye'][0][0], face_landmarks_list_apice[0]['right_eye'][0][1]), vermelho,2)
cv2.line(imagem, (face_landmarks_list_apice[0]['left_eyebrow'][4][0], face_landmarks_list_apice[0]['left_eyebrow'][4][1]), (face_landmarks_list_apice[0]['right_eyebrow'][0][0], face_landmarks_list_apice[0]['right_eyebrow'][0][1]), vermelho, 2)
cv2.line(imagem, (face_landmarks_list_apice[0]['left_eye'][2][0], face_landmarks_list_apice[0]['left_eye'][2][1]), (face_landmarks_list_apice[0]['left_eye'][4][0], face_landmarks_list_apice[0]['left_eye'][4][1]), vermelho, 2)
cv2.line(imagem, (face_landmarks_list_apice[0]['right_eye'][1][0], face_landmarks_list_apice[0]['right_eye'][1][1]), (face_landmarks_list_apice[0]['right_eye'][5][0], face_landmarks_list_apice[0]['left_eye'][5][1]), vermelho, 2)
cv2.line(imagem, (face_landmarks_list_apice[0]['left_eyebrow'][4][0], face_landmarks_list_apice[0]['left_eyebrow'][4][1]), (face_landmarks_list_apice[0]['nose_tip'][0][0], face_landmarks_list_apice[0]['nose_tip'][0][1]), vermelho, 2)
cv2.line(imagem, (face_landmarks_list_apice[0]['right_eyebrow'][0][0], face_landmarks_list_apice[0]['right_eyebrow'][0][1]), (face_landmarks_list_apice[0]['nose_tip'][4][0], face_landmarks_list_apice[0]['nose_tip'][4][1]), vermelho, 2)
cv2.line(imagem, (face_landmarks_list_apice[0]['top_lip'][3][0], face_landmarks_list_apice[0]['top_lip'][3][1]), (face_landmarks_list_apice[0]['nose_tip'][2][0], face_landmarks_list_apice[0]['nose_tip'][2][1]), vermelho, 2)
cv2.line(imagem, (face_landmarks_list_apice[0]['top_lip'][0][0], face_landmarks_list_apice[0]['top_lip'][0][1]), (face_landmarks_list_apice[0]['top_lip'][6][0], face_landmarks_list_apice[0]['top_lip'][6][1]), vermelho, 2)
cv2.line(imagem, (face_landmarks_list_apice[0]['nose_tip'][0][0], face_landmarks_list_apice[0]['nose_tip'][0][1]), (face_landmarks_list_apice[0]['top_lip'][0][0], face_landmarks_list_apice[0]['top_lip'][0][1]), vermelho, 2)
cv2.line(imagem, (face_landmarks_list_apice[0]['nose_tip'][4][0], face_landmarks_list_apice[0]['nose_tip'][4][1]), (face_landmarks_list_apice[0]['top_lip'][6][0], face_landmarks_list_apice[0]['top_lip'][6][1]), vermelho, 2)
cv2.line(imagem, (face_landmarks_list_apice[0]['bottom_lip'][3][0], face_landmarks_list_apice[0]['bottom_lip'][3][1]), (face_landmarks_list_apice[0]['nose_tip'][2][0], face_landmarks_list_apice[0]['nose_tip'][2][1]), vermelho, 2)
cv2.line(imagem, (face_landmarks_list_apice[0]['bottom_lip'][3][0], face_landmarks_list_apice[0]['bottom_lip'][3][1]), (face_landmarks_list_apice[0]['chin'][8][0], face_landmarks_list_apice[0]['chin'][8][1]), vermelho, 2)
cv2.line(imagem, (face_landmarks_list_apice[0]['top_lip'][0][0], face_landmarks_list_apice[0]['top_lip'][0][1]), (face_landmarks_list_apice[0]['top_lip'][6][0], face_landmarks_list_apice[0]['top_lip'][6][1]), vermelho, 2)
cv2.line(imagem, (face_landmarks_list_apice[0]['top_lip'][3][0], face_landmarks_list_apice[0]['top_lip'][3][1]), (face_landmarks_list_apice[0]['bottom_lip'][3][0], face_landmarks_list_apice[0]['bottom_lip'][3][1]), vermelho, 2)
cv2.line(imagem, (face_landmarks_list_apice[0]['top_lip'][9][0], face_landmarks_list_apice[0]['top_lip'][9][1]), (face_landmarks_list_apice[0]['bottom_lip'][9][0], face_landmarks_list_apice[0]['bottom_lip'][9][1]), vermelho, 2)
cv2.line(imagem, (face_landmarks_list_apice[0]['chin'][8][0], face_landmarks_list_apice[0]['chin'][8][1]), (face_landmarks_list_apice[0]['nose_tip'][2][0], face_landmarks_list_apice[0]['nose_tip'][2][1]), vermelho, 2)


cv2.imshow("AU1", imagem)

cv2.imwrite("apice.png", imagem)
cv2.waitKey(0)