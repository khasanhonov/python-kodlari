import json


def load(file_name):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        with open(file_name, "w") as file:
            json.dump([], file)
        return []

def save(file_name, lst):
    with open(file_name, "w") as file:
        return json.dump(lst, file, indent=4)
        



class User:
    file_name = "users.json"

    def __init__(self, username, password, role="user"):
        self.username = username
        self.password = password
        self.role = role

    
    # CRUD
    @staticmethod
    def create(username, password):
        users = load(User.file_name)
        for user in users:
            if user ['username'] == username:
                print("Bunday foydalanuvchi bazada bor")
                return
        users.append( {"username": username, "password": password, "role": "user"})
        save(User.file_name, users)
    
    @staticmethod
    def read():
        return loasd(User.file_name)
        

    @staticmethod
    def update(username, password):
        for user in users:
            if username == user['username']:
                user['password'] = password 

                return
        print("Bunday user topilmadi")
        users.append( {"password": password, "role": "user"})
        save(User.password, users)
    
    @staticmethod
    def delete(username):
        for i, user in enumerate(users):
            if username == user['username']:
                print(i)
                # users.remove(user)
                del users[i]
        print("Bunday user topilmadi")
        
        if users ['username'] == username:
            del file_name
        else:
            del file
                return


User.create("Anvar","123")
User.create("Jasur","123")
User.create("Otabek","123")

# User.update("Anvar", "1")
# User.delete("Anvar")
# print(User.read())

# User.file_name

class Menu(User):
    
    def __init__(self, username, password, role="user")


