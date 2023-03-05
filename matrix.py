def copy_matrix(matrix):
    copy = []
    for row in matrix:
        copied_row = []
        for value in row:
            copied_row.append(value)
        copy.append(copied_row)
    return copy


def create_diagonal_matrix(vector):
    n = len(vector)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[i][i] = vector[i]
    return matrix


def create_zero_matrix(size):
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    return matrix


def create_zero_vector(size):
    vector = [0 for _ in range(size)]
    return vector
