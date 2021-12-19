# Uses python3
import sys
import itertools

def partition3_1(A):
    # This has exponential running time
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)
        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1
    return 0

def partition3(A):
    n = len(A)
    W = sum(A)
    if W % 3 != 0:
        return 0
    lookup = {}
    def opt(a, b, c, i):
        if a == b == c == 0:
            return True
        if i < 0:
            return False
        if (a,b,c,i) in lookup:
            return lookup[(a,b,c,i)]
        ans = False
        if a >= A[i]:
            ans = opt(a - A[i], b, c, i-1)
        if b >= A[i]:
            ans = ans or opt(a, b - A[i], c, i-1)
        if c >= A[i]:
            ans = ans or opt(a, b, c - A[i], i-1)
        lookup[(a,b,c,i)] = ans
        return ans
    return 1 if opt(W//3, W//3, W//3, n-1) else 0
    # Or change all True to 1 and False to 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

