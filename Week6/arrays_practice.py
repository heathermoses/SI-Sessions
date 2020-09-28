"""
Step 1: Using the arrays.py module from class, 
create a function that creates an array 
based on a text file full of items (1 item per line).

Step 2: Write a linear search function that returns
the index of a item or returns None 
if the item wasn’t found, given an array and target value as parameters.

Step 3: In main(), print an item found message with the name of the item
or an item not found message with the name of the item, depending on the returned value.
"""
import arrays

# Step 1
def get_file_length(filename):
    with open(filename) as f:
        line = 0
        for l in f:
            line += 1
            if l == "":
                continue
    return line

def arrays_from_file(filename):
    length = get_file_length(filename)
    an_array = arrays.Array(length)
    with open(filename) as f:
        n = 0
        for l in f:
            stripped = l.strip()
            an_array[n] = stripped
            n += 1
    return an_array

# Step 2
def item_search(file_array, target):
    length = len(file_array)
    for l in range(length):
        if file_array[l] == target:
            return l
        else:
            return None

# Step 3
def main():
    stockroom_array = arrays_from_file("stockroom.txt")
    dining_room_table = item_search(stockroom_array, "dining room table")
    if dining_room_table == None:
        print("Dining room table not found.")
    else:
        print("Item was found.")
 
if __name__ == "__main__":
    main()  