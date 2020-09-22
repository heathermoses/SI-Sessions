"""
Session 5B
"""

def read_file(filename):
    '''
    reads and prints the first and last name of each person in file, then prints hello statement
    also prints the longest name
    '''
    f = open(filename)
    line_count = 0
    namelen = 0
    name = ""
    for line in f:
        line_count += 1
        if line_count == 1:
            continue
        s = line.split(", ")
        print ("Hello", s[1], ".")
        if namelen < len(s[1]):
            namelen = len(s[1])
            name = s[1]
    print (name, "has the longest first name.")
    f.close()
    

def override_file(filename):
    '''
    adds a new student to the end of the file
    '''
    f = open(filename, 'a')
    f.write("\nHartley, Carissa, 1, Computing Security")
    f.close()
    

def main():
    read_file("../Week5/people.csv")
    override_file("people.csv")


if __name__ == "__main__":
    main()