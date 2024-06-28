print("Welcome to Simple Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation: (+, -, *, /): ")

if operation == '+':
    print("Result:", num1 + num2)
elif operation == '-':
    print("Result:", num1 - num2)
elif operation == '*':
    print("Result:", num1 * num2)
elif operation == '/':
    if num2 == 0:
        print("Error! Division by zero.")
    else:
        print("Result:", num1 / num2)
else:
    print("Invalid operation.")

print("Thank you for using Simple Calculator.")
