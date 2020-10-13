"""
Session 8A
"""

def countdown(n):
    """
    This function starts at n, and counts down to 0
    It does not print 0. Once the countdown is finished, print "Done!"
    """
    if n < 0:
        print("Invalid input.")
        return
    elif n == 0:
        print("Done!")
    else:
        print(n)
        n = n - 1
        return countdown(n)
    # What cases do we need for recursion? 
    # Make sure to check for valid input (no negative values!)

def main():
    countdown(10)

if __name__ == "__main__":
    main()