# Calculator

# Addition function
def addition(x, y):
    return x + y

# Subtraction function
def subtraction(x, y):
    return x - y

# Multiplication function
def multiplication(x, y):
    return x * y

# Division function
def division(x, y):
    return x / y

print("Select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

# User input for operation choice
choice = input("Enter choice (1/2/3/4): ")

# User input for two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Perform operation based on user choice
if choice == '1':
    print(num1, "+", num2, "=", addition(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtraction(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiplication(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", division(num1, num2))
else:
    print("Invalid input")

