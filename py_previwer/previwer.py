import drawClass
import os
from psd_tools2 import PSDImage
import re
from PIL import Image

tmpDir = 'tmp'


def searchFl(flExt, fldr=""):
    filteredFlList = []
    with os.scandir(fldr) as flList:
        for fl in flList:
            if not fl.name.startswith('.') and fl.is_file() and \
                    re.findall(r"^.*\." + flExt + "*", fl.name):
                filteredFlList.append(fl.name)
    return filteredFlList


def convertPsd(psdFl, tmpDir):
    for psdFlName in psdFl:
        psd = PSDImage.open(psdFlName)
        psd.compose().save(tmpDir + "/" + "tmp_file.png")
        pngFl = Image.open(tmpDir + "/" + "tmp_file.png")
        rgb_png = pngFl.convert("RGB")
        xsize, ysize = rgb_png.size
        jpgFl = rgb_png.resize((round(xsize / 3), round(ysize / 3)))
        jpgFl.save(tmpDir + "/" + psdFlName[0:-4] + ".jpeg")
    os.remove(tmpDir + "/" + "tmp_file.png")


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
            os.remove(i[0] + '/' + fl)
    folders.reverse()
    for i in folders:
        os.removedirs(i)


def createDictClass(flList):
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
                if key == "Класс":
                    val.append(fl)
    return clssList


def generatePDF(dictOfClass):
    for key, val in dictOfClass.items():
        cell = 0
        count = 0
        page = drawClass.drawPage()
        for v in val:
            cell += 1
            count += 1
            if cell == 1:
                page = drawClass.drawPage()
                page.drawNameObject("Иркутск")
                page.drawOfKlass(key)
                page.changeFont(fontSize=60)
            page.drawProductParametrs(cell)
            page.addImg(tmpDir + "/" + v, cell)
            if cell == 4 or count == len(val):
                page.savePage()
                page.__init__()
                cell = 0


def pyMain(folder='/media/work_part/python/Ижевск 40 ш 1в досьемка/'):
    os.chdir(folder)
    #createTmpDir()
    #psdFl = searchFl("psd")
    #convertPsd(psdFl, tmpDir)
    jpgFl = searchFl("jpeg", "tmp")
    dictOfClass = createDictClass(jpgFl)
    generatePDF(dictOfClass)
    # removeTmpDir()


if __name__ == "__main__":
    pyMain()
