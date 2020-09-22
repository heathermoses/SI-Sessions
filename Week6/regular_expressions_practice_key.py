"""
Session 6 A
"""

import re

def main():
    """
    Work together to solve these problems! Find all of the matches
    """
    # 1: Given the string, find and print all digit characters (numbers)
    string_1 = "95!3###?!"
    for match in re.findall("\d", string_1):
        print(match)

    # 2: Given the string, find and print all non-digit characters (letters)
    string_2 = "Hello World!"
    for match in re.findall("\D", string_2):
        print(match)

    # 3: Given the string, find and print all numbers in pairs of 2
    string_3 = "112233445599887766!?!?!?"
    for match in re.findall("\d\d", string_3):
        print(match)

    # 4: Given the string, find and print all non-alphanumeric characters
    string_4 = "23112!%*Heyheyhey"
    for match in re.findall("\W", string_4):
        print(match)

    # 5: Given the string, find and print all characters within the range 'a' to 'k'
    string_5 = "123456789asdfghjk"
    for match in re.findall("[a-k]", string_5):
        print(match)


if __name__ == "__main__":
    main()