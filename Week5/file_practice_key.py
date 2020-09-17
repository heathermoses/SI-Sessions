"""
Session 5B Key
"""

def read_file(filename):
    """
    This function takes a filename as an argument, and opens the file.
    Then, it reads each line of the file and prints "Hello, name" where
    name is the name of the person in the file. It also prints
    out the longest name of the entire file.
    """
    line_count = 0
    name_count = 0
    max_count = 0
    max_name = " "
    with open(filename) as file:
        for line in file:
            line_count += 1
            if line_count == 1:
                continue
            else:
                stripped_line = line.strip()
                stripped_line = stripped_line.split(", ")
                print("Hello,", stripped_line[1])
                name_count = 0
                for ch in stripped_line[1]:
                    name_count += 1
                if name_count > max_count:
                    max_count = name_count
                    max_name = stripped_line[1]
        print("The person with the longest name is: ", max_name)

def write_to_file(filename):
    """
    This function writes to the given file and overrides any content
    already in the file. The content is replaced with other hard-coded
    names. 
    """
    with open(filename, "w") as file:
        file.write("Moses, Heather, 2, Software Engineering\n")
        file.write("Deer, John, 5, Computer Science")

def main():
    """
    The main function calls the read_file and write_to_file function, 
    using the people.csv file as an argument for both.
    """
    read_file("../Week5/people.csv")
    write_to_file("../Week5/people.csv")


if __name__ == "__main__":
    main()