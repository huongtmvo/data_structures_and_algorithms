#Uses python3

# Strongly connected components: the portion of a directed graph 
# in which there is a path from each vertex to another vertex
import sys

sys.setrecursionlimit(200000)

def reverse_graph(adj):
    n = len(adj)
    adjr = [[] for _ in range(n)]
    for v in range(n):
        for w in adj[v]:
            adjr[w].append(v)
    return adjr 

def dfs(adj, visited, order, x): # to get the post order
    visited[x] = True
    for u in adj[x]:
        if not visited[u]:
            dfs(adj, visited, order, u)
    order.insert(0,x)

def toposort(adj):
    visited = [False] * len(adj)
    order = []
    for v in range(len(adj)):
        if not visited[v]:
            dfs(adj,visited,order,v)
    return order    

def explore(adj, visited, x):
    visited[x] = True
    for u in adj[x]:
        if not visited[u]:
            explore(adj, visited, u) 

def number_of_strongly_connected_components(adj):
    result = 0 
   # reverse the graph
    adjr = reverse_graph(adj)
    # find the largest post order umber in reverse of G.
    order = toposort(adjr)

    visited = [False] * n
    for v in order:
        if not visited[v]:
            explore(adj, visited, v)
            result += 1
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
