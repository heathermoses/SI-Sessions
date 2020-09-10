"""
Week 4 SI Session A
Author: Heather Moses (hlm8500@rit.edu)
Date: 9/7/20
Course: SWEN/CSEC-123-11
"""

def foo(color):
    return (color == "yellow")

def main():
    if (foo("red") and foo("yellow") and foo("red") == True):
        print("Do the wobble")
    elif (foo("green") or foo("blue") == True):
        print("Do the macarena")
    elif (foo("yellow") or foo("green") == False):
        print("Do the turbo hustle")
    else:
        print("Make up your own dance!")


main()