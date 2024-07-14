
import requests
import base64
import subprocess


# https://cdn011.thotdeep.com/hls/LBlMAwttECfeVzWvJPNFyQ,1718724647/6757/video21.ts

pat = ""
authorization = str(base64.b64encode(bytes(':'+pat, 'ascii')), 'ascii')

headers = {
 'Accept': 'application/json',
 'Authorization': 'Basic '+authorization
}

def padding(cnt,digit):
    ss = str(cnt)
    return ("0"*(digit-len(ss))+ss)


def download(url,paddingNum,ending):
    cnt = 0
    while True:
        inputUrl = url+padding(cnt,paddingNum)+ending
        print(inputUrl)
        outputFile = "folder/video"+padding(cnt,0)+".ts"
        response = requests.get(inputUrl, headers=headers)

        # with open("abc.mp4", "w") as text_file:
        #     text_file.write(response.content)
        if response.status_code!=200:
            print("breaking",response.status_code)
            break
        file = open(outputFile, "wb")
        file.write(response.content)
        file.close()
        cnt+=1


if __name__ == '__main__':
    url = "https://cdn011.thotdeep.com/hls/LBlMAwttECfeVzWvJPNFyQ,1718724647/6757/video"
    ending = ".ts"
    download(url,0,ending)
