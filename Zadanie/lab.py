import math
import random
import matplotlib.pyplot as plt
import numpy
from numpy.fft import fft
from numpy.random import normal

n = 1
x1 = []
x2 = []
x3 = []
x4 = []
x = []
xn = []

while n <= 500:
    xx = math.sin(2*math.pi*n/100)
    x1.append(xx)
    xx = 4*math.exp(-1*((n-150)**2)/300) - math.exp(-1*((n-150)**2)/2500)
    x2.append(xx)
    if 240 < n < 300:
        x3.append(1)
    elif 299 < n < 380:
        x3.append(-2)
    else:
        x3.append(0)
    v = (1 / (math.sqrt(2*math.pi))) * math.e ** -1*((n**2)/2)
    #xx = normal(0,1) + normal(0,1) + normal(0,1) + normal(0,1) + normal(0,1) + normal(0,1) - 3
    xx = random.random() + random.random() + random.random() + random.random() + random.random() + random.random() - 3
    x4.append(xx)
    n += 1

# fig = plt.figure()   # Создание объекта Figure
# plt.title('sin(2*π*n/100)')
# plt.plot(x1)
# plt.grid(True)
# plt.xlabel('n')
# plt.ylabel('x1[n]')
# fig = plt.figure()
# plt.plot(x2)
# plt.title('4*exp(-(n-150)^2/300)-exp(-(n-150)^2/2500)')
# plt.grid(True)
# plt.xlabel('n')
# plt.ylabel('x2[n]')
# fig = plt.figure()
# plt.plot(x3)
# plt.title('Ступенчатая функция')
# plt.grid(True)
# plt.xlabel('n')
# plt.ylabel('x3[n]')
# fig = plt.figure()
# plt.plot(x4)
# #plt.title('Нормальное распределение')
# plt.title('Равномерное распределение')
# plt.grid(True)
# plt.xlabel('n')
# plt.ylabel('x4[n]')

for number in range(0, 500):
    xx = x1[number] + x2[number] + x3[number] + x4[number]
    xn.append(xx)

# fig = plt.figure()
# plt.plot(xn)
# plt.title('Суммарная последовательность')
# plt.grid(True)
# plt.xlabel('n')
# plt.ylabel('x[n]')


yn = []
y1 = []
y2 = []
y3 = []
y4 = []
n = 1

yn.append(0)
y1.append(0)
y2.append(0)
y3.append(0)
y4.append(0)

while n < 500:
    yn.append(0.05 * xn[n] + 0.95 * yn[n - 1])
    y1.append(0.05 * x1[n] + 0.95 * y1[n - 1])
    y2.append(0.05 * x2[n] + 0.95 * y2[n - 1])
    y3.append(0.05 * x3[n] + 0.95 * y3[n - 1])
    y4.append(0.05 * x4[n] + 0.95 * y4[n - 1])
    n += 1

ysub = []

for number in range(0, 500):
    sub = yn[number] - (y1[number] + y2[number] + y3[number] + y4[number])
    ysub.append(sub)

plt.figure()
plt.title('y1[n]=0.05*x1[n]+0.95*y1[n-1]')
plt.plot(y1)
plt.grid(True)
plt.xlabel('n')
plt.ylabel('y1[n]')

fig = plt.figure()
plt.plot(y2)
plt.title('y2[n]=0.05*x2[n]+0.95*y2[n-1]')
plt.grid(True)
plt.xlabel('n')
plt.ylabel('y2[n]')
fig = plt.figure()
plt.plot(y3)
plt.title('y3[n]=0.05*x3[n]+0.95*y3[n-1]')
plt.grid(True)
plt.xlabel('n')
plt.ylabel('y3[n]')
fig = plt.figure()
plt.plot(y4)
plt.title('y4[n]=0.05*x4[n]+0.95*y4[n-1]')
plt.grid(True)
plt.xlabel('n')
plt.ylabel('y4[n]')

fig = plt.figure()
plt.subplot(2, 1, 1)
plt.title('y[n]')
plt.plot(yn)
plt.grid(True)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.subplot(2, 1, 2)
plt.title('y[n] - (y1[n]+y2[n]+y3[n]+y4[n]')
plt.plot(ysub)
plt.grid(True)
plt.xlabel('n')
plt.ylabel('y sub')

hn = [1/25, 2/25, 3/25, 4/25, 5/25, 4/25, 3/25, 2/25, 1/25]
z = []
z = numpy.convolve(xn, hn)

fig = plt.figure()
plt.plot(z)
plt.grid(True)
plt.title('Cвертка сигнала x[n]')
plt.ylabel('Значения сигнала')
plt.xlabel('Отсчеты')

# len = 1024 - len(xn)
# for zero in range(0, len):
#     xn.append(0)
#
# new = fft(xn)

# fig = plt.figure()
# plt.plot(new)
# plt.grid(True)
# plt.title('ДПФ Сигнала')
# plt.ylabel('Амплитуда спектра тут')
# plt.xlabel('1024 отсчета')

# H = []
# for zero in range(0, 1015):
#     hn.append(0)
# for number in range(0,1024):
#     H.append(hn[number] * xn[number])

plt.figure()
plt.plot(fft(hn))
plt.hlines(0.1, 0, 1024, colors='g', linestyles='--', label="зона непрозрачности")
plt.hlines(0.9, 0, 1024, colors='r', linestyles='--', label="полоса пропускания")
plt.title("Частнотная характеристика")
plt.legend()
