"""
Session 6 A
"""
from csv import reader

# What do we need to import??

def read_file(filename):
    """
    This function takes a filename as an argument, and opens the file.
    Then, it reads each line of the file and prints "Hello, name" where
    name is the name of the person in the file. It also prints
    out the longest name of the entire file.
    """
    # How do we know that the give filename exists and is valid? Let's add a try/except block!
    # Add two except blocks: 1 for a FileNotFoundException and 1 for a general Exception
    # Print an error message when you catch those exceptions
    try:
        with open(filename) as f:
            csv_reader = reader(f)
            next(csv_reader)
            namelen = 0
            name = ""
            for line in csv_reader:
                print ("Hello", line[1], ".", sep=" ")
                if namelen < len(line[1]):
                    namelen = len(line[1])
                    name = line[1]
            print (name, "has the longest first name.")
    except FileNotFoundError: 
        print("File not found.")
    except Exception:
        print("Unknown error.")



def main():
    """
    The main function calls the read_file and write_to_file function, 
    using the people.csv file as an argument for both.
    """
    read_file("people1.csv")


if __name__ == "__main__":
    main()