
def print_matrix(m):
    for i in m:
        print(i)
    print()
    
def scalar_product(A, b, n):
    d = len(vect)
    s = 0
    for i in range(n+1,d):
        s = s + A[n][i]*b[i]
    return s

def gauss_solve(matrix, vect):
    d = len(vect)
    for m in range(0, d-1):
        for j in range(m+1,d):
            k = matrix[j][m] / matrix[m][m]
            for i in range(m,d):
                matrix[j][i] = matrix[j][i] - k*matrix[m][i]
            vect[j] = vect[j] - k*vect[m]

    for i in range(d-1, -1, -1):
        vect[i] = (vect[i] - scalar_product(matrix, vect, i)) / matrix[i][i]

if __name__ == "__main__":
    matrix = [[25,-18,-19,22,16],
            [-6, 21, 19,-3,8],
            [-19,22,-17,-4,18],
            [12,-2,22,-10,8],
            [-10,1,19,4,-8]]
    vect = [14,6,13,19,16]
    
    gauss_solve(matrix, vect)
    print_matrix(matrix)
    print(f"Вектор розв'язку:{vect}\n")