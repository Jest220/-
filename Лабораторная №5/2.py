import matplotlib.pyplot as plt
from random import random

#список случайных элементов
y = [random() * 10 for i in range(100)]
leny = len(y)
#ось x
x = [random() * 10 for i in range(100)]
#вычисление математического ожидания
leny = len(y)
mathWait = 0
dmathWait = {}
for i in y:
    if not i in dmathWait:
        dmathWait[i] = 1
    else:
        dmathWait[i] += 1
for i in dmathWait.keys():
    mathWait += i * dmathWait[i] / leny

#вычисление среднеквадратического отклонения
##вычисление дисперсии
disp = 0
for i in y:
    disp += (i - mathWait) * (i - mathWait)
disp /= leny
##вычисление
standardDeviation = disp**0.5

#построение линейной регрессии
plt.scatter(x, y)
##среднее значение x
averagex = 0
for i in x:
    averagex += i
averagex /= leny
##среднее значение y
averagey = 0
for i in y:
    averagey += i
averagey /= leny
##среднее значение x * y
averagexy = 0
for i in range(leny):
    averagexy += x[i] * y[i]
averagexy /= leny

##среднее значение x^2
averagex2 = 0
for i in x:
    averagex2 += i * i
averagex2 /= leny
##коэффициент b
b = (averagexy - averagex * averagey) / (averagex2 - averagex**2)
##коэффициент a
a = averagey - b * averagex

##построение прямой
plt.plot(x, [a + b * i for i in x])
plt.show()
