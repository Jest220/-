n = int(input())
a = list(map(int, input().split()))

for i in range(n - 1):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)
print('O(n^2)')