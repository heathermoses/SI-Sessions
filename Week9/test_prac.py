"""
Session 9 A
"""
import lists_tuples_slicing_prac

def test_perim():
    assert(round(prac.perim(5), 4) == 15.708)
    assert(round(prac.perim(3), 4) == 9.4248)
    assert(round(prac.perim(20), 4) == 62.8319)
    assert(round(prac.perim(8), 4) == 25.1327)
    assert(prac.perim(-100) is None)
    assert(prac.perim(-5) is None)
    assert(prac.perim(-1) is None)

def test_lists():
    pass

def test_tuples():
    pass

def test_slicing():
    pass

def main():
    test_perim()


if __name__ == "__main__":
    main()
