"""
Week 3 SI Session A
Author: Heather Moses (hlm8500@rit.edu)
Date: 8/31/20
Course: SWEN/CSEC-123-11

This program is the key to the task_manager activity
"""

def task_manager(item1, item2, item3, item4):
    """
    This function has 4 parameters (item1 through item4), which are items
    that the user wishes to add to their to-do list.
    This function prompts the user to enter their name, and then
    greets the user and prints their name and the 4 tasks they want to do.
    """
    name = input("Please enter your name: ")
    print("Hello,", name, "!")
    print("This is your to-do list:")
    print("1. ", item1)
    print("2. ", item2)
    print("3. ", item3)
    print("4. ", item4)

def main():
    """
    This main function calls the task_manager function
    """
    task_manager("SWEN/CSEC-123 homework", "Clean room", "Eat dinner", "Go to SI session")

main()
