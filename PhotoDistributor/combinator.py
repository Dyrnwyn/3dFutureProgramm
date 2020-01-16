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
    """Создаем списки фотографий 10х15, 15х20, 20х30"""
    fl = open(txtFl[0], 'r', encoding='cp1251')
    photo = []  # Список фото
    for line in fl:
        if line[1] == '$':
            photo.append(line.split(';')[5])
    return photo


def sortphoto(photo, dirPhoto):
    """Функция копирования фотографий 10х15 в отдельную папку"""
    os.mkdir(dirPhoto)
    for i in photo:
        os.system('copy ' + i + '.jpg ' + '"' + dirPhoto + '"')
