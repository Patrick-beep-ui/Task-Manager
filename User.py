import json

class User:
    first_name = None
    last_name = None
    username = None
    password = None
    
    def __init__(self, first_name, last_name, username, password):
        self.setFirstName(first_name)
        self.setLastName(last_name)
        self.setUsername(username)
        self.setPassword(password)
        self.id = self.generate_id(self)
        self.tasks = []
        #self.create_user()
    
    def setFirstName(self, first_name):
        self.first_name = first_name
    
    def setLastName(self, last_name):
        self.last_name = last_name
        
    def setUsername(self, username):
        self.username = username
    
    def setPassword(self, password):
        self.password = password
        
    def getFirstName(self):
        return self.first_name
    def getLastName(self):
        return self.last_name
    def getUsername(self):
        return self.username
    def getPassword(self):
        return self.password
    
    def __str__(self) -> str:
        return f"ID: {self.id} \n Name: {self.first_name} \n Last Name: {self.last_name} \n Username: {self.username} \n Password: {self.password}"
    
    @staticmethod
    def generate_id(self):
        users = self.load_users()
        if users:
            max_id = max(user["id"] for user in users)
            return max_id + 1
        else:
            return 1
    
    def getUser(self):
        return {
              "id": self.id,
              "first_name": self.first_name,
                "last_name": self.last_name,
                "username": self.username,
                "password": self.password,
                "tasks": self.tasks
        }
    
    def find_user_id_by_username(self, username):
        try:
            with open('data.json', 'r') as file:
                users = json.load(file)
                for user in users:
                    if user['username'] == username:
                        return user['id']
        except FileNotFoundError:
            print("Data file not found.")
        return None
    
    @staticmethod
    def load_users():
        try:
            with open('data.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
            
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
            
            