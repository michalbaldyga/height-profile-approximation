import pandas as pd
from matplotlib import pyplot


def read_data(path):
    df = pd.read_csv(path)
    points = []
    distance = list(df["Distance"])
    height = list(df["Height"])
    for i in range(len(distance)):
        point = [distance[i], height[i]]
        points.append(point)
    return distance, height, points


def draw_plot(distance, height, interpolated_y, points_for_interpolation, name):
    x = []
    y = []
    for point in points_for_interpolation:
        x.append(point[0])
        y.append(point[1])

    pyplot.semilogy(distance, height, '.b', label='dane wejściowe')
    pyplot.semilogy(distance, interpolated_y, color='green', label='funkcja interpolująca')
    pyplot.semilogy(x, y, '.r', label='dane do interpolacji')
    pyplot.legend()
    pyplot.ylabel('Wysokość')
    pyplot.xlabel('Dystans')
    pyplot.title('Interpolacja ' + name)
    pyplot.grid()
    pyplot.show()
