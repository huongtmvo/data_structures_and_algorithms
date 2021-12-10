# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]

    j = l
    for i in range(l+1, r+1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    
    k = l 
    for i in range(l, j+1):
        if a[i] < a[j]:
            a[i], a[k] = a[k], a[i]
            k += 1
    return k, j

def randomized_quick_sort(a, l, r):
    if l >= r:
        return a
    m = random.randint(l, r)
    a[l], a[m] = a[m], a[l]
    
    k, j = partition3(a, l, r)
    randomized_quick_sort(a, l, k-1)
    randomized_quick_sort(a, j + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
