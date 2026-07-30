def color(i: int, max_i: int) -> tuple[int, int, int]:
    # Farbton in Abhängigkeit der benötigten Schleifendurchläufe.
    hue = int(255 * (i / max_i))

    # Volle Helligkeit 255, außer wenn c Teil der Mandelbrotmenge ist.
    # Dadurch wird das innere schwarz.
    value = 255 if i < max_i else 0

    # Volle Sättigung
    saturation = 255

    return (hue, saturation, value)
