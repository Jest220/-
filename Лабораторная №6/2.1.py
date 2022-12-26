#ПОИСК В ШИРИНУ
from queue import Queue
q = Queue()
g = [[] for i in range(100000)]
d = [0 for i in range(100000)]

n, m = list(map(int, input().split()))

for i in range(m):
    a, b = list(map(int, input().split()))
    g[a].append(b)
    g[b].append(a)

d[1] = 1
q.put(1)
while not q.empty():
    x = q.get()
    for i in g[x]:
        if d[i] == 0:
            d[i] = d[x] + 1
            q.put(i)
print(d[n] - 1)