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


