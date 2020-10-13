"""
Session 8A
"""

def countdown(n):
    """
    This function starts at n, and counts down to 0
    It does not print 0. Once the countdown is finished, print "Done!"
    """
    if n < 0:
        print("ERROR! Invalid input")
    elif n == 0:
        print("Done!")
    else:
        print(n)
        return countdown(n-1)

def main():
    countdown(10)

if __name__ == "__main__":
    main()