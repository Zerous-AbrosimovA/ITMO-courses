import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time

# подсчет значения f в точке
def evaluate(x, y):
    return x**2*y**2*np.log(2*x**2+3*y**2)

# подсчет значения f'_x в точке
def evaluateF_x(x, y):
    return (4*x**3*y**2/(2*x**2 + 3*y**2)
            + 2*x*y**2*np.log(2*x**2 + 3*y**2))

# подсчет значения f'_y в точке
def evaluateF_y(x, y):
    return (6*x**2*y**3/(2*x**2 + 3*y**2)
            + 2*x**2*y*np.log(2*x**2 + 3*y**2))

# функция для нахождения локального минимума функции через градиентный спуск
def gradientDescent(startingPoint, a_k = 0.01, epsilon = 0.000001, maxIterations = 10000):
    # данная переменная хранит текущую координату (изначально координату (1;1))
    currentCoord = np.array(startingPoint, dtype = float)
    # массивы для хранения координат точек, получаемых в результате градиентного спуска
    xArray = np.array([])
    yArray = np.array([])
    # счетчик итераций
    iterations = 0
    for i in range(maxIterations):
        iterations += 1
        # добавляем текущую точку в массив (по координатно)
        xArray = np.append(xArray, currentCoord[0])
        yArray = np.append(yArray, currentCoord[1])
        # считаем значение градиента в данной точке
        currentGradient = np.array([evaluateF_x(currentCoord[0], currentCoord[1]), evaluateF_y(currentCoord[0], currentCoord[1])], dtype = float)
        # считаем норму текущего значения градиента, если она < epsilon, минимум найден (критерий останова)
        if np.linalg.norm(currentGradient) < epsilon:
            break
        # пересчитываем значение точки с учетом нормирующего коэффициента
        currentCoord -= a_k * currentGradient
    # возвращаем точку минимума и точки, через которые мы в нее пришли
    return currentCoord, xArray, yArray, iterations


# точка, полученная в аналитической части
point = np.array([(2 * np.pow(np.e, 1/4)) ** -1, (np.sqrt(6) * np.pow(np.e, 1/4)) ** -1])

# фиксация времени начала градиентного спуска
start = time.perf_counter()
# результат градиентного спуска
localMinimum, x1, y1, iterationsCount = gradientDescent([1, 1])
# фиксация времени, затраченного на поиск точки локального минимума
end = time.perf_counter() - start
# значения функции в точках, через которые мы пришли в минимум
z1 = evaluate(x1, y1)

# таблица с результатами
print(pd.DataFrame({"Требуемые значения": ["Критерий останова", "Число итераций", "Полученная точка", "Полученное значение функции", "Точное значение функции", "Время работы"], "Результаты":
    ["Норма значения градиента строго меньше ε = 1e-6", iterationsCount, localMinimum, evaluate(localMinimum[0], localMinimum[1]), evaluate(point[0], point[1]), end]}))

plt.figure(figsize=(8, 8))
pltX = np.linspace(-1, 1, 1000)
pltY = np.linspace(-1, 1, 1000)
X, Y = np.meshgrid(pltX, pltY)
Z = evaluate(X, Y)

plot = plt.figure(figsize=(16, 8))
# выводим линии уровня функции
plot2d = plot.add_subplot(1, 2, 1)
plot2d.clabel(plot2d.contour(X, Y, Z), fontsize=9)
# выводим путь, по которому мы пришли в точку минимума
plot2d.plot(x1, y1, "o-", color="black", linewidth=1)
# название графика и подписи для осей
plot2d.set_title("Линии уровня и градиент")
plot2d.set_xlabel("x")
plot2d.set_ylabel("y")
# вывод сетки
plot2d.grid(True)

# выводим график функции в осях xyz
polt3d = plot.add_subplot(1, 2, 2, projection='3d')
polt3d.plot_surface(X, Y, Z, rstride=5, cstride=5, alpha=0.7)
# выводим путь в 3d
polt3d.plot(x1, y1, z1, marker='o', color='red')
# название графика и подписи для осей
polt3d.set_title("3D график и градиент")
polt3d.set_xlabel("x")
polt3d.set_ylabel("y")
polt3d.set_zlabel("z")
# вывод графиков
plt.show()
