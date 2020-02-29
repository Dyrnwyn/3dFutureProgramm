from PIL import Image, ImageDraw, ImageFont
#11
fontPath = "C:\\Users\\pod\\AppData\\Local\\Microsoft\\Windows\\Fonts\\a_Futurica.ttf"


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
        self.draw.line([(60, 400), (2420, 400)], fill=0, width=5)
        self.draw.line([(60, 1924), (2420, 1924)], fill=0, width=5)
        self.draw.line([(60, 3448), (2420, 3448)], fill=0, width=5)
        # -------------vertical line----------------------
        self.draw.line([(2420, 400), (2420, 3448)], fill=0, width=5)
        self.draw.line([(1210, 400), (1210, 3448)], fill=0, width=5)
        self.draw.line([(60, 400), (60, 3448)], fill=0, width=5)
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
        self.changeFont(fontSize=45)
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

    def drawLastName(self, lastName,numbCell):
        self.changeFont(fontSize=40)
        dictXY = {1: (80, 400),
                  2: (1220, 400),
                  3: (80, 1925),
                  4: (1220, 1925)
                  }
        self.draw.text(dictXY[numbCell], lastName, font=self.font, fill=0)
        self.changeFont(fontSize=45)

    def drawIdInformation(self, numbCell, idClient):
        self.changeFont(fontSize=25)
        dictXY = {1: (525, 1400),
                  2: (1725, 1398),
                  3: (525, 2950),
                  4: (1725, 2950)
                  }
        dictXYid = {1: (802, 1550),
                    2: (2002, 1548),
                    3: (802, 3100),
                    4: (2002, 3100)
                    }
        dictXYidNmbr = {1: (73, 1710),
                        2: (1223, 1710),
                        3: (73, 3258),
                        4: (1223, 3258)
                        }
        textInformation = ("Возможна безналичная оплата без комиссиии %" + "\n"
            "- с карт Сбербанка, в том числе и кредитных!" + "\n"
            "- через любой банкомат Сбербанка" + "\n"
            "Для оплаты:" + "\n"
            "1. В меню поиска организаций введите наш ИНН 2464105021" + "\n"
            "2. Введите номер изделия     (лицевой счет)" + "\n"
            "3. Проверьте правильность заказа" + "\n"
            "4. Произведите оплату" + "\n"
            "Изделия можно будет забрать через 5 дней после оплаты" + "\n"
            "Подробная инструкция по оплате: \nhttp://ОбъемныйМир.рф/parents/oplata"
            )
        textID = "ID*"
        idNmbr = "ID: " + idClient 
        self.draw.text(dictXY[numbCell],  textInformation, font=self.font, fill=0)
        self.draw.text(dictXYid[numbCell],  textID, font=self.font, fill=(255, 0, 0))
        self.changeFont(fontSize=45)
        self.draw.text(dictXYidNmbr[numbCell],  idNmbr, font=self.font, fill=(255, 0, 0))

    def drawCost(self, numbCell, cost):
        dictXYidNmbr = {1: (73, 1652),
                        2: (1223, 1652),
                        3: (73, 3198),
                        4: (1223, 3203)
                        }
        costTxt = "Сумма: " + cost
        self.draw.text(dictXYidNmbr[numbCell],  costTxt, font=self.font, fill=(255, 0, 0))
        

    def drawSites(self, numbCell):
        
        dictXY = {1: (530, 1800),
                  2: (1725, 1800),
                  3: (530, 3330),
                  4: (1725, 3330)
                }
        sites = ("vk.com/omfoto_ru" + "\n"
                "ОбъемныйМир.рф/parents"
                )
        self.draw.text(dictXY[numbCell],  sites, font=self.font, fill=(25,0,200))



    def drawProductParametrsWithPrice(self, flName, numbCell=1):
        self.changeFont(fontSize=45)

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
            if "[" in number:
                number = number[1:-1]
            cost = splitFlName[8]
            idClient = splitFlName[7]
            lastName = splitFlName[9]
            if "Кружка" in proportions:
               proportions = "Кружка-термос"
            if ("Настенный кален" in proportions) and (idClient != "id"):
               proportions = "Настенный к."
        except IndexError:
            species = proportions = template = photo = number = cost = idClient = lastName = " "
        if lastName != "" and not lastName.isdigit():
            self.drawLastName(lastName, numbCell)
        dictXY = {1: (70, 1400),
                  2: (1220, 1400),
                  3: (70, 2950),
                  4: (1220, 2950)
                  }
        parametrs = ("Вид: " + species + "\n" +
                     "Размер: " + proportions + "\n" +
                     "Шаблон: " + template + "\n" +
                     "Фото: " + photo + "\n" +
                     "Кол-во: " + number + "\n" 
                     )
        self.drawCost(numbCell,cost)
        if idClient != "id":
            self.drawIdInformation(numbCell, idClient)        
        self.draw.text(dictXY[numbCell], parametrs, font=self.font, fill=0)
        self.drawSites(numbCell)

    def addImg(self, cell, imgPath):
        # метод вывода фото изделия в ячейки 
        dictXY = {1: (220, 475),
                  2: (1370, 475),
                  3: (220, 1975),
                  4: (1370, 1975)
                  }
        img = Image.open(imgPath)
        self.page.paste(img, dictXY[cell])

    def savePage(self, nameObject):
        # Добавляем страницу в pdf файл, если файла нет, создаем его
        try:
            self.page.save(nameObject + ".pdf", append=True, resolution=300)
        except FileNotFoundError:
            self.page.save(nameObject + ".pdf", resolution=300)
        except PermissionError as e:
            fl_object = open(pypreviewer_err.txt, w)
            fl_object.write(e)
            fl_object.close()


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
