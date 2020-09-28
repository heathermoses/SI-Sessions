"""
Step 1: Using the arrays.py module from class, create a function that creates an array based on a text file full of items (1 item per line).
Step 2: Write a helper function that returns the number of items in the array that begin with the letter “a” or “A” when given an array as a parameter.
Step 3: Write a linear search function that returns the index of a item or returns None if the item wasn’t found, given an array and target value as parameters.
Step 4: In main(), print an item found message with the name of the item or an item not found message with the name of the item, depending on the returned value.
"""
import arrays

# Step 1
def get_file_length(filename):
    length = 0
    with open(filename) as a_file:
        for line in a_file:
            length += 1
    return length

def arrays_from_file(filename):
    length = get_file_length(filename)
    file_array = arrays.Array(length)
    count = 0
    with open(filename) as a_file:
        for line in a_file:
            line = line.strip()
            file_array[count] = line
            count += 1
    return file_array

# Step 2
def a_count(file_array):
    length = len(file_array)
    num_a = 0
    for i in range(length):
        word = file_array[i]
        if word[0] == "a" or word[0] == "A":
            num_a += 1
    return num_a

# Step 3
def item_search(file_array, target):
    length = len(file_array)
    for i in range(length):
        if file_array[i] == target:
            return i
    return None

def main():
    items = arrays_from_file("stockroom.txt")
    num_a = a_count(items)
    output = item_search(items, "apricot")
    if output == None:
        print("apricot was not found!")
    else:
        print("apricot was found!")

if __name__ == "__main__":
    main()