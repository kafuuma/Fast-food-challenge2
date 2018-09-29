
from app.datastruct import DataStruct
store = DataStruct()

class Users:
    """This class handles creation and storing users in a Datastructure"""

    def __init__(
                self,full_name="", password="",
                email="", contact="" ,user_role="",user_id =0,
        ):
        self.full_name = full_name
        self.password = password
        self.email = email
        self.contact = contact
        self.user_role = user_role 
        if len(store.users) >= 1:
            self.user_id = store.users[-1].user_id+1
        else:
            self.user_id = 1

    def save_user(self):
        """The mothode creates a user and appends to the Datastructure"""
        store.add_user(self)
    
    def login(self):
        pass

    def signup(self):
        pass