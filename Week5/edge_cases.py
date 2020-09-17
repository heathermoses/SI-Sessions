"""
Author: Heather Moses
Session 5 B

This is a short review of edge cases
"""

def menu(price):
    if (price < 0):
        return None
    elif (price > 1000):
        return None
    elif (price >= 0 and price <= 4.99):
        return "Hamburger"
    elif (price >= 5 and price <= 9.99):
        return "Cake"
    elif (price == 10 and pricte <= 19.99):
        return "Steak"
    else:
        return "Apple"

def main():
    user_input = int(input("How much would you like to pay for something from the menu?: "))
    item = menu(user_input)
    print("You get: ", item)


if __name__ == "__main__":
    main()