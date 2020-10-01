"""
Comparators Example
"""

def print_alphabetical(comparator, string1, string2):
    if comparator(string1, string2) == True:
        print(string1, string2)
    else:
        print(string2, string1)

def comparator(string1, string2):
    string1_first = ord(string1[0])
    string2_first = ord(string2[0])
    return string1_first <= string2_first


def main():
    print_alphabetical(comparator, "abc", "xyz")

if __name__ == "__main__":
    main()