"""
Author: Heather Moses
Session 5 B

This is a short review of edge cases
"""
import edge_cases

def test_menu():
    assert(edge_cases.menu(0) == "Hamburger")
    assert(edge_cases.menu(-1) is None)
    assert(edge_cases.menu(1000) == "Apple")
    assert(edge_cases.menu(999) == "Apple")
    assert(edge_cases.menu(1001) is None)
    print("All tests passed")

def main():
    test_menu()


if __name__ == "__main__":
    main()