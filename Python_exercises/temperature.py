def celsius_to_fahrenheit(celsius: float) -> float:
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    celsius = fahrenheit * 5 / 9 - 32
    return celsius


def celsius_to_kelvin(celsius: float) -> float:
    kelvin = celsius + 273.15
    return kelvin


def kelvin_to_celsius(kelvin: float) -> float:
    celsius = kelvin - 273.15
    return celsius


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = celsius_to_kelvin(celsius)
    return kelvin


def kelvin_to_fahrenheit(kelvin: float) -> float:
    celsius = kelvin_to_celsius(kelvin)
    fahrenheit = celsius_to_fahrenheit(celsius)
    return fahrenheit


if __name__ == "__main__":
    source_unit = input("Enter source unit [C / F /K]: ")
    source_value = float(input("Enter source value: "))
    target_unit = input("Enter target unit [C / F / K]: ")
    if source_unit == "C":
        if target_unit == "F":
            converted = celsius_to_fahrenheit(source_value)
        else:
            converted = celsius_to_kelvin(source_value)
    elif source_unit == "F":
        if target_unit == "C":
            converted = fahrenheit_to_celsius(source_value)
        else:
            converted = fahrenheit_to_kelvin(source_value)
    else:
        if target_unit == "C":
            converted = kelvin_to_celsius(source_value)
        else:
            converted = kelvin_to_fahrenheit(source_value)
    print(source_value, "corresponds to", converted, target_unit + ".")
