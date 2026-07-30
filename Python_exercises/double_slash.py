# Define the divider value

num1 = 5

# Define the divisor value

num2 = 2

# Divide using single slash

result = num1 / num2

print("The division result of %d/%d = %0.2f" % (num1, num2, result))

print("The type of the result", type(result))

# Divide using double slash

result = num1 // num2

print("The division result of %d//%d = %0.2f" % (num1, num2, result))

print("The type of the result", type(result))

# Divide using double slash and float divisor value

result = num1 // float(num2)

print("The division result of %d//%0.2f = %0.2f" % (num1, num2, result))

print("The type of the result", type(result))

# Divide using double slash and float divider value

result = float(num1) // num2

print("The division result of %0.2f//%d = %0.2f" % (num1, num2, result))

print("The type of the result", type(result))