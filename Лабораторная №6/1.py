a = input("Введите скобочную последовательность:\n>>>")
b = []
c = []
isexit = False
for i in range(len(a)):
    if a[i] == '(':
        b.append('(')
        c.append(i)
    else:
        if len(b) == 0:
            print(i, a[i])
            isexit = True
            break
        else:
            b.pop()
            c.pop()
if len(b) != 0 and not isexit:
    print(c[0], b[0])
