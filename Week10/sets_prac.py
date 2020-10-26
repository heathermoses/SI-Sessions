"""
Session 10 B
"""

def intersection(set1, set2):
    """
    This function takes two sets and determines the 
    intersection of these two sets.
    Return the intersection.
    """
    pass

def read_file(filename):
    """
    This function takes a filename and creates a set of everything
    in the file. 
    Return the set.
    """
    try:
        shoppinglist = set()
        with open(filename) as f:
            for item in f:
                stripped = item.strip()
                shoppinglist.add(stripped)
        return shoppinglist
    except:
        print("File doesnt exist or other error.")

def in_store(item, store_items):
    """
    This function returns true if "item" is in the set "store_items".
    Otherwise, return false if "item" is not in the set "store_items".
    """
    item_set = {item}
    for val in item_set: 
        if val in store_items:
            return True
    return False

def main():
    shoppinglist = read_file("cornerstore.txt")
    # Determine if "rice" is in the cornerstore file
    res = in_store("rice", shoppinglist)
    print(res)
    # Determine if "reeses pieces" is in the cornerstore file
    res = in_store("reeses pieces", shoppinglist)
    print(res)
    # Determine if "bananas" is in the cornerstore file

    # Determine if "cheese" is in the cornerstore file

    # Determine if "rice" is in the cornerstore file

    # Print out the intersection of the "cornerstore.txt" file and the "walmart.txt" file
    pass

if __name__ == "__main__":
    main()
