import os
from psd_tools2 import PSDImage
import re
from PIL import Image


def searchPsd():
    psdList = []
    with os.scandir() as flList:
        for fl in flList:
            if not fl.name.startswith('.') and fl.is_file() and \
            re.findall(r"^.*\.psd*", fl.name):
                psdList.append(fl.name)
    return psdList


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


def createTmpDir(tmpFolder):
    try:
        os.mkdir(tmpFolder)
    except Exception as e:
        pass    
    return True


def removeTmpDir(tmpDir):
    for root, dirs, files in os.walk(folder + tmpFolder):
        for fl in files:
            os.remove(folder + tmpFolder + '/' + fl)
        for dr in dirs:
            os.removedirs(dirs)


def pyMain(folder='/media/work_part/python/Ижевск 40 ш 1в досьемка/'):
    os.chdir(folder)
    tmpDir = 'tmp'
    createTmpDir(tmpDir)
    psdFl = searchPsd()
    convertPsd(psdFl, tmpDir)


if __name__ == "__main__":
    pyMain()
