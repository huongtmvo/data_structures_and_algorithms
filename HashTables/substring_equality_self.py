import sys

class Solver:
    _m1 = 10**9 + 7
    _m2 = 10**9 + 9
    _x = 263

    def __init__(self, s):
        self.s = s
        n = len(s)
        self.h1 = [0] * (n+1) 
        self.h2 = [0] * (n+1)
        for i in range(1, n+1):
            self.h1[i] = (self._x * self.h1[i-1] + ord(self.s[i-1])) % self._m1
            self.h2[i] = (self._x * self.h2[i-1] + ord(self.s[i-1])) % self._m2

    def pow(self, x, l, m):
        if l == 0: return 1
        h = self.pow(x, l//2, m)
        return (h * h) % m if l % 2 == 0 else (x * h * h) % m 

    def run(self, a, b, l):
        xl_m1 = self.pow(self._x, l, self._m1)
        xl_m2 = self.pow(self._x, l, self._m2)

        ha_m1 = (self.h1[a+l] - xl_m1 * self.h1[a]) % self._m1
        hb_m1 = (self.h1[b+l] - xl_m1 * self.h1[b]) % self._m1

        ha_m2 = (self.h2[a+l] - xl_m2 * self.h2[a]) % self._m2
        hb_m2 = (self.h2[b+l] - xl_m2 * self.h2[b]) % self._m2
        
        return True if ha_m1 == hb_m1 and ha_m2 == hb_m2 else False

s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.run(a, b, l) else "No")