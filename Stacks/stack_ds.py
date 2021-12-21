# write stack data structure that support
# pop O(1)
# push O(1)
# top O(1)
# empty O(1)

class Stack:
    def __init__(self):
        self.stack = []
    
    def pop(self):
        if len(self.stack) == 0:
            raise Exception("Can't perform pop from empty stack")
        return self.stack.pop()

    def top(self):
        if len(self.stack) == 0:
            raise Exception("Can't perform top from empty stack")
        return self.stack[-1]

    def push(self, x):
        self.stack.append(x)

    def empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return f"Stack: {' '.join(map(str, self.stack))}"
        
