import json
from User import User
from datetime import datetime

class Task(User):
    title = None
    state = None
    date = None
    priority = None
    
    def __init__(self, title, state, date, priority, user_id, comments=None):
        self.setTitle(title)
        self.setState(state)
        self.setDate(date)
        self.setPriority(priority)
        self.user_id = user_id
        self.comments = comments if comments is not None else []
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
            "user_id": self.user_id,
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
    
    def delete_task(self, user_id, task_id):
        try:
            users = Task.load_users()
            for user in users:
                if user["id"] == user_id:
                    for task in user["tasks"]:
                        if task["id"] == task_id:
                            user["tasks"].remove(task)
                            with open('data.json', 'w') as file:
                                json.dump(users, file, indent=4)
                            return True
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
    
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
        
    def show_tasks(self, user_id):
        try:
            tasks = []
            data = Task.load_users()
            for user in data:
                if user["id"] == user_id:
                    for task in user["tasks"]:
                        user_task = {
                            "ID": task["id"],
                            "Title": task["Title"],
                            "State": task["State"],
                            "Date": task["Date"],
                            "Priority": task["Priority"]
                        }
                        tasks.append(user_task)
                    return tasks
                        
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
    
    def get_tasks_for_date(self, user_id, date):
        try:
            tasks = []
            data = Task.load_users()
            for user in data:
                if user["id"] == user_id:
                    for task in user["tasks"]:
                        if date == task["Date"]:
                            user_task = {
                                "ID": task["id"],
                                "Title": task["Title"],
                                "State": task["State"],
                                "Date": task["Date"],
                                "Priority": task["Priority"]
                            }
                            tasks.append(user_task)
            return tasks  
        except FileNotFoundError:
            return []  
        except json.JSONDecodeError:
            return []
        
    def get_tasks_for_period(self, user_id, start_date, end_date):
        try:
            tasks = []
            data = Task.load_users()

            for user in data:
                if user["id"] == user_id:
                    for task in user["tasks"]:
                        task_date = task["Date"]
                        if start_date <= task_date <= end_date:
                            user_task = {
                                "ID": task["id"],
                                "Title": task["Title"],
                                "State": task["State"],
                                "Date": task["Date"],
                                "Priority": task["Priority"]
                            }
                            tasks.append(user_task)
            return tasks  
        except FileNotFoundError:
            return []  
        except json.JSONDecodeError:
            return []
    
                
    def filter_task(self, user_id, attribute, value):
        tasks = []
        data = Task.load_users()
        for user in data:
            if user["id"] == user_id:
                for task in user["tasks"]:
                    if attribute == "Title" and value.lower() in task["Title"].lower():
                        tasks.append(task)
                    elif task.get(attribute) == value:
                        tasks.append(task)
        return tasks
    
    # Comments Functionality
    
    def get_comments(self):
        return self.comments

    def show_comments(self, user_id, task_id):
        try:
            comments = []
            task_data = Task.load_users()
            for user in task_data:
                if user["id"] == user_id:
                    for task in user["tasks"]:
                        if task["id"] == task_id:
                            comments = task.get("comments", [])
                            return comments  
            return comments  
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

        
    def add_comment(self, user_id, task_id, comment):
        data = Task.load_users()
        for user in data:
            if user["id"] == user_id:
                for task in user["tasks"]:
                    if task["id"] == task_id:
                        if "comments" in task:
                            task["comments"].append(comment)
                        else:
                            task["comments"] = [comment]
                        
                        with open('data.json', 'w') as file:
                            json.dump(data, file, indent=4)
                        return
                    
                    
    def delete_comment(self, user_id, task_id, comment):
            data = Task.load_users()
            for user in data:
                if user["id"] == user_id:
                    for task in user["tasks"]:
                        if task["id"] == task_id:
                            if "comments" in task:
                                if comment in task["comments"]:
                                    task["comments"].remove(comment)
                                    with open('data.json', 'w') as file:
                                        json.dump(data, file, indent=4)
                                    return True
                                else:
                                    print("Comment not found")
                                    return False  
                            else:
                                print("No comments for this task")
                                return False  
            print("User or task not found")
            return False  
