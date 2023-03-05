from matrix import *


def lu_factorization(A, b):
    N = len(A)
    x = [1 for _ in range(N)]
    y = [0 for _ in range(N)]
    U = copy_matrix(A)
    L = create_diagonal_matrix(x)

    # tworzenie macierzy L i U; A = L * U
    for i in range(N):
        for j in range(i+1, N):
            L[j][i] = U[j][i] / U[i][i]
            for k in range(i, N):
                U[j][k] = U[j][k] - L[j][i]*U[i][k]

    # L * y = b
    for i in range(N):
        result = b[i]
        for j in range(i):
            result -= L[i][j] * y[j]
        y[i] = result / L[i][i]

    # U * x = y
    for i in range(N-1, -1, -1):
        result = y[i]
        for j in range(i+1, N):
            result -= U[i][j] * x[j]
        x[i] = result / U[i][i]

    return x
