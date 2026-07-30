import pillow


def mandelbrot(c = complex, m = int) -> int:
    """This function takes a complex number, c, and a whole number, m, as arguments
    and returns the smallest 0 =< n < m where |z_n| ≥ 2. If such an n does not exist,
    it returns m."""
    z = 0
    for n in range(m):
        z = z**2 + c
        if abs(z >= 2):
            return n + 1
    return m


def color(i: int, max_i: int) -> tuple[int, int, int]:
    # Farbton in Abhängigkeit der benötigten Schleifendurchläufe.
    hue = int(255 * (i / max_i))
    # Volle Helligkeit 255, außer wenn c Teil der Mandelbrotmenge ist.
    # Dadurch wird das innere schwarz.
    value = 255 if i < max_i else 0
    # Volle Sättigung
    saturation = 255
    return (hue, saturation, value)

# def render_mandelbrot(c1: complex, c2: complex, x: int, y: int, n: int, pic: str):
    """Generates a picture of the Mandelbrot set."""
    # Erstelle ein Bild mit Auflösung 800x600 wobei die einzelnen 
    # Pixel das HSV-Farbformat verwenden (Hue-Saturation-Value).
    size = (800, 600)
    img = Image.new("HSV", size)
    #Call the sample function to determine the complex numbers for each
    #pixel coordinate.
    for x in range(size[0]): 
        c = sample(-2 - i, 1 + i, x, y, 800, 600, )
    for y in range(size[1]): 
        pxl_colour = color() 
        img.putpixel((x,y), pxl_colour)