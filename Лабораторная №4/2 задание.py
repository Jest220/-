from timeit import timeit
def bucketSort(a, l, r): #блочная сортировка
    if len(a) < 2 or l == r:
        return a

    mid = (l + r) / 2
    left = [i for i in a if i < mid]
    right = [i for i in a if i >= mid]
    return bucketSort(left, l, max(left)) + bucketSort(right, min(right), r)




def heapify(a, n, i): # построение двоичной кучи поддерева
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and a[l] > a[largest]:
        largest = l
    if r < n and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)
def heapSort(a, n): #пирамидальная сортировка
    for i in range(n // 2 - 1, -1, -1): #построение max-heap
        heapify(a, n, i)
    for i in range(n-1, -1, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)


a = list(map(int, input("Введите массив: ").split()))
heapSort(a, len(a))
print(a)

a = list(map(int, input("Введите массив: ").split()))
a = bucketSort(a, min(a), max(a))
print(a)