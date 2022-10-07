import random
import numpy as np

def print_matrix(M, matr_name):
    print("матрица " + matr_name)
    for i in M:  # делаем перебор всех строк матрицы
        for j in i:  # перебираем все элементы в строке
            print("%5d" % j, end=' ')
        print()

na = random.randint(1, 10)
x = np.zeros((na, na), int)
a = np.zeros((na, na), dtype=float)
ssum = 0
for i in range(na):                             # заполняем матрицу
    for j in range(na):
        x[i][j] = np.random.randint(1, 10)
print_matrix(x, "x")                            # выводим матрицу

t = int(input("Введите количество знаков после запятой при вычислении неточности : "))
t1 = 0.1 ** t

n = 1
ssum = 0
modl = 1
fact = 1
det = 0
diff = 1
nowssum = 0
while abs(diff) > t1:
    nowssum += ssum
    n += 1
    prom = (3 * n) - 1                          # промежуточные вычисления
    fact = np.math.factorial(prom)
    modl = - np.linalg.matrix_power(x, prom)
    det = np.linalg.det(modl)
    ssum = ssum + (det/fact)
    diff = abs(nowssum - ssum)                  # считаем разницу
    nowssum = 0
    print(n - 1, ':', ssum, ' ', diff)
print('Сумма знакопеременного ряда:', ssum)
