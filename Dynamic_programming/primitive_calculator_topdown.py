def topdown(n, d = {}):
    if n == 1:
        return 0
    if n in d: 
        return d[n]
    ans = float('inf')
    if n % 2 == 0:
        ans = min(ans,topdown(n//2, d)+ 1)
    elif n % 3 == 0:
        ans = min(ans,topdown(n//3, d) + 1)
    else:
        ans = min(ans,topdown(n-1, d) + 1)
    d[n] = ans
    return d[n]

n = int(input())
d = {}
ans = topdown(n,d)
print(ans)



        
