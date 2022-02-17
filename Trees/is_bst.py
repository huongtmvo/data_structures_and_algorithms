#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTreeRecursive(tree):
  # # Implement correct algorithm here
  if len(tree) == 0:
    return True
  
  key, left, right = [], [], []
  for a, b, c in tree:
    key.append(a)
    left.append(b)
    right.append(c)
  
  def isValid(i, lower=float('-inf'), upper=float('inf')):
    if i == -1:
      return True
    if not lower < key[i] < upper:
      return False
    return isValid(left[i], lower, key[i]) and isValid(right[i], key[i], upper)
  
  return isValid(0)


class Node:
    def __init__(self, a, b, c):
        self.key = a
        self.left = b
        self.right = c

def inOrder(tree):
    stack = []
    result = []
    curr = 0
    while stack or curr != -1:
        if curr != -1:
            root = tree[curr]
            stack.append(root)
            curr = root.left
        else:
            root = stack.pop()
            result.append(root.key)
            curr = root.right
    return result

def IsBinarySearchTree(tree, n):
    nodes = inOrder(tree)
    for i in range(1, n):
        if nodes[i] <= nodes[i - 1]:
            return False
    return True


def main():
  n_nodes = int(input())
  nodes = [0 for _ in range(n_nodes)]
  for i in range(n_nodes):
    a, b, c = map(int, input().split())
    node = Node(a, b, c)
    nodes[i] = node
  if n_nodes == 0 or IsBinarySearchTree(nodes, n_nodes):
    print('CORRECT')
  else:
    print('INCORRECT')

threading.Thread(target=main).start()
