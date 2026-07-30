from dataclasses import dataclass, field
from geo import GuiWrapper, Vector2D, Object2D
from math import pi
import abc
import tkinter as tk

# 9(a)


@dataclass
class Circle(Object2D):
    """Represents a 2D-circle.

    Properties:
        radius: indicates the circle's radius
        top_left:  top left corner of the smallest square that can encompass the circle
        bottom_right: bottom right corner of the smallest square that can encompass the circle

    Invariants:
        radius > 0
    """

    __radius: float
    __top_left: Vector2D = field(repr=False, init=False)
    __bottom_right: Vector2D = field(repr=False, init=False)

    def __post_init__(self):
        assert self.radius > 0, "Radius must be greater than 0."
        self.top_left = Vector2D((self.pos.x - self.radius // 2), (self.pos.y + self.radius // 2))
        self.bottom_right = Vector2D((self.pos.x + self.radius // 2), (self.pos.y - self.radius // 2))

    @property
    def radius(self) -> float:
        return self.__radius

    @property
    def top_left(self) -> Vector2D:
        return self.__top_left

    @top_left.setter
    def top_left(self, top_left: Vector2D):
        self.__top_left = top_left

    @property
    def bottom_right(self) -> Vector2D:
        return self.__bottom_right

    @bottom_right.setter
    def bottom_right(self, bottom_right: Vector2D):
        self.__bottom_right = bottom_right

    def draw(self, gui: GuiWrapper, fillcolor: str, outlinecolor: str):
        return gui.canvas.create_oval(
            self.bottom_right.x,
            self.top_left.y,
            self.top_left.x,
            self.bottom_right.y,
            fill=fillcolor,
            outline=outlinecolor)


# 9(b)

# @dataclass
# class RotableEllipse(Object2D):
    """A rotatable ellipse with the following properties:
        size(type: Vector2D):
            - defines the horizontal and vertical raidus of the ellipse (half the width and height)
            - both coordiantes must be greater than 0
        angle(float):
            - the angle of the ellipse in the radian
            - the ellipse is rotated counterclockwise around its centrepoint
            - must be greater or equal to 0 but < 2π """

#    __size: Vector2D
#    __angle: float

#    def __post_init__(self):
#        assert self.size.x > 0 and self.size.y  > 0
#        assert 0 <= self.angle < 2 * pi

#    @property
#    def size(self) -> Vector2D:
#        return self.__size

#    @property
#    def angle(self) -> float:
#        return self.__angle

#    def draw(self, gui: GuiWrapper, fillcolor: str = "black",
#        outlinecolor: str = "black"):
#        return gui.canvas.create_polygon(())

# Implementieren Sie die Methode draw, verwenden Sie hierfür gui.canvas.create_polygon.
# Erstellen Sie eine Liste mit 360 Punkten [x1, y1, ..., x360, y360], um die Ellipse zu beschreiben.
# Verwenden Sie den star-operator *liste um die Koordinaten der Punkte der Funk-tion zu übergeben.
# Dieser Operator wandelt die Liste in einzelne Argu-mente um.
# Beispiel: funktion(*[1, 2, 3]) entspricht funktion(1, 2, 3).
# Übergeben Sie die Farbwerte mit den keywords fill und outline

# 9(c)


@dataclass
class Triangle(Object2D):
    """A triangle with the following properties:
    edge1
    edge 2
    """

    __edge1: Vector2D
    __edge2: Vector2D

    @property
    def edge1(self):
        return self.__edge1

    @edge1.setter
    def edge1(self, edge1: Vector2D):
        self.__edge1 = edge1

    @property
    def edge2(self):
        return self.__edge2

    @edge2.setter
    def edge2(self, edge2: Vector2D):
        self.__edge2 = edge2

    def draw(self, gui: GuiWrapper, fillcolor: str = "black", outlinecolor: str = "black"):
        return gui.canvas.create_polygon(
            self.pos.x,
            self.pos.y,
            self.edge1.x,
            self.edge1.y,
            self.edge2.x,
            self.edge2.y,
            fill=fillcolor,
            outline=outlinecolor)


if __name__ == "__main__":
    gui = GuiWrapper(width=800, height=600)
    circle = Circle(Vector2D(100, 200), 75)
    circle.draw(gui, fillcolor="lightblue", outlinecolor="black")
    gui.start()
    # ellipse = RotatableEllipse(Vector2D(300, 250), Vector2D(200, 50), 7 * pi / 5)
    # ellipse.draw(gui, fillcolor="pink")
    triangle = Triangle(Vector2D(450, 150), Vector2D(200, 150), Vector2D(100, 350))
    triangle.draw(gui, fillcolor="green", outlinecolor="black")