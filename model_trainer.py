import cv2 
import os
import numpy as np
from PIL import Image
path = 'dataset'
recognizer = cv2.face.LBPHFaceRecognizer_create()
def getImagesWithId(path):
    images_list=[]
    faces=[]
    IDs=[]
    for sample in os.listdir(path):
        images_list.append(os.path.join(path,sample))
    for imagePath in images_list:
        img = Image.open(imagePath).convert('L')
        faceNp = np.array(img,'uint8')
        # img = cv2.imread(imagePath)
        # faceNp=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        id = int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        IDs.append(id)
        cv2.imshow("faces",faceNp)
        cv2.waitKey(100)
    return faces,np.array(IDs)
    

faces,IDs=getImagesWithId(path)
recognizer.train(faces,IDs)
recognizer.write("recognizer/trainer.yml")
print("success")