from cone_area_lib import cone_area

radius = float(input("Radius: "))
height = float(input("Height: "))

area = cone_area(radius, height)

print("Mantelfläche: ", area)
