#!/usr/bin/python3
"""
Multiplication Table Generator
Generates and prints the multiplication table for a given number
"""

def generate_multiplication_table():
    """Generate and print multiplication table for user input"""
    try:
        number = int(input("Enter a number to see its multiplication table: "))
        
        print(f"Multiplication table for {number}:")
        for i in range(1, 11):
            print(f"{number} * {i} = {number * i}")
    
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    generate_multiplication_table()