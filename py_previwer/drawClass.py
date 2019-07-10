from PIL import Image, ImageDraw, ImageFont


class drawPage(object):
    """docstring for drawPage"""

    def __init__(self, fontName="Font/a_Futurica.ttf"):
        # Инициализируем новый лист, шрифт
        self.page = Image.new("RGB", (2480, 3508), color=(255, 255, 255))
        self.draw = ImageDraw.Draw(self.page, "RGB")
        self.font = ImageFont.truetype(fontName, 40)

    def changeFont(self, fontName="Font/a_Futurica.ttf", fontSize=40):
        self.font = ImageFont.truetype(fontName, fontSize)

    def drawLinePage(self):  # Метод рисования линий на листе
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
        #  Метод в котором пишем в заголовке
        # "класс/группа" и "Наименование объекта"
        self.draw.text((60, 30), "класс/группа", font=self.font, fill=0)
        fontWidth = self.font.getsize("Наименование Объекта")[0]
        self.draw.text((self.page.width / 2 - fontWidth / 2, 30),
                       "Наименование Объекта", font=self.font, fill=0)

    def drawNameObject(self, nameObject="Без имени"):
        fontWidth = self.font.getsize(nameObject)[0]
        self.draw.text((self.page.width / 2 - fontWidth / 2, 100),
                       nameObject, font=self.font, fill=0)

    def drawOfKlass(self, nameKlass="00"):
        # Рисуем класс/группу
        self.draw.text((60, 100), nameKlass, font=self.font, fill=0)

    def drawProductParametrs(self, numbCell=1):
        dictXY = {1: (70, 1500),
                  2: (1220, 1500),
                  3: (1220, 3050),
                  4: (70, 3050)
                  }
        parametrs = ("Вид: плоска\n" +
                     "Размер: 10х15\n" +
                     "Шаблон: 2401\n" +
                     "Фото: 6546\n" +
                     "Кол-во: 10\n"
                     )
        self.draw.text(dictXY[numbCell], parametrs, font=self.font, fill=0)

    def savePage(self):
        self.page.save("1.jpg")


if __name__ == "__main__":
    page1 = drawPage()
    page1.drawLinePage()
    page1.drawTitle()
    page1.changeFont(fontSize=100)
    page1.drawNameObject("Новосибирск 111221")
    page1.drawOfKlass("7б класс")
    page1.changeFont(fontSize=60)
    page1.drawProductParametrs(3)
    page1.savePage()
