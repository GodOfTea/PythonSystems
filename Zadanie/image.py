# Подключение библиотек
import random as rand
from PIL import Image, ImageDraw
import cv2

# Настройки
img = Image.open("pyt.jpg")
draw = ImageDraw.Draw(img)
width = img.size[0]
height = img.size[1]
pix = img.load()

# Добавляем шум
for i in range(width):
    for j in range(height):
        rnd = rand.randint(-70, 70) # чем больше значение, тем больше шум
        a = pix[i, j][0] + rnd
        b = pix[i, j][1] + rnd
        c = pix[i, j][2] + rnd
        if a < 0:
            a = 0
        elif a > 255:
            a = 255
        if b < 0:
            b = 0
        elif b > 255:
            b = 255
        if c < 0:
            c = 0
        elif c > 255:
            c = 255

        draw.point((i, j), (a, b, c))

img.save("noise.png", "PNG")
del draw

