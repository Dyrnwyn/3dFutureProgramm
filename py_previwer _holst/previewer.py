import newPage
import os
from psd_tools import PSDImage
import re
from PIL import Image
from os import sep
#11

tmpDir = 'tmp'


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


def rename_psd_file(txtFl):
    """Создаем списки фотографий 10х15, 15х20, 20х30"""
    fl = open(txtFl[0], 'r', encoding='cp1251')
    vid = "п" # Вид фото
    sizeHolst = "" # размер фото
    photoName = "" # имя фото
    shablon = "Синий фон"
    number = "" # Количество
    price = "" # Цена
    clss = "" # Класс
    for line in fl:
        if line[1] == '$':
            splittedLine = line.split(';')
            photoName = splittedLine[5]
            sizeHolst = splittedLine[6]
            number = splittedLine[9]
            price = splittedLine[10]
            clss = splittedLine[3]
            try:
                os.rename(photoName + ".psd", vid + "_" + sizeHolst + "_" +
                          shablon + "_" + photoName + "_" + number + "_" +
                          clss + "_" + "" + "_" + "id" + "_" + price + "__H" + ".psd")
            except Exception as e:
                continue



def convertPsd(psdFl, tmpDir):
    # Конвертируем psd файлы в jpeg, сначала пересохраняем в png
    # тк метод не из psd_tools не умеет сразу сохранять в jpeg
    # загружаем png файл, конвертируем его в RGB и ресайзим
    # до размера 900 px
    baseSize = 900
    for psdFlName in psdFl:
        psd = PSDImage.open(psdFlName)
        psd.compose().save(tmpDir + sep + "tmp_file.png")
        pngFl = Image.open(tmpDir + sep + "tmp_file.png")
        rgb_png = pngFl.convert("RGB")
        x, y = rgb_png.size
        if x > y:
            width = baseSize
            height = int(width / x * y)
        elif y > x:
            height = baseSize
            width = int(height / y * x)
        else:
            height = 590
            width = 590
        jpgFl = rgb_png.resize((width, height), Image.BICUBIC)
        jpgFl.save(tmpDir + sep + psdFlName[0:-4] + ".jpeg")
    os.remove(tmpDir + sep + "tmp_file.png")


def createTmpDir():
    # Создаем временную директорию
    try:
        os.mkdir(tmpDir)
    except FileExistsError:
        pass


def removeTmpDir():
    folders = []
    for i in os.walk(tmpDir):
        folders.append(i[0])
        for fl in i[2]:
            os.remove(i[0] + sep + fl)
    folders.reverse()
    for i in folders:
        os.removedirs(i)


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


def generatePDF(dictOfClass, objectName):
    # objectName = os.getcwd().split(sep)[-1]
    for key, val in dictOfClass.items():
        cell = 0
        count = 0
        page = newPage.drawPage()
        for v in val:
            cell += 1
            count += 1
            if cell == 1:
                page = newPage.drawPage()
                page.drawNameObject(objectName)
                page.drawOfKlass(key)
            sizeV = len(v.split("_"))
            if sizeV <= 7:
                page.drawProductParametrs(v, cell)
            elif sizeV > 7:
                page.drawProductParametrsWithPrice(v, cell)
            page.addImg(cell, tmpDir + sep + v)
            if cell == 4 or count == len(val):
                page.savePage(objectName)
                page.__init__()
                cell = 0


def removeOldPdf(pdfFlName, folder):
    pdfFl = searchFl("pdf", folder)
    if pdfFlName in pdfFl:
        os.remove(folder + os.sep + pdfFlName)     


def pyMain(folder='/media/work_part/python/Ижевск 40 ш 1в досьемка/'):
    os.chdir(folder)
    createTmpDir()
    psdFl = searchFl("psd", folder)
    convertPsd(psdFl, tmpDir)
    jpgFl = searchFl("jpeg", tmpDir)
    dictOfClass = createDictClass(jpgFl)
    generatePDF(dictOfClass)
    removeTmpDir()

if __name__ == "__main__":
    pyMain()
