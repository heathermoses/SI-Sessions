"""
Session 10 A
"""
import math

def pythagorean(int1, int2):
    """
    This function takes two numbers and uses Pythagorean Theorem
    to return the "hypotenuse"
    """
    return math.sqrt(int1**2 + int2**2) 

def read_file(filename):
    """
    This function takes a filename (assume .txt file) and
    reads through every line and prints the line
    """
    try:
        with open(filename) as file:
            for line in file:
                line.strip()
                print(line)
    except:
        print("errror")

def divide_calculator(int1, int2):
    """
    This function determines if int1 divided by int2 is equal
    to int2 divided by int1
    Return true if yes, return false if no
    """
    try:
        divide1 = int1 / int2
        divide2 = int2 / int1
        return divide1 == divide2
    except ZeroDivisionError:
        print("Cannot divide by zero.")

def main():
    print(pythagorean(3, 4))
    read_file("test_file.txt")
    divide_calculator(1, 0)

if __name__ == "__main__":
    main()
