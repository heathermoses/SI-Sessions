"""
Session 11 A
"""
import random

def hash_string_example(string):
    """
    What is wrong with this hash function?
    """
    string_length = len(string)
    index1 = string_length // 2
    index2 = string_length - 1
    hashed = 12 * (ord(string[index1]) + (3 * ord(string[index2]))) + random.randint(1, 500)
    return hashed

def hash_slinging_slasher(a_string):
    '''
    makes a hash
    '''
    hashed = 0
    length = len(a_string)
    for ch in range(0, length):
        hashed += ord(a_string[ch])*(21**(ch+3))
    return hashed


def main():
    string1 = "software development"
    string2 = "hello"
    print(hash_string_example(string1))
    print(hash_string_example(string2))
    a_string = "apples"
    b_string = "oranges"
    print(hash_slinging_slasher(a_string))
    print(hash_slinging_slasher(b_string))



if __name__ == "__main__":
    main()
