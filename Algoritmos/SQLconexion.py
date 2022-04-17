from PIL import Image, ImageDraw
import face_recognition
import cv2
# Load the jpg file into a numpy array


image1 = cv2.imread("foto.jpg")


# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image1)


print(face_landmarks_list[0])

for i in range(0,17):
    cv2.circle(image1, face_landmarks_list[0]['chin'][i] , 3, (0,0,255), -1)
    
for i in range(0,5):
    cv2.circle(image1, face_landmarks_list[0]['left_eyebrow'][i] , 3, (0,0,255), -1)

for i in range(0,5):
    cv2.circle(image1, face_landmarks_list[0]['right_eyebrow'][i] , 3, (0,0,255), -1)

for i in range(0,4):
    cv2.circle(image1, face_landmarks_list[0]['nose_bridge'][i] , 3, (0,0,255), -1)

for i in range(0,5):
    cv2.circle(image1, face_landmarks_list[0]['nose_tip'][i] , 3, (0,0,255), -1)
    
for i in range(0,6):
    cv2.circle(image1, face_landmarks_list[0]['left_eye'][i] , 3, (0,0,255), -1) 
    
for i in range(0,6):
    cv2.circle(image1, face_landmarks_list[0]['right_eye'][i] , 3, (0,0,255), -1)

for i in range(0,12):
    cv2.circle(image1, face_landmarks_list[0]['bottom_lip'][i] , 3, (0,0,255), -1)
    
for i in range(0,12):
    cv2.circle(image1, face_landmarks_list[0]['top_lip'][i] , 3, (0,0,255), -1)

a = face_landmarks_list[0]['chin'][0][0]

b = face_landmarks_list[0]['chin'][0][1]

import mysql.connector

banco = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "32331716",
        database = "thallys"
)

cursor = banco.cursor()

comando_SQL = "INSERT INTO landmarks (captura,landmark,x,y) VALUES (%s, %s, %s, %s)"

dados = ("1", "1", a, b)

cursor.execute(comando_SQL, dados)

banco.commit()



cv2.imshow("f", image1)

cv2.waitKey(0)



