"""
Session 11 A
"""
import random

def hash_string_example(string):
    string_length = len(string)
    index1 = string_length // 2
    index2 = string_length - 1
    hashed = 12 * (ord(string[index1]) + (3 * ord(string[index2]))) + random.randint(1, 500)
    return hashed

def main():
    string1 = "software development"
    string2 = "hello"
    print(hash_string_example(string1))
    print(hash_string_example(string2))

if __name__ == "__main__":
    main()
