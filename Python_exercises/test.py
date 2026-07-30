from math import log2
res = int(log2(64)) + 2 ** abs(1+1j)
print(res)
print(type(res))

from math import sqrt, floor, ceil
res = floor(2.3 * 7) * ceil(2 ** 3 + 7.1)
print(res)
print(type(res))

from math import pi, sin, cos, radians
res = cos(pi/4)**2 + sin(radians(45))**2j
print(res)
print(type(res))

res = 6 * round(2.1, 1) // 1
print(res)
print(type(res))

print(2.12//1)
print(type(2.12//1))

print(abs(1+1j))