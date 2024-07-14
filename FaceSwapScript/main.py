import os
from pathlib import Path
from swapFirstToFirst import swapFxn


def cutting(face):
    lt = face.split(".")
    print(lt)
    return lt

lt = os.listdir("destImage")
face = "test7.jpeg"
prefix, suffix = cutting(face)
cnt = 0
for ele in lt:
    # print(ele)
    bodyPath = "destImage/"+ ele
    prefix2, suffix2 = cutting(ele)
    facePath = "faces/" + face
    outputPath = "output/" + prefix + prefix2 + "." + suffix
    print((facePath,bodyPath,outputPath))
    p = Path(outputPath)
    # print(p.exists())
    if p.exists()==False:
        swapFxn(facePath,bodyPath,outputPath)
    if cnt==10:
        break
    cnt+=1
# print(cnt)
