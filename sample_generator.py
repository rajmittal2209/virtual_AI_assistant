import cv2
import os
vid = cv2.VideoCapture(0,cv2.CAP_DSHOW)
casc = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
sampleNum = 0
pre=0
path_of_faces = "C:\\Users\\Raj mittal\\Desktop\\virtual_AI_Assistant\\dataset"
os.mkdir(path_of_faces)
with open("id.txt","r") as f:
    pre=f.read()
pre = int(pre)
id = pre + 1
with open("id.txt",'w') as f:
     f.write(str(id))
name = input("enter your name : ")
with open("names.txt",'a') as f:
    f.write(name+'\n')
while True:
    check,frame = vid.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = casc.detectMultiScale(gray,1.32,5)
    for x,y,w,h in faces:
        sampleNum=sampleNum + 1
        cv2.imwrite(f"dataset/user.{id}.{sampleNum}.jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),2)
    cv2.imshow("face",frame)
    cv2.waitKey(1)
    if(sampleNum>=20):break 
vid.release()
cv2.destroyAllWindows()    

