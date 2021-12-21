# Uses python3
import numpy
def edit_distance(s, t):
    n1,n2 = len(s),len(t)

    matrix = numpy.zeros((n1+1, n2+1))
    for i in range(n1+1):
        matrix[i][0] = i
    for j in range(n2+1):
        matrix[0][j] = j
    for j in range(1,n2+1):
        for i in range(1,n1+1):
            insertion = matrix[i][j-1] + 1
            deletion = matrix[i-1][j] + 1
            match = matrix[i-1][j-1] 
            mismatch = matrix[i-1][j-1] + 1
            if s[i-1] == t[j-1]:
                matrix[i][j] = min(insertion,deletion,match)
            else:
                matrix[i][j] = min(insertion,deletion,mismatch)
    return int(matrix[n1][n2])

if __name__ == "__main__":
    print(edit_distance(input(), input()))
