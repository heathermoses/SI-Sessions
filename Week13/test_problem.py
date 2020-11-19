"""
Session 13 A
"""


import problem_solving


def test_create_user():
    user_1 = problem_solving.User("cim4692@rit.edu", "Cooper", "123")
    assert user_1.email == "cim4692@rit.edu"
    assert user_1.get_password() == 6


def main():
    test_create_user()


if __name__ == "__main__":
    main()