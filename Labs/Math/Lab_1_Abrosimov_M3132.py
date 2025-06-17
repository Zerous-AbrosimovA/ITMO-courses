import matplotlib.pyplot as plt
import numpy as np
from random import uniform
import pandas as pd

# Данная по условию функция
def f(n):
    return n ** 2 + n - 1

# Ввод пользователем мелкости разбиения отрезка
lambda_n = int(input())
# Длина отрезка между x_i и x_i+1
delta_x = 5 / lambda_n
# интегральная сумма для левого оснащения
l_s = 0
# интегральная сумма для правого оснащения
r_s = 0
# интегральная сумма для среднего оснащения
m_s = 0
# интегральная сумма для случайного оснащения
rand_s = 0
# массив для значения нижней суммы Дарбу на отрезке от x_i до x_i+1
darbu_s = []
# массив для значения верхней суммы Дарбу на отрезке от x_i до x_i+1
darbu_S = []
# массив для площади трапеции между точка x_i и x_i+1
int_value = []

# массив, в котором содержатся значения ξ_i для вычисления интегральной суммы
# с левым оснащением, их количество зависит от мелкости разбиения
ksi_l = np.linspace(-2.0, 3 - delta_x, lambda_n)
# массив, в котором содержатся значения ξ_i для вычисления интегральной суммы
# с правым оснащением, их количество зависит от мелкости разбиения
ksi_r = np.linspace(-2 + delta_x, 3.0, lambda_n)
# массив, в котором содержатся значения ξ_i для вычисления интегральной суммы
# со средним оснащением, их количество зависит от мелкости разбиения
ksi_m = np.linspace(-2 + delta_x / 2, 3 - delta_x / 2, lambda_n)
# массив, в котором содержатся значения ξ_i для вычисления интегральной суммы
# со случайным оснащением, их количество зависит от мелкости разбиения
ksi_rand = [uniform(-2 + i * delta_x, -2 + (i + 1) * delta_x) for i in range(lambda_n)]

# подсчет интегральной суммы для левого оснащения
for x in ksi_l:
    l_s += f(x) * delta_x
# подсчет интегральной суммы для правого оснащения
for x in ksi_r:
    r_s += f(x) * delta_x
# подсчет интегральной суммы для среднего оснащения
for x in ksi_m:
    m_s += f(x) * delta_x
# подсчет интегральной суммы для случайного оснащения
for x in ksi_rand:
    rand_s += f(x) * delta_x

# вычисление сумм Дарбу и площади трапеции на отрезке от x_i до x_i+1
for x1, x2 in zip(ksi_l, ksi_r):
    darbu_s.append(min(f(x1), f(x2)))
    darbu_S.append(max(f(x1), f(x2)))
    int_value.append((f(x1) + f(x2)) / 2 * (x2 - x1))

# вывод результатов подсчетов в табличку для пункта 3
print(pd.DataFrame({"Variable": ["λ(τ_n)", "σ(f, ξ_left)", "σ(f, ξ_right)", "σ(f, ξ_mid)", "σ(f, ξ_random)", "I^*", "I_*", "trap_int"], "Value":
    [lambda_n, l_s, r_s, m_s, rand_s, sum(darbu_S) * delta_x, sum(darbu_s) * delta_x, sum(int_value)]}))
# Pre: true
# Inv: Sorry, you lost
# Post: dopsa
x = np.linspace(-2, 3, 1000)
plt.figure(figsize=(20, 20))
plt.title("График функции f(x) и интегральные суммы")
# График интегральных сумм с левым оснащением
plt.subplot(6, 1, 1)
plt.plot(x, f(x), color="r", linewidth=3, zorder=2, label="f(x)")
plt.bar(ksi_l, f(np.array(ksi_l)), width=delta_x, align="edge", alpha=0.5, color="b", label="Левое оснащение")
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right')
# График интегральных сумм с правым оснащением
plt.subplot(6, 1, 2)
plt.plot(x, f(x), color="r", linewidth=3, zorder=2, label="f(x)")
plt.bar(ksi_l, f(np.array(ksi_l)), width=delta_x, align="edge", alpha=0.5, color="b", label="Правое оснащение")
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right')
# График интегральных сумм со средним оснащением
plt.subplot(6, 1, 3)
plt.plot(x, f(x), color="r", linewidth=3, zorder=2, label="f(x)")
plt.bar(ksi_l, f(np.array(ksi_l)), width=delta_x, align="edge", alpha=0.5, color="b", label="Среднее оснащение")
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right')
# График интегральных сумм со случайным оснащением
plt.subplot(6, 1, 4)
plt.plot(x, f(x), color="r", linewidth=3, zorder=2, label="f(x)")
plt.bar(ksi_l, f(np.array(ksi_l)), width=delta_x, align="edge", alpha=0.5, color="b", label="Случайные точки")
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right')
plt.subplot(6, 1, 5)
# Вывод графика f(x)
plt.plot(x, f(x), color="r", zorder=2, linewidth=3)
# Вывод ступенчатых фигур для нижней суммы Дарбу
plt.step(ksi_l, darbu_s, where="post", color="b", linewidth=2, label="Нижняя сумма Дарбу")
# Вывод ступенчатых фигур для верхней суммы Дарбу
plt.step(ksi_l, darbu_S, where="post", color="g", linewidth=2, label="Верхняя сумма Дарбу")
# Блок для включения точки x = 3 в вывод ступенчатых фигур
ksi_l_extend = np.append(ksi_l, 3)
darbu_s = np.append(darbu_s, darbu_s[-1])
darbu_S = np.append(darbu_S, darbu_S[-1])
plt.step(ksi_l_extend, darbu_s, where="post", color="b", linewidth=2)
plt.step(ksi_l_extend, darbu_S, where="post", color="g", linewidth=2)
plt.grid(True)
# Вывод осей и названия функции
plt.title("График функции f(x) и суммы Дарбу")
plt.xlabel('x')
plt.ylabel('y')
# Вывод легенды
plt.legend(loc='upper right')
plt.subplot(6, 1, 6)
# Вывод графика f(x)
plt.plot(x, f(x), color="r", zorder=2, linewidth=3)
# Вывод хорд, которые используются для подсчета площадей трапеций в методе трапеции
for i in range(len(ksi_l)):
    # Блок для корректного вывода легенды
    if i == 0:
        plt.plot([ksi_l[i], ksi_r[i]], [f(ksi_l[i]), f(ksi_r[i])], color="b", linestyle="--", linewidth=2, label="касательные для метода трапеции")
    # Вывод оставшихся точек
    else:
        plt.plot([ksi_l[i], ksi_r[i]], [f(ksi_l[i]), f(ksi_r[i])], color="b", linestyle="--", linewidth=2)
plt.grid(True)
# Вывод осей и названия функции
plt.title("График функции f(x) и хорды для метода трапеции")
plt.xlabel('x')
plt.ylabel('y')
# Вывод легенды
plt.legend(loc='upper right')
# Вывод всех графиков на одно полотно
plt.show()
