# Program to add and subtract two numbers entered

# User to input two numbers
num1 = float(input("Enter the first number (num1): "))
num2 = float(input("Enter the second number (num2): "))

# Addition
add_result = num1 + num2

# Subtraction
sub_result = num1 - num2

# Display results
print(f"Addition of {num1} and {num2} is: {add_result}")
print(f"Subtraction of {num1} and {num2} is: {sub_result}")

# Multiplication
mul_result = num1 * num2

# Division (handle division by zero)
if num2 != 0:
    div_result = num1 / num2
else:
    div_result = "Undefined (division by zero)"

# Display results
print(f"Addition of {num1} and {num2} is: {add_result}")
print(f"Subtraction of {num1} and {num2} is: {sub_result}")
print(f"Multiplication of {num1} and {num2} is: {mul_result}")
print(f"Division of {num1} by {num2} is: {div_result}")
