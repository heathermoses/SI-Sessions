"""
Session 8 A
"""
# What do we need to import?

import csv

def read_file(filename):
    """
    This function takes a filename as an argument, and opens the file.
    Then, it reads and prints each line of the file
    Example: "Intro to Software Development is taught by Hamza"
    """
    try:    
        with open(filename) as input_file:
            csv_file = csv.reader(input_file)
            header = next(csv_file)
            for line in csv_file:
                print(line[0], "is taught by ", line[1])
    except FileNotFoundError:
        print("The file could not be found.")
    except:
        print("General error")
        # How do we know that the give filename exists and is valid? Let's add a try/except block!
    # Add an except block: 1 for a FileNotFoundException
    # Print an error message when you catch those exceptions


def main():
    read_file("rit_classes.csv")

if __name__ == "__main__":
    main()