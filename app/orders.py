from app.datastruct import DataStruct
from app.menu import Menu
store = DataStruct()


class Orders:
    """This class handles all orders, creation and storage"""
    def __init__(self,user_name="", menu_id="", status="", order_id=0):
        self.user_name= user_name
        self.status = "pending"
        self.menu_id = menu_id
        self.order_id = order_id
     

    def save_order(self):
        """This memthod appends orders to the Data structure"""
        if len(store.orders) >=1:
            self.order_id = store.orders[-1].order_id+1
        else:
            self.order_id = 1
        store.add_orders(Orders(
                  self.user_name, self.menu_id,
                  self.status,self.order_id,
                )
            )

    def covert_order_to_dict(self, order_obj):
        """This method coverts order object attributes into a diction
        used by view fuctions to generate a json array"""
        obj_data = {
            "menu_id": order_obj.menu_id,
            "order_id": order_obj.order_id,
            "status": order_obj.status,
            "user_name": order_obj.user_name
        }
        return obj_data
