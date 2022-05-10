#Uses python3

# Find if there is any cycles in the graph
import sys

'''
For directed graphs, 

WHITE: never visited, 
GREY: visiting,
BLACK: done visited
'''

WHITE, GREY, BLACK = 0, 1, 2
def explore(adj, v):
    visited[v] = GREY
    for u in adj[v]:
        if visited[u] == GREY: 
            return True
        if visited[u] == WHITE:
            if explore(adj, u):
                return True   
    visited[v] = BLACK  
    return False        
        
def acyclic(adj):
    for v in range(len(adj)):
        if visited[v] == WHITE:
            if explore(adj, v): 
                return 1
    return 0 

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    
    visited = [WHITE] * n
    print(acyclic(adj))

