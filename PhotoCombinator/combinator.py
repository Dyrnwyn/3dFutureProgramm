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


def getphotoname(line):
    return line.split(';')[5] + '_' + line.split(';')[9]

def createListsOfPhotoFile(txtFl):
    fl = open(txtFl[0], 'r', encoding='cp1251')
    size10 = []
    size15 = []
    size20 = []
    for line in fl:
        if '10х15' in line:
            photoName = getphotoname(line)
            size10.append(photoName)
        elif '15х20' in line:
            photoName = getphotoname(line)
            size15.append(photoName)
        elif '20х30' in line:
            photoName = getphotoname(line)
            size20.append(photoName)
    fl.close()
    return size10, size15, size20


def sortphoto10(size10, dir10):
    os.mkdir(dir10)
    for i in size10:
        os.system('copy ' + i.split('_')[0] + '.jpg ' + '"' + dir10 + '"')


def sortphoto15(size15, dir15):
    os.mkdir(dir15)
    for i in size15:
        os.system('copy ' + i.split('_')[0] + '.jpg ' + '"' + dir15 + '"')

def sortphoto20(size20, dir20):
    os.mkdir(dir20)
    for i in size20:
        os.system('copy ' + i.split('_')[0] + '.jpg ' + '"' + dir20 + '"')

def pagesize10(size10):
    baseImg = Image.new('RGB', (2480, 3508), color=(255, 255, 255))
    countImg10 = 0
    countImg = 0
    baseFileName = '10x15_'
    count = 0
    baseSize = 1181
    for i in size10:
        countImg10 += 1
        count = 0
        img = Image.open(i.split('_')[0]+'.jpg')
        x, y = img.size
        

        if x > y:
            height = baseSize
            width = int(height / y * x)
            imgR = img.resize((width, height), Image.BICUBIC)
        elif y > x:
            width = baseSize
            height = int(width / x * y)
            imgR = img.resize((width, height), Image.BICUBIC)

        while count < int(i.split('_')[1]):
            count += 1
            countImg += 1
            if countImg == 1:
                baseFileName += i.split('_')[0] + '_'
                if x < y:
                    imgRH =  imgR.transpose(Image.ROTATE_90)
                    baseImg.paste(imgRH, (300, 150))
                else:
                    baseImg.paste(imgR, (300, 150))
                if size10.index(i) == (len(size10) - 1):
                    baseImg.save(baseFileName + 'NONE_NONE_' +
                    '.jpeg', dpi=(300,300))
                    baseFileName = '10x15_'
            elif countImg == 2:
                baseFileName += i.split('_')[0] + '_'
                if x > y:
                    imgRV = imgR.transpose(Image.ROTATE_90)
                    baseImg.paste(imgRV, (50, 1560))
                else:
                    baseImg.paste(imgR, (50, 1560))
                if size10.index(i) == (len(size10) - 1):
                    baseImg.save(baseFileName + 'NONE_' +
                    '.jpeg')
                    baseFileName = '10x15_'
            elif countImg == 3:
                baseFileName += i.split('_')[0] + '_'
                if x > y:
                    imgRV = imgR.transpose(Image.ROTATE_90)
                    baseImg.paste(imgRV, (1250, 1560))
                else:
                    baseImg.paste(imgR, (1250, 1560))
                baseImg.save(baseFileName +'r'+ str(count) + '.jpeg', dpi=(300,300))
                baseFileName = '10x15_'
                countImg = 0
                baseImg = Image.new('RGB', (2480, 3508), color=(255, 255, 255))





def pagesize15(pagesize15):
    baseImg = Image.new('RGB', (2480, 3508), color=(255, 255, 255))
    countImg15 = 0
    countImg = 0
    baseFileName = '15x20_'
    count = 1
    baseSize = 1700
    for i in pagesize15:
        count = 0
        countImg15 += 1     
        img = Image.open(i.split('_')[0] + '.jpg')

        x, y = img.size
        if x > y:
            height = baseSize
            width = int(height / y * x)
            imgR = img.resize((width, height), Image.BICUBIC)
        elif y > x:
            width = baseSize
            height = int(width / x * y)
            imgR = img.resize((width, height), Image.BICUBIC)


        while count < int(i.split('_')[1]):
            count += 1
            countImg += 1
            if countImg == 1:
                baseFileName += i.split('_')[0] + "_"
                basImg = Image.new('RGB', (2480, 3508), color = (255, 255, 255))
                if x < y:
                    imgRH = imgR.transpose(Image.ROTATE_90)
                    basImg.paste(imgRH, (34, 40))
                else:
                    basImg.paste(imgR, (34, 40))
                if pagesize15.index(i) == (len(pagesize15) - 1):
                    basImg.save(baseFileName + "NONE_.jpeg", dpi=(300,300))
            else:
                baseFileName += i.split('_')[0] + "_"
                if x < y:
                    imgRH = imgR.transpose(Image.ROTATE_90)
                    basImg.paste(imgRH, (34, 1758))
                else:
                    basImg.paste(imgR, (34, 1758))
                basImg.save(baseFileName +'r'+ str(count) + ".jpeg", dpi=(300,300))            
                baseFileName = "15x20_"
                countImg = 0
                baseImg = Image.new('RGB', (2480, 3508), color=(255, 255, 255))





def pagesize20(size20):

    countImg20 = 0
    countImg = 0
    baseFileName = '20x30_'
    count = 0
    baseSize = 2415

    for i in size20:
        baseImg = Image.new('RGB', (2480, 3508), color=(255, 255, 255))
        countImg20 += 1
        img = Image.open(i.split('_')[0] + '.jpg')
        x, y = img.size

        if x > y:
            height = baseSize
            width = int(height / y * x)
            imgR = img.resize((width, height), Image.BICUBIC)
        elif y > x:
            width = baseSize
            height = int(width / x * y)
            imgR = img.resize((width, height), Image.BICUBIC)
        if x > y:
            imgRH = imgR.transpose(Image.ROTATE_90)
            baseImg.paste(imgRH, (35, 50))
        else:
            baseImg.paste(imgR, (35, 50))

        baseFileName += i 
        baseImg.save(baseFileName + ".jpeg", dpi=(300,300))


        baseFileName = '20x30_'
        baseImg = Image.new('RGB', (2480, 3508), color=(255, 255, 255))
