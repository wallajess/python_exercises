from math import pi
from math import sqrt

height = input("Bitte geben Sie die Höhe des Kegels ein: ")
radius = input("Bitten geben Sie den Radius des Kegels ein: ")

height_float = float(height)
radius_float = float(radius)
s = sqrt(radius_float ** 2 + height_float ** 2)

surface = round((pi * radius_float * s), 2)
print("Radius: " + radius)
print("Höhe: " + height)
print("Mantelfläche: " + str(surface))