def bottomup(n):
    ans = [0,0] + [float('inf')]* (n-1) 
    if n == 1:
        return ans[n]
    for n in range(2,n+1):
        if n % 2 == 0:
            ans[n] = min(ans[n],ans[n//2]+ 1)
        elif n % 3 == 0:
            ans[n] = min(ans[n],ans[n//3]+1)
        ans[n] = min(ans[n],ans[n-1] + 1)
    
    path = [n]
    while path[-1] != 1:
        x = path[-1]
        if ans[x] == ans[x-1] + 1:
            path.append(x-1)
        elif x%2==0 and ans[x] == ans[x//2] + 1:
            path.append(x//2)
        else:
            path.append(x//3)
    return path[::-1]

n = int(input())
path = bottomup(n)
print(len(path) -1)
for p in path:
    print(p,end = ' ')
print()
    

