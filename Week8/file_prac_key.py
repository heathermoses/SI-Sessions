"""
Session 8 A
"""
from csv import reader

def read_file(filename):
    """
    This function takes a filename as an argument, and opens the file.
    Then, it reads and prints each line of the file
    Example: "Intro to Software Development is taught by Hamza"
    """
    # How do we know that the give filename exists and is valid? Let's add a try/except block!
    # Add an except block: 1 for a FileNotFoundException
    # Print an error message when you catch those exceptions
    try:
        with open(filename) as f:
            csv_reader = reader(f)
            next(csv_reader)
            for line in csv_reader:
                print (line[0], "is taught by", line[1])
    except FileNotFoundError: 
        print("File not found.")


def main():
    read_file("rit_classes.csv")

if __name__ == "__main__":
    main()