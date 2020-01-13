import re
import os
from PIL import Image

def searchFl(flExt, fldr=""):
    # Во временно директории ищем все jpeg файлы
    # И добавляем их в список
    filteredFlList = []
    with os.scandir(fldr) as flList:
        for fl in flList:
            if not fl.name.startswith('.') and fl.is_file() and \
                    re.findall(r"^.*\." + flExt + "*", fl.name):
                filteredFlList.append(fl.name)
    return filteredFlList


def listHVPhoto(fl):
    photoH = []
    photoV = []
    for i in fl:
        img = Image.open(i)
        if img.size[0] < img.size[1]:
            photoV.append(i)
        else:
            photoH.append(i)
        img.close()
    return photoH, photoV

def createFileForRemoveBGH(photoH):
    baseSize = 4000
    basImg = Image.new('RGB', (4000, 6250), color = (255, 255, 255))
    countImg = 0
    baseFileName = "H_"
    for i in photoH:
        countImg += 1
        img = Image.open(i)
        x, y = img.size
        width = baseSize
        height = int(width / x * y)
        imgR = img.resize((width, height), Image.BICUBIC)
        
        if countImg == 1:
            baseFileName += i[:-4] + "_"
            basImg = Image.new('RGB', (4000, 6250), color = (255, 255, 255))     
            basImg.paste(imgR, (0, 0))
            print(countImg)
        else:
            baseFileName += i[:-4]
            basImg.paste(imgR, (0,3250))
            basImg.save(baseFileName + ".jpeg")
            baseFileName = "H_"
            countImg = 0
