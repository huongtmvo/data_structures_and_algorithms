#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTreeRecursive(tree):
  # Implement correct algorithm here
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
    if not lower < key[i] <= upper:
      return False
    return isValid(left[i], lower, key[i]) and isValid(right[i], key[i], upper)
  
  return isValid(0)

class Node:
  def __init__(self, a, b, c):
    self.key = a
    self.left = b
    self.right = c

def IsBinarySearchTree(tree):
  stack = [(float('-inf'), tree[0], float('inf'))]
  while stack:
    min, root, max = stack.pop()
    if root.key < min or root.key >= max:
      return False
    if root.left != -1:
      stack.append((min, tree[root.left], root.key))
    if root.right != -1:
      stack.append((root.key, tree[root.right], max))
  return True

def main():
  n_nodes = int(input())
  nodes = [0 for _ in range(n_nodes)]
  for i in range(n_nodes):
    a, b, c = map(int, input().split())
    node = Node(a, b, c)
    nodes[i] = node
  if n_nodes == 0 or IsBinarySearchTree(nodes):
    print('CORRECT')
  else:
    print('INCORRECT')

threading.Thread(target=main).start()
