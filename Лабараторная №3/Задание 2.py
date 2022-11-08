# O(3n)

def n3(n):
    for i in range(3):
        for j in range(n):
            print(1)


# O(nlogn)

def nlogn(n):
    for i in range(n):
        l = 0
        r = n + 1
        while r - l != 1:
            mid = (l + r) // 2
            if mid <= i:
                l = mid
            else:
                r = mid
        print(l)

# O(n!)
def facn(n):
    if n == 1:
        return 1
    return facn(n - 1) * n
# O(n^3)

def nstep3(n):
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ans += 1
    return ans
# O(3log(n))

def logn3(n):
    for i in range(3):
        l = 0
        r = n + 1
        while r - l != 1:
            mid = (l + r) // 2
            if mid <= i:
                l = mid
            else:
                r = mid
        print(l)