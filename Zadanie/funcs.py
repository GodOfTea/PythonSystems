# Лабораторная работа #1. Задание 3.5.1.

# Графическая библиотека
import matplotlib.pyplot as plt
import random
import numpy.random as rand
from math import sin
from math import pi
from math import exp
from numpy import convolve
from numpy import real
from numpy.fft import fft
from numpy.fft import ifft
from PIL import Image, ImageDraw
import scipy.signal as sig
import scipy.ndimage.filters as nd

xn1 = []
xn2 = []
xn3 = []
xn4 = []

yn = []
ynDelta = []

yn1 = []
yn2 = []
yn3 = []
yn4 = []

xn = []
conv = []
XnConv = []
X = []

n = 500
max = 0

h = [1/25, 2/25, 3/25, 4/25, 5/25, 4/25, 3/25, 2/25, 1/25]
H = []
XH = []
delXH = []

# рандом
def rnd():
    return random.random()

def normrnd():
    return rand.normal(0, 1)

#  заполенеие x1 - x4 и y1 - y4
def fillLists():
    yn1.append(0)
    yn2.append(0)
    yn3.append(0)
    yn4.append(0)
    for i in range(n+1):
        xi = sin(2*pi*i/100)
        xn1.append(xi)
        yi = 0.05 * xn1[i] + 0.95 * yn1[i - 1]
        yn1.append(yi)

        xi = 4*exp(-(i-150)**2/300) - exp(-(i-150)**2/2500)
        xn2.append(xi)
        yi = 0.05 * xn2[i] + 0.95 * yn2[i - 1]
        yn2.append(yi)

        if 240 < i < 300:
            xn3.append(1)
        elif 299 < i < 380:
            xn3.append(-2)
        else:
            xn3.append(0)

        yi = 0.05 * xn3[i] + 0.95 * yn3[i - 1]
        yn3.append(yi)

        xi = rnd() + rnd() + rnd() + rnd() + rnd() + rnd() - 3
        # xin = normrnd() + normrnd() + normrnd() + normrnd() + normrnd() + normrnd() - 3
        xn4.append(xi)
        yi = 0.05 * xn4[i] + 0.95 * yn4[i - 1]
        yn4.append(yi)

# заполнение xn
def mergerFuncs():
    for i in range(n+1):
        xi = xn1[i] + xn2[i] + xn3[i] + xn4[i]
        xn.append(xi)

# заполнение yn и ynDelta
def ynMergerFunc():
    yn.append(0)
    ynDelta.append(0)
    for i in range(1, n+1):
        yi = 0.05 * xn[i] + 0.95 * yn[i - 1]
        yn.append(yi)

        yi = yn[i] - (yn1[i] + yn2[i] + yn3[i] + yn4[i])
        ynDelta.append(yi)

def convolution():
    conv = convolve(xn, h)
    for i in range(len(conv)):
        XnConv.append(conv[i])
    val = real(fft(xn, 1024))
    for i in range(len(val)):
        X.append(val[i])
    val = real(fft(h, 1024))
    for i in range(len(val)):
        H.append(val[i])
    for i in range(1024):
        XH.append(H[i]*X[i])

def compare():
    cmp = []
    r = (real(ifft(XH)))
    for i in range(len(XnConv)):
        delXH.append(r[i])
    for i in range(len(XnConv)):
         cmp.append(abs(delXH[i] - XnConv[i]))
    return cmp

