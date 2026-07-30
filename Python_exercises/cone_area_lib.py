from math import pi, sqrt


def cone_area(radius, height):
    s = sqrt(radius ** 2 + height ** 2)
    m = round((pi * radius * s), 2)
    return m