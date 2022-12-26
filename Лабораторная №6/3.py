g = list()
moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
used = [[0 for i in range(m)] for j in range(n)]

#основное решение лабиринта
def dfs(x, y):
    if (x == n - 1 or y == m - 1) and g[x][y] == 0:
        used[x][y] = 1
        g[x][y] = 'A'
        return
    used[x][y] = 1
    for i, j in moves:
        x1 = x + i
        y1 = y + j
        if x1 < n and y1 < m and not used[x1][y1] and g[x1][y1] == 0:
            dfs(x + i, y + j)
            if g[x + i][y + j] == 'A':
                g[x][y] = 'A'

def output():
    print()
    for i in range(n):
        for j in range(m):
            print(g[i][j], end = ' ')
        print()

#Ввод лабиринта
print("Введите лабиринт:")
for i in range(n):
    cur = list(map(int, input().split()))
    g.append(cur)

#ищем вход и запускаемся
isprinted = False
for i in range(n):
    if g[i][0] == 0:
        dfs(i, 0)
        if g[i][0] == 'A':
            output()
            isprinted = True

for j in range(m):
    if g[0][j] == 0:
        dfs(0, j)
        if g[0][j] == 'A':
            output()
            isprinted = True

#14
#15
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 0 0 0 0 1 0 1 0 0 0 0 1 1 1
# 1 0 1 1 1 1 0 1 0 1 1 0 1 0 1
# 1 0 1 0 0 0 0 1 0 1 1 0 1 0 1
# 1 0 1 1 1 1 0 1 0 0 1 0 1 0 1
# 1 0 0 0 0 1 0 1 0 1 1 0 1 0 1
# 1 0 1 1 1 1 0 1 0 1 1 0 1 0 1
# 0 0 1 1 0 1 0 1 0 1 0 0 1 0 0
# 1 0 1 0 0 0 0 0 0 1 1 0 1 0 1
# 1 0 1 1 1 0 1 1 0 0 1 0 1 0 1
# 1 0 0 1 1 0 1 1 1 1 1 0 1 0 1
# 1 1 0 0 0 0 1 0 0 0 0 0 1 0 1
# 1 1 1 1 0 0 0 0 0 0 0 0 0 0 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1