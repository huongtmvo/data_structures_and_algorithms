#Uses python3

import sys

def reach(adj, x, y):
    visited[x] = True
    for v in adj[x]:
        if not visited[v]: 
            reach(adj, v, y)
    if visited[y]:
        return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)] # adj is the adj list
    x, y = x - 1, y - 1 # index of the vertices
    for (a, b) in edges:
        adj[a - 1].append(b - 1) # idex of vertices
        adj[b - 1].append(a - 1)
    visited = [False] * n 
    print(reach(adj, x, y))


