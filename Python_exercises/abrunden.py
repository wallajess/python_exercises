from math import floor, ceil

Kommazahl = input("Bitte geben Sie eine Fließkommazahl ein: ")

sqrd = (float(Kommazahl)) ** 2

method_1 = float(round(sqrd) // 1)
method_2 = float(floor(sqrd))
method_3 = float(int(sqrd))
method_4 = float(round(sqrd - 0.5))

print("Kommazahl: " + Kommazahl)
print("Quadriert: " + str(sqrd))
print("Methode 1: " + str(method_1))
print("Methode 2: " + str(method_2))
print("Methode 3: " + str(method_3))
print("Methode 4: " + str(method_4))