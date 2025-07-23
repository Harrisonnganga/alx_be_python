#!/usr/bin/python3
"""
Simple Calculator using Match Case
Performs basic arithmetic operations based on user input
"""

def calculator():
    """Get user input and perform calculations using match case"""
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose the operation (+, -, *, /): ")
        
        match operation:
            case "+":
                result = num1 + num2
                print(f"The result is {result}")
            case "-":
                result = num1 - num2
                print(f"The result is {result}")
            case "*":
                result = num1 * num2
                print(f"The result is {result}")
            case "/":
                if num2 == 0:
                    print("Cannot divide by zero")
                else:
                    result = num1 / num2
                    print(f"The result is {result}")
            case _:
                print("Invalid operation. Please choose from +, -, *, /")
    
    except ValueError:
        print("Please enter valid numbers")

if __name__ == "__main__":
    calculator()