"""
Session 9 B
"""

def checkers():
    """
    A standard checker board is of size 8 x 8 (meaning there are 64 squares)
    Create a "checker board" using a 2-dimensional list
    Fill in the checker board with blank spaces
    """
    dimension = 8
    checkerboard = [[0 for x in range(dimension)] for y in range(dimension)]
    return checker_board

def main():
    print(checkers())

if __name__ == "__main__":
    main()
