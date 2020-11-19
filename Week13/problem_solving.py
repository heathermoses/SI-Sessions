"""
Session 13 A
"""

class User:
    __slots__ = ['email', 'username', '__password', 'status']

    def get_password(self):
        return self.__password

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.__password = len(self.__password) * 2
        self.status = False
    
    def login(self, password):
        password_hash = len(password) * 2
        if self.__password == password_hash:
            self.status = True
        else: 
            return False

    def logout(self):
        self.status = False
        


class Chat:
    __slots__ = ['sender', 'recipient', 'message']

    def __init__(self, sender, recipient, message):
        self.sender = sender
        self.recipient = recipient
        self.message = message

def main():
    pass


if __name__ == "__main__":
    main()
