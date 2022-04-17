# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 16:34:36 2020

@author: tales
"""

import cv2 as cv
import matplotlib.pyplot as plt
import face_recognition
from PIL import Image, ImageDraw
import mysql.connector
import math

banco = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "32331716",
        database = "thallys"
)

net = cv.dnn.readNetFromTensorflow("graph_opt.pb")
inWidth = 368
inHeight = 368
thr = 0.2 

BODY_PARTS = { "Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
               "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
               "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
               "LEye": 15, "REar": 16, "LEar": 17, "Background": 18 }

POSE_PAIRS = [ ["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
               ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
               ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
               ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"],
               ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"] ]

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FPS, 10)
cap.set(3,800)
cap.set(4,800)

if not cap.isOpened():
    cap = cv.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open video")

while cv.waitKey(1) < 0:
    hasFrame, frame = cap.read()
    if not hasFrame:
        cv.waitKey()
        break
    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]
    
    face_landmarks_list = face_recognition.face_landmarks(frame)
    
    if len(face_landmarks_list) > 0:
        a = face_landmarks_list[0]['chin'][0][0]

        b = face_landmarks_list[0]['chin'][0][1]
        
        c = face_landmarks_list[0]['chin'][1][0]

        d = face_landmarks_list[0]['chin'][1][1]
        
        cursor = banco.cursor()

        comando_SQL = "INSERT INTO landmarks (captura,landmark,x,y) VALUES (%s, %s, %s, %s)"

        dados = ("1", "1", a, b)

        cursor.execute(comando_SQL, dados)

        banco.commit()
        for i in range(0,11):
            cv.circle(frame, face_landmarks_list[0]['top_lip'][i] , 2, (0,0,255), -1)
        
    net.setInput(cv.dnn.blobFromImage(frame, 1.0, (inWidth, inHeight), (127.5, 127.5, 127.5), swapRB=True, crop=False))
    out = net.forward()
    out = out[:, :19, :, :]  # MobileNet output [1, 57, -1, -1], we only need the first 19 elements

    assert(len(BODY_PARTS) == out.shape[1])

    points = []
    
    for i in range(len(BODY_PARTS)):
        # Slice heatmap of corresponging body's part.
        heatMap = out[0, i, :, :]

        # Originally, we try to find all the local maximums. To simplify a sample
        # we just find a global one. However only a single pose at the same time
        # could be detected this way.
        _, conf, _, point = cv.minMaxLoc(heatMap)
        x = (frameWidth * point[0]) / out.shape[3]
        y = (frameHeight * point[1]) / out.shape[2]
        # Add a point if it's confidence is higher than threshold.
        points.append((int(x), int(y)) if conf > thr else None)

    for pair in POSE_PAIRS:
        partFrom = pair[0]
        partTo = pair[1]
        assert(partFrom in BODY_PARTS)
        assert(partTo in BODY_PARTS)

        idFrom = BODY_PARTS[partFrom]
        idTo = BODY_PARTS[partTo]

        if points[idFrom] and points[idTo]:
            cv.line(frame, points[idFrom], points[idTo], (0, 255, 0), 3)
            cv.ellipse(frame, points[idFrom], (3, 3), 0, 0, 360, (0, 0, 255), cv.FILLED)
            cv.ellipse(frame, points[idTo], (3, 3), 0, 0, 360, (0, 0, 255), cv.FILLED)

    t, _ = net.getPerfProfile()
    freq = cv.getTickFrequency() / 1000
    cv.putText(frame, '%.2fms' % (t / freq), (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    
    cv.imshow("Pose estimation", frame)
    
    if cv.waitKey(1)&0xFF == ord("q"):
        break
    
cap.release()
cv.destroyAllWindows()
    
    
    



