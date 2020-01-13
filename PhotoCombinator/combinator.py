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

def createListsOfPhotoFile(txtFl):
    fl = open(txtFl[0], 'r', encoding = 'cp500')
    for line in fl:
        print(line)

def listHVPhotoForCrop(fl):
    photoH = []
    photoV = []
    for i in fl:
        if "H" in i:
            photoH.append(i)
        elif "V" in i:
            photoV.append(i)
    return photoH, photoV

def createFileForRemoveBGH(photoH):
    baseSize = 4000
    basImg = Image.new('RGB', (4000, 6250), color = (255, 255, 255))
    countImg = 0
    baseFileName = "H_"
    countLen = 0
    for i in photoH:
        print() 
        countImg += 1
        img = Image.open(i)
        x, y = img.size
        width = baseSize
        height = int(width / x * y)
        imgR = img.resize((width, height), Image.BICUBIC)
        #countLen += 1
        if countImg == 1:
            baseFileName += i[:-4] + "_"
            basImg = Image.new('RGB', (4000, 6250), color = (255, 255, 255))     
            basImg.paste(imgR, (0, 0))
            if photoH.index(i) == (len(photoH) - 1):
                basImg.save(baseFileName + "NONE_.jpeg")
        else:
            baseFileName += i[:-4] + "_"
            basImg.paste(imgR, (0,3250))
            basImg.save(baseFileName + ".jpeg")
            baseFileName = "H_"
            countImg = 0

def createFileForRemoveBGV(photoV):
    baseSize = 4000
    basImg = Image.new('RGB', (6250, 4000), color = (255, 255, 255))
    countImg = 0
    baseFileName = "V_"
    countLen = 0
    for i in photoV:
        print() 
        countImg += 1
        img = Image.open(i)
        x, y = img.size
        height = baseSize
        width = int(height / y * x)
        imgR = img.resize((width, height), Image.BICUBIC)
        #countLen += 1
        if countImg == 1:
            baseFileName += i[:-4] + "_"
            basImg = Image.new('RGB', (6250, 4000), color = (255, 255, 255))     
            basImg.paste(imgR, (0, 0))
            if photoV.index(i) == (len(photoV) - 1):
                basImg.save(baseFileName + "NONE_.jpeg")
        else:
            baseFileName += i[:-4] + "_"
            basImg.paste(imgR, (3250,0))
            basImg.save(baseFileName + ".jpeg")
            baseFileName = "V_"
            countImg = 0

def cropImage(photoH, photoV):
    for i in photoH:
        img = Image.open(i)
        imgTopName = i.split("_")[1]
        imgTop = img.crop((0,0,4000,2700))
        imgTop.save(imgTopName + ".png")
        imgBottomName = i.split("_")[2]
        if "NONE" not in imgBottomName:
            imgBottom = img.crop((0,3250,4000,6000))
            imgBottom.save(imgBottomName + ".png")

    for i in photoV:
        img = Image.open(i)
        imgTopName = i.split("_")[1]
        imgTop = img.crop((0,0,2700,4000))
        imgTop.save(imgTopName + ".png")
        imgBottomName = i.split("_")[2]
        if "NONE" not in imgBottomName:
            imgBottom = img.crop((3250,0,6000,4000))
            imgBottom.save(imgBottomName + ".png")