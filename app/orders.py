from data_struct import DataStruct
from menu import Menu
store = DataStruct()

class Orders:
    """This class handles all order stuff"""
    def __init__(self,user_name, menu_id, status=None):
        self.user_name= user_name
        self.status = "pending"
        self.menu_id = menu_id

    def save_order(self):
        
        if len(store.orders) >=1:
            self.order_id = store.orders[-1]["menu_id"]+1
        else:
            self.order_id = 1

        self.order = {
            "order_id": self.order_id,
            "menu_id": self.menu_id,
            "user_name": self.user_name,
            "status":  self.status,
        }

        store.add_order(self.order)
    