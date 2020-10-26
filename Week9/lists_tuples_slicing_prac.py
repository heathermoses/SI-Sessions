"""
Session 9 A
"""

def lists_prac():
    # define a list and give it the initial values of 1, "hello", 2, "goodbye", and 3
    list_1 = [1, "hello", 2, "goodbye", 3]
    # create another list and append it to your first list
    list_2 = [4, 7 ,"hi"]
    # list_1.append(list_2)

    list_1.append(list_2)

    print("Append:", list_1)
    list_1 = [1, "hello", 2, "goodbye", 3]
    list_2 = [4, 7 ,"hi"]
    list_1 += list_2
    print("+=: ", list_1)

    # pop the third value and print out that value
    print(list_1.pop(2))
    
    # insert a new value of "SI is the best" at index 5 
    list_1.insert(5, "SI is the best")
    # print out the list
    print(list_1)
    # return the list as is
    return list_1

def tuples_prac():
    # define a tuple and give it the initial values of 1, 2, 3, "a", "b", "c"

    # print the size of the tuple

    # print each element inside of the tuple

    # return the tuple as is

    pass

def slicing_prac():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # print out every third value in list1

    # print out the last 4 values in list1

    # print out every value in the list backwards (reverse the list)

    string1 = "sunshine daises butter mellow"

    # print out the words "sunshine daises"

    # print out every other letter in string1

    # print out "daises butter"

    # return the word "butter" from string1

    pass

def main():
    lists_prac()

if __name__ == "__main__":
    main()