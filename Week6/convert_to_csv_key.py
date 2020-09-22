"""
Session 6 A
"""

import csv

def read_file(filename):
    """
    This function takes a filename as an argument, and opens the file.
    Then, it reads each line of the file and prints "Hello, name" where
    name is the name of the person in the file. It also prints
    out the longest name of the entire file.
    """
    try:
        namelen = 0
        name = " "
        f = open(filename)
        csv_reader = csv.reader(f)
        next(csv_reader)

        for record in csv_reader:
            print ("Hello", record[1], ".", sep=" ")
            if namelen < len(record[1]):
                namelen = len(record[1])
                name = record[1]
        print (name, "has the longest first name.")
        f.close()
    
    # Specific exception
    except FileNotFoundError as fnfe:
        print("This file doesn't exist or is invalid!")
        raise fnfe

    # General exception
    except Exception as e:
        print("This is the general exception")
        raise e


def main():
    """
    The main function calls the read_file and write_to_file function, 
    using the people.csv file as an argument for both.
    """
    read_file("people.csv")


if __name__ == "__main__":
    main()