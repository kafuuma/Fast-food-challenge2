from datastruct import DataStruct
from menu import Menu
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

    # def fetch_all_orders(self):
    #     """This method fetches all orders"""
    #     if len(store.orders) >= 0:
    #         return store.orders
    #     return None
    
    # def fetch_order(self, order_id):
    #     """This method fetches a specific order"""
    #     if store.orders:
    #         for order in store.orders:
    #             if order["order_id"] == order_id:
    #                 return [order]
    #         return None
    
    # def update_order_status(self, status, order_id):
    #     """This method updates a status of an existing orderc"""
    #     count = 0
    #     for order in store.orders:
    #         if order["order_id"] == order_id:
    #             store.orders[count]["status"] = status
    #             return [store.orders[count]]
    #         count = count+1
    #     return None   
