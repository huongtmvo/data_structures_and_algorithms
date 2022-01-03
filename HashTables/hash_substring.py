# python3

# def read_input():
#     return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

# def get_occurrences(pattern, text):
# This solution is very slow
#     return [
#         i 
#         for i in range(len(text) - len(pattern) + 1) 
#         if text[i:i + len(pattern)] == pattern
#     ]

def hash_func(s, multiplier, prime):
    ans = 0
    for c in s[::-1]:
        ans = (ans * multiplier + ord(c)) % prime
    return ans

def precomputed_hash(pattern, text, multiplier, prime):
    t = len(text)
    p = len(pattern)
    s = text[t-p:]
    H = [0] * (t-p+1)
    H[t-p] = hash_func(s, multiplier, prime)
    y = 1
    for i in range(1, p+1):
        y = (y * multiplier) % prime
    for i in range(t-p-1, -1, -1):
        H[i] = (H[i+1] * multiplier + ord(text[i]) - ord(text[i+p]) * y) % prime 
    return H
    
def get_occurrences(pattern, text):
    p = len(pattern)
    t = len(text)
    multiplier = 263
    prime = 1000000007
    res = []
    pattern_hash = hash_func(pattern, multiplier, prime)
    substrings_hash = precomputed_hash(pattern,text,multiplier,prime)

    for i in range(t-p+1):
        if substrings_hash[i] == pattern_hash:
            if text[i:i+p] == pattern:
                res.append(i)
    return res
    
if __name__ == '__main__':
    pattern = input()
    text = input()
    print_occurrences(get_occurrences(pattern, text))

