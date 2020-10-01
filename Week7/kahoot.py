"""
Questions for Kahoot Quiz Session 7 A
"""

def foo(start, stop):
    if start == 0 and stop == 0:
        print("Invalid start and stop values")
    if start >= stop:
        return
    else:
        print(start)
        foo(start + 2, stop)

def main():
    foo(0, 11)

main()

