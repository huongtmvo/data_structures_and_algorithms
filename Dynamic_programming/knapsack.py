# Uses python3
import sys

def topdown(W, w, n, d = {}):
    if W == 0 or n == 0 :
        return 0
    if (W,n) in d:
        return d[(W,n)]
    opt = topdown(W, w, n-1, d)
    if W >= w[n-1]:
        opt = max(opt, topdown(W - w[n-1], w, n-1, d) + w[n-1])
    d[(W, n)] = opt
    return d[(W, n)]


def optimal_weight(W, w, n):
    opt = [[0] * (n+1) for _ in range(W + 1)]
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            opt[j][i] = opt[j][i-1]
            if j >= w[i-1]:
                opt[j][i] = max(opt[j][i], opt[j - w[i-1]][i-1] + w[i-1])
    return opt[W][n]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w, n))



