import matplotlib.pyplot as plt
import math

sup = [2*math.pi] * 100 #супремум, найденный аналитическим путем
inf = [0] * 100 #инфинум, найденный аналитическим путем
epsilon = 1 #заданный эпсилон
n_0 = int(math.pi // epsilon + 1) #находим n_0 по формуле, полученной в аналитической части
coord = 0 #значение x_m, начиная с которого x_m > sup - эпсилон

for n in range(1, 10**6):
    m = (2*n-1)/n * math.acos((-1)**n) #определяем значение x_m 
    if m > (sup[0] - epsilon):
        coord = n 
        break

plt.figure(figsize=(20, 10)) #задаем размер окна

plt.subplot(3, 1, 1)
plt.title("Задание №1 и №4")
plt.xlabel("n", fontsize=14)
plt.ylabel("x_n", fontsize=14)
plt.plot([(2*n-1)/n * math.acos((-1)**n) for n in range(1, max(101, coord + 1))], marker='o', linestyle='None', color='b', label='последовательность x_n') #вывод последовательности x_n
plt.plot([0 for i in range(max(101, coord + 1))], linestyle='-', color='r',label='инфинум') #вывод инфинума и нижнего предела последовательности
plt.plot([2*math.pi for i in range(max(101, coord + 1))], linestyle='-', color='r', label='супремум') #вывод супремума, предела и верхнего предела последовательнсти
plt.scatter(coord, m, color='g', s=100, zorder=3, label='x_m') #точка, начиная с которой x_m > sup - эпсилон
plt.legend()
plt.grid()

plt.subplot(3, 1, 2)
plt.title("Задание №2")
plt.xlabel("n", fontsize=14)
plt.ylabel("x_n", fontsize=14)
for n in range(1, 101): #выводим первые 100 точек подпоследовательности
    if n % 2 == 0: #пропускаем точки последовательноси кратные 2
        if n == 2: #блок для корректного отображения легенды на графике
            plt.scatter(1, math.pi, marker=None, color='y', label='последовательность при n кратным 2')
        else:
            plt.scatter(1, math.pi, marker=None, color='y')
    else:
        plt.scatter(n, (2*n-1)/n * math.pi, color='y', marker='o') #вывод подпоследовательности x_n при n не ратным 2
plt.legend()
plt.grid()

plt.subplot(3, 1, 3)
plt.title("Задание №3")
plt.xlabel("n", fontsize=14)
plt.ylabel("x_n", fontsize=14)
for n in range(n_0, n_0 + 101): #вывод подпоследовательности, начиная с n_0
    if n % 2 == 0: #пропускаем точки кратные 2
        plt.scatter(n_0, math.pi, alpha=0)
    else: #выводим подпоследовательность x_n при n не кратным 2, начиная с n_0
        if n == n_0 + 1: #блок для корректного отображения легенды на графике
            plt.scatter(n, (2 * n - 1) / n * math.pi, color='y', marker='o', label='подпоследовательность с n_0')
        else:
            plt.scatter(n, (2 * n - 1) / n * math.pi, color='y', marker='o')
plt.plot([n_0, n_0+101], [2*math.pi, 2*math.pi], color='r') #предел последовательности
plt.legend()
plt.grid()

plt.subplots_adjust(hspace=0.5)
plt.show()

