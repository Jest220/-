import timeit
import numpy as np
a = list()
print("Введите матрицу: ")
for i in range(3):
    a.append(list(map(int, input().split())))
a = np.array(a)

print(timeit.timeit('np.linalg.inv(a)', number=100000, globals=globals()))