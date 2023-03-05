from lagrange import *
from spline import *
from utils import *

if __name__ == '__main__':
    paths = ['data/MountEverest.csv', 'data/Obiadek.csv', 'data/WielkiKanionKolorado.csv']

    for path in paths:
        distance, height, points = read_data(path)
        points_for_interpolation, interpolated_y = lagrange_interpolation(points, 7)
        draw_plot(distance, height, interpolated_y, points_for_interpolation, "Lagrange'a")
        points_for_interpolation, interpolated_y = interpolate_with_spline(points, 7)
        draw_plot(distance, height, interpolated_y, points_for_interpolation, "funkcjami sklejanymi")
