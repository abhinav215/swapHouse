import os


def deleteContent(directory):
    files = os.listdir(directory)
    for file in files:
        if os.path.exists(os.path.join(directory, file)):
            os.remove(os.path.join(directory, file))


if __name__=="__main__":
    print("gg")
    deleteContent("andrea")