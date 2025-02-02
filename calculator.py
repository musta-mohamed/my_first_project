import math

def calculator():
    print('''
     Simple Calculator 
    
    1. Addition (+)
    2. Subtraction (-)
    3. Multiplication (*)
    4. Division (/)
    5. Modulus (%)
    6. Exponentiation (**)
    7. Floor Division (//)
    ''')
  # Taking user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /, %, **, //): ")

  # Performing calculations
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero!"
    elif operation == "%":
        result = num1 % num2
    elif operation == "**":
        result = num1 ** num2
    elif operation == "//":
        if num2 != 0:
            result = num1 // num2
        else:
            return "Error: Division by zero!"
    else:
        return "Invalid operation!"

    return f"Result: {result}"

# Run the calculator
print(calculator())
