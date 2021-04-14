import cv2
import urllib.request
import numpy as np
import time

URL = "http://192.168.1.102:8080/shot.jpg"
faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
while True:
    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
    img1 = cv2.imdecode(img_arr, -1)
    img1 = cv2.resize(img1, (400, 640))
    cv2.imshow('IPWebcam', img1)

    imgGray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 11., 3)
    Xo, Yo, Co = img1.shape

    Xc = Xo / 2
    Yc = Yo / 2
    print(img1.shape)
    for (x, y, w, h) in faces:
        cv2.rectangle(img1, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.circle(img1, (int(x + w / 2), int(y + h / 2)), 2, (0, 0, 255), 5)
        cv2.circle(img1, (int(Yc), int(Xc)), 2, (0, 255, 0), 5)
        print(Yc - (x + w / 2), "distance in X")
        print(Xc - (y + h / 2), "distance in Y")

    cv2.imshow("result", img1)

    #print(Xc - (x + w / 2), "distance in X")
    #print(Yc - (y + h / 2), "distance in Y")

    if cv2.waitKey(1)==27:
        break


#img =cv2.imread("D:/face/1.jpg")

#imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#faces=faceCascade.detectMultiScale(imgGray,1.1,4)
#Xo,Yo,Co=img.shape

#Xc=Xo/2
#Yc=Yo/2
#print(img.shape)
#for (x,y,w,h) in faces:
    #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    #cv2.circle(img, (int(x+w/2), int(y+h/2)), 2, (0, 0, 255), 5)
   # cv2.circle(img, (int(Yc), int(Xc)), 2, (0, 255, 0), 5)
    #print(Yc - (x + w / 2), "distance in X")
    #print(Xc - (y + h / 2), "distance in Y")

#cv2.imshow("result",img)
#cv2.waitKey(0)
#print(Xc-(x+w/2),"distance in X")
#print(Yc-(y+h/2),"distance in Y")