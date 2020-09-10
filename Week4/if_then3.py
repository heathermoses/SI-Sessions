"""
Week 4 SI Session A
Author: Heather Moses (hlm8500@rit.edu)
Date: 9/7/20
Course: SWEN/CSEC-123-11
"""

def foo(int1, int2):
    x = int1 - int2
    x = x - 5
    return x

def main():
    if (foo(4, 5) == 8):
        print("Make a silly face")
    elif (foo(9, 2) >= 9):
        print("Dance!")
    elif (foo(20, 8) != 7):
        print("Strike a pose")
    else:
        print("Moo as loud as you can")

main()