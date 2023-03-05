def lagrange_function(points, x):
    result = 0
    n = len(points)
    for i in range(n):
        x_i, y_i = points[i]
        base = 1
        for j in range(n):
            if i != j:
                x_j = points[j][0]
                base *= (x - x_j) / (x_i - x_j)
        result += y_i * base
    return result


def lagrange_interpolation(points, points_no):
    step = round(len(points) / points_no)
    points_for_interpolation = points[::step]
    interpolated_y = []
    for point in points:
        result = lagrange_function(points_for_interpolation, point[0])
        interpolated_y.append(result)

    return points_for_interpolation, interpolated_y
