# -*- coding: utf-8 -*-
"""Wrong solution."""
import math

def function():
    # input
    x, y = [float(coord) for coord in input().split()][:2]
    floats = [float(x) for x in input().split()]

    # coords
    room_coords = [
        (0, 0),
        (x, 0),
        (x, y),
        (0, y),
    ]
    corner_coords = [(floats[i], floats[i + 1]) for i in range(0, 8, 2)]

    # найти угол наклона плана относительно помещения
    # определяем координаты вектора и оси 0x
    # Ox = (corner_coords[1][0], corner_coords[0][1])
    # vector = corner_coords[1]
    Ox = room_coords[2]
    vector = (corner_coords[2][0] - corner_coords[0][0], corner_coords[2][1] - corner_coords[0][1])

    # ((ax * bx) + (ay * by)) / ((sqrt(ax^2 + ay^2)) * (sqrt(bx^2 + by^2)))
    cosinus = (
                  (Ox[0] * vector[0]) + (Ox[1] * vector[1])
              ) / (
            (
                math.sqrt(Ox[0] ** 2 + Ox[1] ** 2)
            ) * (
                math.sqrt(vector[0] ** 2 + vector[1] ** 2)
            )
    )
    cosinus = round(cosinus, 5)

    angle = math.degrees(math.acos(cosinus))
    angle = round(angle, 5)

    # найти коэффициент подобия прямоугольников
    A1B1 = x
    B1C1 = y
    A2B2 = abs(corner_coords[1][0] - corner_coords[0][0])
    B2C2 = abs(corner_coords[2][1] - corner_coords[1][1])

    k = A2B2 / A1B1

    # найти координаты точки
    # since here пошла пизда по кочкам
    # X = (x + k * Y * sin(angle)) / (1 - cos(angle))
    # Y = (y - k * X * cos(angle)) / (1 - k * sin(angle))
    return ("yes")


if __name__ == "__main__":
    print(function())
