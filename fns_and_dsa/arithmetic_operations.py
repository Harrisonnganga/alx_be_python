#!/usr/bin/python3
"""
Arithmetic Operations Module
Provides basic arithmetic operations through the perform_operation function
"""

def perform_operation(num1: float, num2: float, operation: str) -> float | str:
    """
    Performs basic arithmetic operations on two numbers
    
    Args:
        num1: First operand
        num2: Second operand
        operation: Type of operation (add, subtract, multiply, divide)
    
    Returns:
        Result of the operation or error message for division by zero
    """
    operation = operation.lower().strip()
    
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Error: Division by zero"
            return num1 / num2
        case _:
            return "Error: Invalid operation"