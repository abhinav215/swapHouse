
from tkinter import *
from PIL import ImageTk, Image
import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from multifaceSwap import *

mapp = {
    "Abhinav":"faces/abhinav.jpeg",
    "None":""
}

characters = []
for ele in mapp:
    characters.append(ele)

add = "images"
add2 = add
cnt = 0
data = []
for filename in os.listdir(add):
    source = add+"/"+filename
    out = "output/"+filename
    dic = {"body":source,"face":[],"out":out}
    data.append(dic)
    cnt+=1

print(data)


swapper = insightface.model_zoo.get_model("inswapper_128.onnx",download=False,download_zip=False)

def swapping(facePath,bodyPath,outputPath):
    swapFxn(facePath,bodyPath,swapper,outputPath)


indexer = 0
faces = data[indexer]["face"]



def lol(image):
    width, height = image.size
    factor = height/400
    ans = image.resize((int(width/factor),int(height/factor)))
    return ans

def CharBtnFxn(arg):
    global indexer
    print(arg)
    if arg in mapp:
        arg = mapp[arg]
    else:
        return
    if arg not in faces:
        faces.append(arg)
    else:
        faces.remove(arg)
    faceInput.configure(text="Faces are ["+displayFaceText(faces)+"]")    

def nextImage():
    global panel,data,indexer,faces
    indexer+=1
    faces = data[indexer]["face"]
    print(data[indexer]["body"],data[indexer]["face"])
    tempImg = Image.open(data[indexer]["body"])
    resize_image = lol(tempImg)
    img2 = ImageTk.PhotoImage(resize_image)
    panel.configure(image=img2)
    panel.image = img2
    showPersonFaces()
    faceInput.configure(text="Faces are ["+displayFaceText(faces)+"]")  

def prevImage():
    global panel,data,indexer,faces
    indexer-=1
    faces = data[indexer]["face"]
    print(data[indexer]["body"],data[indexer]["face"])
    tempImg = Image.open(data[indexer]["body"])
    resize_image = lol(tempImg)
    img2 = ImageTk.PhotoImage(resize_image)
    panel.configure(image=img2)
    panel.image = img2
    showPersonFaces()
    faceInput.configure(text="Faces are ["+displayFaceText(faces)+"]")  

def createImage():
    print(faces)
    print(data[indexer])
    F = data[indexer]["face"]
    B = data[indexer]["body"]
    O = data[indexer]["out"]
    swapping(F,B,O)
 
def displayFaceText(faces):
    out = ""
    for ele in faces:
        out+=" , "+ele
    return out[3:]

def showPersonFaces():
    list = middleframe.grid_slaves()
    for l in list:
        l.destroy()
    persons = showFacesOrder(data[indexer]["body"])
    ll = [0]*len(persons)
    pp = [0]*len(persons)
    for i in range(len(persons)):
        person = persons[i]
        color_converted = cv2.cvtColor(person, cv2.COLOR_BGR2RGB)
        pil_image=Image.fromarray(color_converted)
        # resize_image = lol(pil_image)
        ll[i] = ImageTk.PhotoImage(pil_image)
        pp[i] = Label(middleframe, image = ll[i])
        pp[i].grid(column=i//3,row=i%3)
    middleframe.configure(text="Asd")


root = Tk()

root.title("Editor")
root.geometry("1300x650")
lbl = Label(root,text="Abhinav Baba")
lbl.grid(column=0,row=0)






leftframe = Frame(root,bg="green")
leftframe.grid(column=0,row=1,padx=10,pady=10)

tempImg = Image.open(data[indexer]["body"])
resize_image = lol(tempImg)
img = ImageTk.PhotoImage(resize_image)
panel = Label(leftframe, image = img)
panel.grid(column=0,row=0)

faceInput = Label(leftframe,text="Faces are ["+displayFaceText(faces)+"]")
faceInput.grid(column=0,row=1)




middleframe = Frame(root)
middleframe.grid(column=1,row=1,padx=10,pady=10)
persons = showFacesOrder(data[indexer]["body"])
ll = [0]*len(persons)
pp = [0]*len(persons)
for i in range(len(persons)):
    person = persons[i]
    color_converted = cv2.cvtColor(person, cv2.COLOR_BGR2RGB)
    pil_image=Image.fromarray(color_converted)
    # resize_image = lol(pil_image)
    ll[i] = ImageTk.PhotoImage(pil_image)
    pp[i] = Label(middleframe, image = ll[i])
    pp[i].grid(column=i//3,row=i%3)




rightframe = Frame(root,bg="pink",padx=10,pady=10)
rightframe.grid(column=2,row=1)

btn = [0]*(len(characters))
for i in range(len(characters)):
    print("+=== char",characters[i])
    btn[i] = Button(rightframe,text=characters[i],command=lambda z=characters[i]: CharBtnFxn(z))
    btn[i].grid(column=i%3,row=i//3)


crtImg = Button(rightframe,text="Create Image",command=createImage)
crtImg.grid(column=0,row=400)

prev = Button(rightframe,text="Previous Image",command=prevImage)
prev.grid(column=1,row=400)
nxt = Button(rightframe,text="Next Image",command=nextImage)
nxt.grid(column=2,row=400)



root.mainloop()