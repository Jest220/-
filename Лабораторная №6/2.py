#ПОИСК В ГЛУБИНУ

g = [[] for i in range(100000)]
used = [0 for i in range(100000)]

def dfs(x, color):
    used[x] = color
    for i in g[x]:
        if not used[i]:
            dfs(i, color)

n, m = list(map(int, input().split()))

for i in range(m):
    a, b = list(map(int, input().split()))
    g[a].append(b)
    g[b].append(a)

cnt = 0
for i in range(1, n + 1):
    if not used[i]:
        cnt += 1
        dfs(i, cnt)
print(cnt)

# 7 4
# 1 2
# 1 3
# 4 5
# 5 6