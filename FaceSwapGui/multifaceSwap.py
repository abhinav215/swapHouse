import numpy as np
import cv2
import glob
import os
import matplotlib.pyplot as plt

import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image

app = FaceAnalysis(name="buffalo_l")
app.prepare(ctx_id=0, det_size=(640,640))


# swapper = insightface.model_zoo.get_model("inswapper_128.onnx",download=False,download_zip=False)


def swapFxn(facePath,bodyPath,swapper,outputPath):
    bodyImage = cv2.imread(bodyPath)
    body = app.get(bodyImage)
    
    if len(body)==0:
        return 
    
    res = bodyImage.copy()
    cnt = 0
    for bodyImgFaceInput in body:
        if cnt==len(facePath):
            break
        if facePath[cnt]=="":
            cnt+=1
            continue
        faceImage = cv2.imread(facePath[cnt])
        print(facePath[cnt])
        faceImgFace = app.get(faceImage)[0]
        res = swapper.get(res,bodyImgFaceInput,faceImgFace,paste_back=True)
        cnt+=1
    cv2.imwrite(outputPath,res)
    print("Swap Done")

def showFacesOrder(body):
    print(body)
    img = cv2.imread(body)
    faces = app.get(img)
    temp = []
    i = 0
    for face in faces:
        bbox = face["bbox"]
        bbox = [int(b) for b in bbox]
        abc = img[bbox[1]:bbox[3],bbox[0]:bbox[2],::]
        
        # cv2.imwrite("tempFaces/"+str(i)+".jpg",abc)
        temp.append(abc)
        print("DONE")
        i+=1
    return temp


if __name__== "__main__":
    # facePath = ["faces/abc.jpg","faces/abhinav.jpeg"]
    # facePath.reverse()
    # bodyPath = "images/zzabhi169.jpg"
    # outputPath = "output/169.jpg"
    # swapFxn(facePath,bodyPath,swapper,outputPath)
    
    bodyPath = "images/ab002.jpg"
    showFacesOrder(bodyPath)


