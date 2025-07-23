#!/usr/bin/python3
"""
Pattern Drawing Program
Draws a square pattern of asterisks based on user input
"""

def draw_square_pattern():
    """Draw a square pattern using nested loops"""
    try:
        size = int(input("Enter the size of the pattern: "))
        
        if size <= 0:
            print("Please enter a positive integer.")
            return
        
        row = 0
        while row < size:
            for col in range(size):
                print("*", end=" ")
            print()  # New line after each row
            row += 1
    
    except ValueError:
        print("Please enter a valid positive integer.")

if __name__ == "__main__":
    draw_square_pattern()