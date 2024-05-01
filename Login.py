import json
from User import User

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def authenticate(self):
        users = User.load_users()
        for user in users:
            if user['username'] == self.username and user['password'] == self.password:
                return True
        return False
