# python3

import sys
import threading


def compute_height(n, parents):
    # build tree with array (can be done using LinkedList as well)
    children = [[] for _ in range(n)]
    root = None
    for i in range(n):
        p = parents[i]
        if p == -1:
            root = i
        else:
            children[p].append(i)
    
    def height(i):
        h = 0
        for c in children[i]:
            h = max(h, height(c))
        return h+1
    
    return height(root)

# children = [[], [3, 4], [], [], [0, 2]]
# children[1] = [3,4]


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
