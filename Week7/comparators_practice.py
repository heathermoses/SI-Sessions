"""
Comparators
"""

def print_alphabetical(string1, string2, comparator):
    if comparator(string1[0], string2[0]) == True:
        print(string1, string2)
    else:
        print(string2, string1)

def comparator(char1, char2):
    char1_ascii = ord(char1)
    char2_ascii = ord(char2)
    if char1_ascii < char2_ascii:
        return True
    else:
        return

def main():
    print_alphabetical("xyz", "abc", comparator)

if __name__ == "__main__":
    main()