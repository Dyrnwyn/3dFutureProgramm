from PIL import Image, ImageDraw, ImageFont

fontPath = "/media/work_part/python/previewer/py_previwer/Font/a_Futurica.ttf"


class drawPage(object):
    """docstring for drawPage"""

    def __init__(self, fontName=fontPath):
        # Инициализируем новый лист, шрифт
        self.page = Image.new("RGB", (2480, 3508), color=(255, 255, 255))
        self.draw = ImageDraw.Draw(self.page, "RGB")
        self.font = ImageFont.truetype(fontName, 30)
        self.drawLinePage()
        self.drawTitle()
        self.changeFont(fontSize=100)

    def changeFont(self, fontName=fontPath, fontSize=40):
        self.font = ImageFont.truetype(fontName, fontSize)

    def drawLinePage(self):  # Разметка страницы на ячейки
        # -------------horizontal line--------------------
        self.draw.line([(60, 400), (2420, 400)], fill=0, width=7)
        self.draw.line([(60, 1924), (2420, 1924)], fill=0, width=7)
        self.draw.line([(60, 3448), (2420, 3448)], fill=0, width=7)
        # -------------vertical line----------------------
        self.draw.line([(2420, 400), (2420, 3448)], fill=0, width=7)
        self.draw.line([(1210, 400), (1210, 3448)], fill=0, width=7)
        self.draw.line([(60, 400), (60, 3448)], fill=0, width=7)
        self.draw.text((60, 40), "Class")

    def drawTitle(self):
        #  Метод в котором выводим в заголовке
        # "класс/группа" и "Наименование объекта"
        self.changeFont(fontSize=35)
        self.draw.text((60, 30), "класс/группа", font=self.font, fill=0)
        fontWidth = self.font.getsize("Наименование Объекта")[0]
        self.draw.text((self.page.width / 2 - fontWidth / 2, 30),
                       "Наименование Объекта", font=self.font, fill=0)

    def drawNameObject(self, nameObject="Без имени"):
        # В методе выводим название объекта
        self.changeFont(fontSize=70)
        fontWidth = self.font.getsize(nameObject)[0]
        self.draw.text((self.page.width / 2 - fontWidth / 2, 100),
                       nameObject, font=self.font, fill=0)

    def drawOfKlass(self, nameKlass="00"):
        # Рисуем класс/группу
        self.changeFont(fontSize=70)
        self.draw.text((60, 100), nameKlass, font=self.font, fill=0)

    def drawProductParametrs(self, flName, numbCell=1):
        # метод вывода информации об изделии
        # в ячейки
        # numbcell номер ячейки на листе, в который выводим данные
        self.changeFont(fontSize=30)
        splitFlName = flName.split("_")
        try:
            if splitFlName[0] == "о":
                species = "объемная"
            elif splitFlName[0] == "п":
                species = "плоская"
            else:
                species = " "
            proportions = splitFlName[1]
            template = splitFlName[2]
            photo = splitFlName[3]
            number = splitFlName[4]
        except IndexError:
            species = proportions = template = photo = number = " "
        dictXY = {1: (70, 1500),
                  2: (1220, 1500),
                  3: (70, 3050),
                  4: (1220, 3050)
                  }
        parametrs = ("Вид: " + species + "\n" +
                     "Размер: " + proportions + "\n" +
                     "Шаблон: " + template + "\n" +
                     "Фото: " + photo + "\n" +
                     "Кол-во:" + number + "\n"
                     )
        self.draw.text(dictXY[numbCell], parametrs, font=self.font, fill=0)

    def addImg(self, cell, imgPath):
        # метод вывода фото изделия в ячейки 
        dictXY = {1: (120, 425),
                  2: (1270, 425),
                  3: (120, 1950),
                  4: (1270, 1950)
                  }
        img = Image.open(imgPath)
        self.page.paste(img, dictXY[cell])

    def savePage(self, nameObject):
        # Добавляем страницу в pdf файл, если файла нет, создаем его
        try:
            self.page.save(nameObject + ".pdf", append=True, resolution=300)
        except FileNotFoundError:
            self.page.save(nameObject + ".pdf", resolution=300)


# if __name__ == "__main__":
#     for i in range(10):
#         page1 = drawPage()
#         # page1.drawLinePage()
#         # page1.drawTitle()
#         # page1.changeFont(fontSize=100)
#         page1.drawNameObject("Новосибирск 111221")
#         page1.drawOfKlass("7б класс")
#         page1.changeFont(fontSize=60)
#         page1.drawProductParametrs(4)
#         page1.addImg("/media/work_part/python/Ижевск 40 ш 1в досьемка/tmp/о_магнит 10х15_4030_7802_1_1в_H.jpeg", 4)
#         page1.savePage()
