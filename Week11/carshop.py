"""
Session 11 B
"""

# Let's make a car class!
# Make a class for a car with at least 5 fields
# Set default values for 3 of your fields
class Car:
    def __init__(self, name="Car", door_num=4, color="red", eng_type="strong", max_speed=100):
        self.name = name
        self.door_num = door_num
        self.color = color
        self.eng_type = eng_type
        self.max_speed = max_speed



def print_class(carobject):
    """
    This function takes a Car object and prints out all variables on one line
    """
    print("Name: ", carobject.name, "\tNum of doors: ", carobject.door_num, "\tColor: ", carobject.color, "\tEngine type: ", carobject.eng_type, "\tMax Speed: ", carobject.max_speed)

def main():
    # Make an instance of a car with the default values
    car1 = Car()
    # Make an instance of a car and change the default values
    car2 = Car("Jeep", 0, "Blue", "v_8", 20)
    # Make another instance of a car and change the default values
    car3 = Car("Mustang", 2, "Gold", "v2", 5)
    # Print out the types of all of the cars you instantiated
    print_class(car1)
    print_class(car2)
    print_class(car3)


if __name__ == "__main__":
    main()
