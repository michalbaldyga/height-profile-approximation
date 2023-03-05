from solving_methods import *


def create_system_of_equations(points):
    # Ax = b
    n = len(points)
    A = create_zero_matrix(4 * (n - 1))
    b = create_zero_vector(4 * (n - 1))

    # S_j(x_j) = f(x_j)
    for i in range(n - 1):
        x, y = points[i]
        A[4 * i + 3][4 * i + 3] = 1
        b[4 * i + 3] = float(y)

    # S_j(x_j+1) = f(x_j+1)
    for i in range(n - 1):
        x_1, y_1 = points[i + 1]
        x_0, y_0 = points[i]
        h = float(x_1) - float(x_0)
        A[4 * i + 2][4 * i] = h ** 3
        A[4 * i + 2][4 * i + 1] = h ** 2
        A[4 * i + 2][4 * i + 2] = h ** 1
        A[4 * i + 2][4 * i + 3] = 1
        b[4 * i + 2] = float(y_1)

    # Dla węzłów wewnętrznych x_j: S'_j-1(x_j) = S'_j(x_j)
    for i in range(n - 2):
        x_1, y_1 = points[i + 1]
        x_0, y_0 = points[i]
        h = float(x_1) - float(x_0)
        A[4 * i][4 * i] = 3 * (h ** 2)
        A[4 * i][4 * i + 1] = 2 * h
        A[4 * i][4 * i + 2] = 1
        A[4 * i][4 * (i + 1) + 2] = -1
        b[4 * i] = 0.0

    # Dla węzłów wewnętrznych x_j: S''_j-1(x_j) = S''_j(x_j)
    for i in range(n - 2):
        x_1, y_1 = points[i + 1]
        x_0, y_0 = points[i]
        h = float(x_1) - float(x_0)
        A[4 * (i + 1) + 1][4 * i] = 6 * h
        A[4 * (i + 1) + 1][4 * i + 1] = 2
        A[4 * (i + 1) + 1][4 * (i + 1) + 1] = -2
        b[4 * (i + 1) + 1] = 0.0

    # Na krawędziach: S''_0(x_0) = 0
    A[1][1] = 2
    b[1] = 0.0

    # Na krawędziach: S''_n-1(x_n) = 0
    x_1, y_1 = points[-1]
    x_0, y_0 = points[-2]
    h = float(x_1) - float(x_0)
    A[-4][1] = 2
    A[-4][-4] = 6 * h
    b[-4] = 0.0

    return A, b


def compute_polynomial(solution_vectors, points, x):
    for i in range(1, len(points)):
        x_i = points[i-1][0]
        x_j = points[i][0]
        if float(x_i) <= x <= float(x_j):
            a, b, c, d = solution_vectors[i-1]
            elem = x - float(x_i)
            return a*(elem**3) + b*(elem**2) + c*elem + d


def split_solution_vector(solution_vector):
    solution_vectors = []
    vec = []
    counter = 1
    for coefficient in solution_vector:
        vec.append(coefficient)
        if counter == 4:
            solution_vectors.append(vec.copy())
            vec.clear()
            counter = 1
        else:
            counter += 1
    return solution_vectors


def interpolate_with_spline(points, points_no):
    step = round(len(points) / points_no)
    points_for_interpolation = points[::step]

    A, b = create_system_of_equations(points_for_interpolation)
    solution_vector = lu_factorization(A, b)
    solution_vectors = split_solution_vector(solution_vector)

    interpolated_y = []
    for point in points:
        x = point[0]
        interpolated_y.append(compute_polynomial(solution_vectors, points_for_interpolation, float(x)))

    return points_for_interpolation, interpolated_y
