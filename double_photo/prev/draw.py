from PIL import Image, ImageDraw, ImageFont


def newPage():
    page = Image.new("RGB", (2480, 3508), color=(255, 255, 255))
    return page


def drawLinePage(page):
    draw = ImageDraw.Draw(page, "RGB")
#
# -------------horizontal line---------------
    draw.line([(60, 400), (2420, 400)], fill=0, width=7)
    draw.line([(60, 1924), (2420, 1924)], fill=0, width=7)
    draw.line([(60, 3448), (2420, 3448)], fill=0, width=7)
# -------------vertical line----------------------
    draw.line([(2420, 400), (2420, 3448)], fill=0, width=7)
    draw.line([(1210, 400), (1210, 3448)], fill=0, width=7)
    draw.line([(60, 400), (60, 3448)], fill=0, width=7)
    draw.text((60, 40), "Class")
    return page


def drawTitle(page):
    draw = ImageDraw.Draw(page, "RGB")
    font = ImageFont.truetype("Font/a_Futurica.ttf", 40)
    draw.text((60, 30), "класс/группа", font=font, fill=0)
    fontWidth = font.getsize("Наименование Объекта")[0]
    draw.text((page.width / 2 - fontWidth / 2, 30),
              "Наименование Объекта", font=font, fill=0)
    return page


def drawNameObject(page, nameObject):



def drawPage():
    page = newPage()
    page = drawLinePage(page)
    page = drawTitle(page)
    page.save("1.jpg")


if __name__ == "__main__":
    drawPage()
