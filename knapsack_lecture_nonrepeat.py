# Notes: there is only 2 scenarios, either we use Vn and Cn or not. 
def topdown(W, n, V, C, opt = {}):
    if W == 0 or n == 0:
        return 0
    if (W, n) in opt:
        return opt[(W, n)]
    for i in range(n):
        ans = topdown(W, n-1, V, C, opt)
        if W >= C[i]:
            ans = max(ans, topdown(W - C[i], n -  1, V, C, opt ) + V [i])
    opt[(W, n)] = ans
    return opt[(W, n)]

W = 10
V = [30, 14, 16, 9]
C = [6, 3, 4, 2]
n = len(V)
print(topdown(W, n, V, C))

def bottom_up(W, n, V, C):
    opt = [[0] * (n + 1) for _ in range(W +1)]
    for i in range(1, n+1):
        for w in range(1, W +1):
            opt[w][i] = opt[w][i-1]
            if w >= C[i-1]:
                opt[w][i] = max(opt[w][i], opt[w - C[i-1]][i - 1] + V[i-1])
    return opt[W][n]

W = 10
V = [30, 14, 16, 9]
C = [6, 3, 4, 2]
n = len(V)
print(bottom_up(W, n, V, C))