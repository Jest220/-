from random import randint

n = int(input("Количество элементов в массиве: "))
x = [randint(0, 1) for i in range(n)]

for i in range(1, n + 1):
    k0 = 0
    for j in range(0, n - i + 1):
        if sum(x[j:j+i]) == 0:
            k0 += 1
    k0 = k0 / (n - i + 1)

    k1 = 0
    for j in range(0, n - i + 1):
        if sum(x[j:j+i]) == i:
            k1 += 1
    k1 = k1 / (n - i + 1)
    if k1 == k0 == 0:
        break
    
    print('0'*i + ':', k0 * 100)
    print('1'*i + ':', k1 * 100)
