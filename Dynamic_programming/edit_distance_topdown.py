def edit_distance(s,t):
    d = {}
    n, m = len(s),len(t)
    def opt(i,j):
        if i == 0 or j == 0:
            return i + j
        if (i,j) in d:
            return d[(i,j)]
        d[(i,j)] = min(opt(i-1,j-1) + (s[i-1] != t[j-1]),opt(i-1,j)+1,opt(i,j-1)+1)
        return d[(i,j)]
    return opt(n,m)

s = input()
t = input()
print(edit_distance(s,t))
