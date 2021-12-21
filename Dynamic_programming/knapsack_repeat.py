def topdown(W, V, C, d = {}):
    if W == 0:
        return 0
    if W in d:
        return d[W]
    ans = 0
    for i in range(len(C)):
        if W >= C[i]:
            ans = max(ans,topdown(W - C[i], V, C, d) + V[i])
    d[W] = ans
    return d[W]

W = 10
V = [30, 14, 16, 9]
C = [6, 3, 4, 2]
print(topdown(W,V,C))

def bottom_up(W, V, C):
    opt = [0] * (W + 1)
    for w in range(1, W + 1):
        for i in range(len(V)):
            if w >= C[i]:
                opt[w] = max(opt[w], opt[w - C[i]] + V[i])
    return opt[W]

W = 10
V = [30, 14, 16, 9]
C = [6, 3, 4, 2]
print(bottom_up(W, V, C))


