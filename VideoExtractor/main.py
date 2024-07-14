from downloadVid import *
from merge import *
from delete import *


url =  "https://cdn011.thotdeep.com/hls/v4zNrzum7ilx9v3z2-e51w,1719096175/15476/video"
ending = ".ts"
download(url,0,ending)

naam = "payalGaming"
zz = r"folder"
merge(naam,zz)

deleteContent(zz)