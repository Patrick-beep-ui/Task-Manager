import json
from User import User

class Task(User):
    title = None
    state = None
    date = None
    priority = None
    
    def __init__(self, title, state, date, priority, user_id):
        self.setTitle(title)
        self.setState(state)
        self.setDate(date)
        self.setPriority(priority)
        self.user_id = user_id
        self.id = self.generate_id(self)
        #self.create_task()
        
    def setTitle(self, title):
        self.title = title
    
    def setState(self, state):
        self.state = state
    
    def setDate(self, date):
        self.date = date
    
    def setPriority(self, proprity):
        self.priority = proprity
    
    def getTitle(self):
        return self.title
    def getState(self):
        return self.state
    def getDate(self):
        return self.date
    def getPriority(self):
        return self.priority
    
    def __str__(self) -> str:
        return f"ID: {self.id} \n Title: {self.title} \n State: {self.state} \n Date: {self.date} \n Priority: {self.priority}"
    
    @staticmethod
    def generate_id(self):
        users = Task.load_users()
        max_id = 0
        for user in users:
            for task in user["tasks"]:
                max_id = max(max_id, task["id"])
        return max_id + 1
    
    def getTask(self):
        return {
            "id": self.id,
            "Title": self.title,
            "State": self.state,
            "Date": self.date,
            "Priority": self.priority,
            "user_id": self.user_id
        }
        
    def create_task(self):
        tasks = []
        try:
            with open('data.json', 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            return 
        
        for user in users:
            if user['id'] == self.user_id:
                user['tasks'].append(self.getTask())
                break 
        
        with open('data.json', 'w') as file:
            json.dump(users, file, indent=4)
    
    def edit_task(self, user_id, task_id, new_task_data): 
        try:
            users = Task.load_users()
            for user in users:
                if user["id"] == user_id:
                    for task in user["tasks"]:
                        if task["id"] == task_id:
                            for key, value in new_task_data.items():
                                if key in task:
                                    task[key] = value
                            with open('data.json', 'w') as file:
                                json.dump(users, file, indent=4)
                            return True  
            return False  
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
    