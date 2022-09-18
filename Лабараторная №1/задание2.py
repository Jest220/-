from math import log, modf, ceil, floor
print('Введите цифру необходимой функции:\n'
          '1.Сложение\n'
          '2.Вычитание\n'
          '3.Умножение\n'
          '4.Деление\n'
          '5.Возведение в степень\n'
          '6.Логарифм\n'
          '7.Округление в большую сторону до N знака после запятой\n'
          '8.Округление в меньшую сторонудо N знака после запятой')
isTrue = False

f = input('---->')
if f in '1234567890' and 1 <= int(f)<= 8:
    f = int(f)
    isTrue = True
while not isTrue:
    f = input('Пожалуйста, попройте еще раз: ')
    if f in '1234567890' and 1 <= int(f)<= 8:
        f = int(f)
        isTrue = True
        f = int(f)
        
a = input("Введите первое число: ")
while any('z' >= i >= 'a' or 'Z' >= i >= 'A' for i in a):
    a = input("Попробуйте еще раз: ")
a = float(a)

b = input("Введите второе число: ")
while any('z' >= i >= 'a' or 'Z' >= i >= 'A' for i in b):
    b = input("Попробуйте еще раз: ")
b = float(b)

if f == 1:
    print('Результат:', (a + b))
elif f == 2:
    print('Результат:', (a - b))
elif f == 3:
    print('Результат:', (a * b))
elif f == 4:
    print('Результат:', (a / b))
elif f == 5:
    print('Результат:', (a ** b))
elif f == 6:
    print('Результат:', log(a, b))
elif f == 7:
    ans = modf(a)
    print('Результат:', ans[1] + ceil(ans[0] * 10**b) / (10**b))
elif f == 8:
    ans = modf(a)
    print('Результат:', ans[1] + floor(ans[0] * 10**b) / (10**b))
