import json
from User import User

class Signup():
    def create_user(self):
            users = []
            data = self.getUser()
            print(data)
            try:
                with open('data.json', 'r') as file:
                    users = json.load(file)
            except FileNotFoundError:
                users = []
            except json.JSONDecodeError:
                users = []

            users.append(self.getUser())

            with open('data.json', 'w') as file:
                json.dump(users, file, indent=4)
            