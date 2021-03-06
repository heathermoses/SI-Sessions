"""
Session 11 A
"""
import arrays

def list_to_array(my_list):
    """
    This function takes a list and returns an array of that list
    """
    my_array = arrays.Array(len(my_list))
    for index in range(len(my_list)):
        my_array[index] = my_list[index]
    return my_array

def main():
    my_list = [1,2,3,4,5,6,7,8,9,10]
    print("My list: ", my_list)
    my_array = list_to_array(my_list)
    print("My array: ", my_array)

if __name__ == "__main__":
    main()
