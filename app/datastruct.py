
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

    def get_orders(self):
        if len(self.orders) >=1:
            return self.orders
        return None

    def get_order(self, id):
        for order in self.orders:
            if order.order_id == id:
                return order
        return None
    
    def modify_order_staus(self, status, id):
        index = 0
        for order in self.orders:
            if order.order_id == id:
                self.orders[index].status = status
                return self.orders[index]
            index = index+1
        return None



    def empty_data(self):
        self.menu[:] = []
        self.orders[:] = []
        self.orders[:] =[]
