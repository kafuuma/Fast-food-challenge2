
class DataStruct:
    """
    This class implements the data structure with 3 lists to store dictionary items 
    """
    menu  =   []
    orders =  []
    users =   []
    
    def add_orders(self, order):
        for menu_item in self.menu:
            if menu_item.menu_id == order.menu_id:
                self.orders.append(order)
                return True
        return False

    def add_menu(self, menu):
        self.menu.append(menu)

    def add_user(self, user):
        self.users.append(user)

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


    def fetch_all_orders(self):
        all_orders = []
        if len(self.orders) >=1:
            for order in self.orders:
                order_data = self.covert_order_to_dict(order)
                all_orders.append(order_data)
            return all_orders
        return None
        

    def fetch_order(self, id):
        for order in self.orders:
            if order.order_id == id:
                return [self.covert_order_to_dict(order)]
        return None
    
    def update_order_status(self, status, id):
        index = 0
        for order in self.orders:
            if order.order_id == id:
                self.orders[index].status = status
                return [self.covert_order_to_dict(self.orders[index])]
            index = index+1
        return None

    def empty_data(self):
        self.menu[:] = []
        self.orders[:] = []
        self.orders[:] =[]
