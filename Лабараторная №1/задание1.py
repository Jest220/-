#число
from math import modf
a = float(input("Введите число: "))
print("Целая часть:", modf(a)[1], "дробная часть: ", modf(a)[0])
#слово
a = input("Введите слово: ")
print("Это слово, но перевернутое:", a[::-1])
#строка
a = input("Введите строку: ")
print("Количество слов в строке: ", len(a.split(' ')))
#список
def isprime(a):
    if a == 1:
        return False
    prime = True
    i = 2
    while i * i <= a:
        if a % i == 0:
            prime = False
            break
        i += 1
    return prime
    
a = [1, 2, 3, 4, 5]
print("Простые числа из списка: ", end = '')
for i in range(len(a)):
    if isprime(a[i]):
        print(a[i], end = ' ')
print()
#кортеж
a = tuple("aboba")
print(a)
