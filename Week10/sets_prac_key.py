"""
Session 10 B
"""

def intersection(set1, set2):
    intersection = set()
    for item in set1:
        if item in set2:
            intersection.add(item)
    return intersection

def read_file(filename):
    store = set()
    with open(filename) as file:
        for line in file:
            line = line.strip()
            store.add(line)
    return store

def in_store(item, store_items):
    return item in store_items

def main():
    store_set1 = read_file("cornerstore.txt")
    store_set2 = read_file("walmart.txt")
    print(store_set1)
    print(in_store("rice", store_set1))
    print("Intersection", intersection(store_set1, store_set2))

if __name__ == "__main__":
    main()
