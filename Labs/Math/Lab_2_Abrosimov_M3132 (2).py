from math import *
import matplotlib.pyplot as plt
import numpy as np
# @author Georgiy Korneev (kgeorgiy@kgeorgiy.info)
def f(x, n): # функция для вычисления многочлена Тейлора n-ой степени
    f = 0
    for k in range(n+1):
        f += (sin(pi/6 + pi*k/2)/factorial(k)) * x ** k
    return f


def g(x): # функция для вычисления значений данной по условию функции
    return np.sin(np.pi/6 + x)


n2 = 3 # наибольшая степень для многочлена Тейлора, полученная в аналитической части
x = np.linspace(-1, 1, 1000)
plt.figure(figsize=(20, 20))
plt.plot(x, g(x), color='r', zorder=2, linewidth=3) # вывод заданной в условие функции
for n in range(1, n2+1):
    plt.plot(x, f(x, n), color='b', zorder=1) # вывод многочлена Тейлора до n2 степени включительно
plt.grid(color='black', linewidth=0.5)
plt.title('График функции f(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['sin(pi/6+x)', 'Многочлен Тейлора n-ого порядка'], loc='lower right') # вывод легенды
plt.show()

print("Приближенное значение f(x) = sin(pi/6 + x) в точке x = 0.05 "
      "при замене на многочлен Тейлора 2 порядка")
x = 0.05
P_2 = 1/2 + (sqrt(3) / 2) * x - 1/4 * x**2
print(P_2)
print("Приближенное значение f(x) = sin(pi/6 + x) в точке x = 0.05 "
      "при замене на многочлен Тейлора 3 порядка")
P_3 = 1/2 + (sqrt(3) / 2) * x - 1/4 * x**2 - (sqrt(3) / 12) * x ** 3
print(P_3)
print("Точное значение f(x) = sin(pi/6 + x) в точке x = 0.05 ")
print(sin(pi/6 + x))

