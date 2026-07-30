cel = input("Please enter a temperature in degrees Celsius: ")
cel_float = float(cel)
fahr = round((cel_float * 1.8000 + 32.00), 2)

print("Celsius: " + cel)
print("Fahrenheit: " + str(fahr))