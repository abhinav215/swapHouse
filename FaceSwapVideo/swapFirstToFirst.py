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


swapper = insightface.model_zoo.get_model("inswapper_128.onnx",download=False,download_zip=False)

def swapFxn(facePath,bodyPath,outputPath):
    faceImage = cv2.imread(facePath)
    faceImgFace = app.get(faceImage)[0]
    bodyImage = cv2.imread(bodyPath)
    body = app.get(bodyImage)
    if len(body)==0:
        cv2.imwrite(outputPath,bodyImage)
        return 
    bodyImgFace = body[0]
    
    res = bodyImage.copy()
    res = swapper.get(res,bodyImgFace,faceImgFace,paste_back=True)
    cv2.imwrite(outputPath,res)

if __name__== "__main__":
    facePath = "D:/dev/image/Main/Main/ai/realAI/swapping/faces/abhinav.jpg"
    bodyPath = "D:/dev/image/Main/Main/ai/realAI/swapping/newImages/mom intro.jpg"
    outputPath = "D:/dev/image/Main/Main/ai/realAI/swapping/output/7.jpg"
    swapFxn(facePath,bodyPath,outputPath)

# img = cv2.imread("D:/dev/image/Main/Main/ai/realAI/swapping/newImages/36.jpg")
# plt.imshow(img[:,:,::-1])
# plt.show()
# cv2.imwrite("D:/dev/ai/others/swapping/output.jpg",img)

