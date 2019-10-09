from psd_tools import PSDImage
from PIL import Image, ImageDraw, ImageFont
import os
import re
import newPrintImage

cup_dir = "Готовые кружки"
fontPath = "/media/work_part/python/previewer/py_previwer/Font/a_Futurica.ttf"
font = ImageFont.truetype(fontPath, 70)
def newPage():
    img = Image.new('RGBA', (2480,3580), color=(255,255,255))
    img = Image.new('RGBA', (2480,3580), color=(255,255,0))
    psdImg = PSDImage.frompil(img, compression=0)
    psdImg.save("test.psd",mode="wb")


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
        psd = PSDImage.open(psdFlName)
        pilImg = psd.compose()
        pilImgRotate = pilImg.transpose(Image.ROTATE_90)
        pilImgRotate.save(cupDir + os.sep +  psdFlName[0:-4] + ".png", compress_level=0)

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



def generatePngForPrint(dictOfClass, objectName):
    # objectName = os.getcwd().split(sep)[-1]
    cell=0
    count=0
    fileName=""
    for key, val in dictOfClass.items():
        for v in val:
            cell += 1
            print(cell)
            if cell == 1:
                className = v.split("_")[5]
                fileName = className
                img = Image.new('RGBA', (2480,3580), color=(255,255,255))
                draw = ImageDraw.Draw(img)
                draw.text((1240, 50), objectName, font=font, fill=0)
                draw.text((595, 50), className, font=font, fill=0)
                cupImg = Image.open(cup_dir + os.sep + v)
                img.paste(cupImg, (50, 275))
            elif cell == 2:
                cupImg = Image.open(cup_dir + os.sep + v)
                className = v.split("_")[5]
                fileName += "_" + className
                draw.text((1885, 50), className, font=font, fill=0)
                img.paste(cupImg, (1290, 275))
                img.save( cup_dir + os.sep + fileName + ".png", compress_level=0)
                cell = 0
                count += 1