# вывод графиков
def draw():
    plt.figure()
    plt.subplot(4, 1, 1)
    plt.plot(xn1)
    plt.title("x1 = sin(2*pi*n/100)")
    plt.ylabel("x(n)")
    plt.xlabel("n")

    plt.subplot(4, 1, 2)
    plt.plot(xn2)
    plt.title("x2 = 4*exp(-(i-150)^2/300) - exp(-(i-150)^2/2500)")
    plt.ylabel("x(n)")
    plt.xlabel("n")

    plt.subplot(4, 1, 3)
    plt.plot(xn3)
    plt.title("Ступенчатая функция")
    plt.ylabel("x(n)")
    plt.xlabel("n")

    plt.subplot(4, 1, 4)
    plt.plot(xn4)
    plt.title("Функция со сулчайными значениями")
    plt.ylabel("x(n)")
    plt.xlabel("n")
    plt.show()

    plt.figure()
    plt.plot(xn)
    plt.title("Суммарная последовательность")
    plt.xlabel("n")
    plt.ylabel("x(n)")
    plt.show()

    plt.figure()
    plt.subplot(4, 1, 1)
    plt.plot(yn1)
    plt.title("y1 = 0.05 * x1[n] + 0.95 * y[n - 1]")
    plt.xlabel("n")
    plt.ylabel("y(n)")

    plt.subplot(4, 1, 2)
    plt.plot(yn2)
    plt.title("y2 = 0.05 * x2[n] + 0.95 * y[n - 1]")
    plt.xlabel("n")
    plt.ylabel("y(n)")

    plt.subplot(4, 1, 3)
    plt.plot(yn3)
    plt.title("y3 = 0.05 * x3[n] + 0.95 * y[n - 1]")
    plt.xlabel("n")
    plt.ylabel("y(n)")

    plt.subplot(4, 1, 4)
    plt.plot(yn4)
    plt.title("y4 = 0.05 * x4[n] + 0.95 * y[n - 1]")
    plt.xlabel("n")
    plt.ylabel("y(n)")
    plt.show()

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(yn)
    plt.title("y = 0.05 * x[n] + 0.95 * y[n - 1]")
    plt.xlabel("n")
    plt.ylabel("y(n)")

    plt.subplot(2, 1, 2)
    plt.plot(ynDelta)
    plt.title("mY = y[n] - (y1[n] + y2[n] + y3[n] + y4[n])")
    plt.xlabel("n")
    plt.ylabel("y(n)")
    plt.show()

    plt.figure()
    plt.subplot(1, 2, 1)
    plt.plot(XnConv)
    plt.title("Свёртка x[n] по h[n]")
    plt.xlabel("n")
    plt.ylabel("x(n)")

    plt.subplot(1, 2, 2)
    plt.plot(xn)
    plt.title("X[n]")
    plt.xlabel("n")
    plt.ylabel("x(n)")
    plt.show()

    plt.figure()
    plt.plot(X)
    plt.title("Амплитуда спектра")
    plt.xlabel("n")
    plt.ylabel("x(n)")
    plt.show()

    plt.figure()
    plt.plot(H)
    plt.hlines(0.1*H[0], 0, 1024, colors='g', linestyles='--', label="зона непрозрачности")
    plt.hlines(0.9*H[0], 0, 1024, colors='r', linestyles='--', label="полоса пропускания")
    plt.title("Частнотная характеристика")
    plt.legend()
    plt.show()

    plt.figure()
    plt.subplot(2, 2, 1)
    plt.plot(XnConv)
    plt.title("Свёртка")
    plt.xlabel("n")
    plt.ylabel("x(n)")

    plt.subplot(2, 2, 2)
    plt.plot(real(ifft(XH)))
    plt.title("Обратная ДПФ")
    plt.xlabel("n")
    plt.ylabel("x(n)")

    plt.subplot(2, 2, 3)
    plt.plot(compare())
    plt.title("Их разница")
    plt.xlabel("n")
    plt.ylabel("x(n)")
    plt.show()

pix = []
def pict (): # загружаем картинку
    img = Image.open("pyt.jpg")
    draw = ImageDraw.Draw(img)
    width = img.size[0]
    height = img.size[1]
    pix = img.load()

    # Добавляем шум
    for i in range(width):
        for j in range(height):
            rnd = rand.randint(-70, 70)  # чем больше значение, тем больше шум
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

    # медианный фильтр
    mFil = sig.medfilt(img)
    f1_image = Image.fromarray(mFil.astype("uint8"))
    f1_image.save("median.png", "PNG")

    # фильтр Гаусса
    gFil = nd.gaussian_filter(img, 1)
    f3_image = Image.fromarray(gFil.astype("uint8"))
    f3_image.save("gauss.png", "PNG")
    del draw

# конец кода

# старт программы
fillLists()
mergerFuncs()
ynMergerFunc()
convolution()
draw()

pict()