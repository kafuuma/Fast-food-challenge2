
from data_struct import DataStruct
store = DataStruct()

class Users:
    """This class handles users, manipulation stuff"""

    def __init__(self, full_name, password, email="", contact="" ,user_role=""):
        self.name = full_name
        self.password = password
        self.email = email
        self.contact = contact
        self.user_role = user_role 

    def save_user(self):
        if len(store.users) >= 1:
            self.id = store.users[-1]["user_id"]+1
        else:
            self.id = 1
        self.user = {
                "user_id": self.id,
                "name": self.name,
                "password": self.password,
                "email": self.email,
                "contact": self.contact,
                "user_role": "user"
            }
        store.add_user(self.user)
    
    def validate_user(self):
        pass