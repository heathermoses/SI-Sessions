"""
Session 11 A
"""
import arrays

def list_to_array(my_list):
    array_size = len(my_list)
    my_array = arrays.Array(array_size)
    for i in range(array_size):
        my_array[i] = my_list[i]
    return my_array

def main():
    my_list = [1,2,3,4,5,6,7,8,9,10]
    print("My list: ", my_list)
    my_array = list_to_array(my_list)
    print("My array: ", my_array)

if __name__ == "__main__":
    main()
