from psd_tools import PSDImage
from PIL import Image, ImageDraw, ImageFont
import os
import re
import newPrintImage

cup_dir = "Готовые кружки"
fontPath = "a_Futurica.ttf"
font = ImageFont.truetype(fontPath, 70)

def createCupDir():
  # Создаем временную директорию
    try:
        os.mkdir(cup_dir)
    except FileExistsError:
        pass

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

def findCup(listPsdFl):
    cupFl = []
    for fl in listPsdFl:
        if "Кружка-термос с крышкой" in fl:
            cupFl.append(fl)
    return cupFl

def convertPsd(psdFl, cupDir):
    # Конвертируем psd файлы в jpeg, сначала пересохраняем в png
    # тк метод не из psd_tools не умеет сразу сохранять в jpeg
    # загружаем png файл, конвертируем его в RGB и ресайзим
    # до размера 900 px
    baseSize = 900
    for psdFlName in psdFl:
        number = int(psdFlName.split("_")[4])
        psd = PSDImage.open(psdFlName)
        pilImg = psd.compose()
        pilImgRotate = pilImg.transpose(Image.ROTATE_90)
        if number == 1:
            pilImgRotate.save(cupDir + os.sep +  psdFlName[0:-4] + ".png", compress_level=0)
        else:
            i = 0
            while i < number :
                pilImgRotate.save(cupDir + os.sep +  psdFlName[0:-4] +"_копия " + str(i) + ".png", compress_level=0)
                i = i + 1

def dictSort(unsortedDict):
    tmpList = []
    clssListSorted = {}
    for key, val in unsortedDict.items():
        tmpList.append(key)
    tmpListSorted = sorted(tmpList)
    for key in tmpListSorted:
        clssListSorted[key] = []
        clssListSorted[key] = unsortedDict[key]
    return clssListSorted
 
def createDictClass(flList):
    # функция создания словаря с "классами", если "класс""
    # в файле не указан, файл будет добавлен в "Класс" по умолчанию
    clssList = {"Класс": [], }
    for fl in flList:
        i = fl.split("_")
        try:
            if i[5] not in clssList.keys():
                clssList[i[5]] = []
                clssList[i[5]].append(fl)
            else:
                clssList[i[5]].append(fl)
        except IndexError:
            for key, val in clssList.items():
                if key == "Не указан":
                    val.append(fl)
    return dictSort(clssList)

def delOldPng(oldPng):
    for i in oldPng:
        if "Кружка-термос с крышкой" in i:
            os.remove(cup_dir + os.sep + i)


def generatePngForPrint(dictOfClass, objectName):
    # objectName = os.getcwd().split(sep)[-1]
    cell=0
    count=0
    fileName=""
    oldFileName=""
    for key, val in dictOfClass.items():
        for v in val:
            cell += 1              
            if cell == 1:
                className = v.split("_")[5]
                fileName = className
                img = Image.new('RGBA', (2480,3508), color=(255,255,255))
                draw = ImageDraw.Draw(img)
                draw.text((500, 50), objectName, font=font, fill=(0,0,0,255))
                draw.text((100, 50), className, font=font, fill=(0,0,0,255))
                cupImg = Image.open(cup_dir + os.sep + v)
                img.paste(cupImg, (75, 160))
                img.save( cup_dir + os.sep + fileName + ".png", compress_level=0, dpi=(300,300))
                img.close()
                oldFileName = fileName
            elif cell == 2:
                img = Image.open(cup_dir + os.sep + fileName + ".png")
                draw = ImageDraw.Draw(img)
                cupImg = Image.open(cup_dir + os.sep + v)

                imgToDel = cup_dir + "/" + oldFileName + ".png"
                os.remove(imgToDel)
                className = v.split("_")[5]
                fileName += "_" + className + "_" + str(count)

                draw.text((2200, 50), className, font=font, fill=(0,0,0,255))
                img.paste(cupImg, (1265, 160))
                img.save( cup_dir + os.sep + fileName + ".png", compress_level=0, dpi=(300,300))
                img.close()
                
                cell = 0
                count += 1
