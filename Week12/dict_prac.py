"""
Session 12 B
"""

def word_count(filename):
    dictionary = dict()
    with open(filename) as f_input:
        for line in f_input:
            words = line.strip().split()
            for word in words:
                word = word.lower()
                if word in dictionary:
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1
    return dictionary

def main():
    """
    This function should open the file "random.txt" and read through every word
    and determine how many times each word is repeated using a dictionary.
    Remember to strip your lines and lower your words!
    """
    dictionary = word_count("random.txt")
    print(dictionary)

if __name__ == "__main__":
    main()