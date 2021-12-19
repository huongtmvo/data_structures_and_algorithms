# Uses python3
def get_maximum_value(dataset):
    n = (len(dataset) - 1) // 2
    lookup_min = {}
    def opt_min(i, j):
        if i == j:
            return int(dataset[2*i])
        if (i, j) in lookup_min:
            return lookup_min[(i,j)]
        ans = float('inf')
        for k in range(i, j):
            op = dataset[2*k+1]
            if op == '+':
                ans = min(ans, opt_min(i,k) + opt_min(k+1,j))
            elif op == '-':
                ans = min(ans, opt_min(i,k) - opt_max(k+1,j))
            else:
                ans = min(ans, opt_min(i,k) * opt_min(k+1,j), \
                                opt_min(i,k) * opt_max(k+1,j), \
                                opt_max(i,k) * opt_min(k+1,j), \
                                opt_max(i,k) * opt_max(k+1,j) )
        lookup_min[(i,j)] = ans
        return ans

    lookup_max = {}
    def opt_max(i, j):
        if i == j:
            return int(dataset[2*i])
        if (i,j) in lookup_max:
            return lookup_max[(i,j)]
        ans = float('-inf')
        for k in range(i, j):
            op = dataset[2*k+1]
            if op == '+':
                ans = max(ans, opt_max(i,k) + opt_max(k+1,j))
            elif op == '-':
                ans = max(ans, opt_max(i,k) - opt_min(k+1,j))
            else:
                ans = max(ans, opt_max(i,k) * opt_max(k+1,j), \
                                opt_min(i,k) * opt_min(k+1,j))
        lookup_max[(i,j)] = ans
        return ans

    return opt_max(0, n)

if __name__ == "__main__":
    print(get_maximum_value(input()))
