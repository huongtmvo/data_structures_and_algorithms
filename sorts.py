# Selection sort 
def selection_sort(A):
    n = len(A)
    for j in range(n):
        minIndex = j
        for i in range(j+1,n):
            if A[i] < A[minIndex]:
                minIndex = i 
        A[j],A[minIndex] = A[minIndex],A[j]
    return A 

# Merge sort:
def merge_sort(A):
    if len(A) <= 1:
        return A 
    mid = len(A)//2
    L = A[:mid]
    R = A[mid:]

    merge_sort(L)
    merge_sort(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    
    if len(L) > i :
        A[k] = L[i]
        i += 1
        k += 1
    while len(R) > j:
        A[k] = R[j]
        j += 1
        k += 1
    return A 


# Quick sort
# l: starting index, r: ending index
def partition(A,l,r):
    pivot = A[l]
    j = l
    for i in range(l+1,r+1):
        if A[i] <= pivot:
            j += 1
            A[i],A[j] = A[j],A[i]
    A[l], A[j] = A[j],A[l]
    return j

def quick_sort(A,l,r):
    if len(A) == 1:
        return A
    if l < r:  
        m = partition(A,l,r)
        quick_sort(A,l,m-1)
        quick_sort(A,m+1,r)

A = [-1,3,24,5,7]
r = len(A) - 1
quick_sort(A,0,r)
print('sorted array is:')
for i in range(len(A)):
    print(A[i], end =' ')



