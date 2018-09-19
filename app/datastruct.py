
class DataStruct:
    menu = []
    users =[]
    orders = []
    """
    This class implements a data structure to store and retrieve
    users, userorders and menu istes
    """
    def __init__(self, user_name=""):
        self.user_name = user_name
      
        
    def add_menu_item(self, menu_item):
        """This method adds a menu item"""
        self.menu.append(menu_item)
        
    def add_user(self, user):
        """This method adds user"""
        self.users.append(user)

    def add_order(self, order):
        """This method appends an order to the order list"""
        for menu_item in self.menu:
            if menu_item["menu_id"] == order["menu_id"]:
                self.orders.append(order)
                return True
        return False
            

    def fetch_all_orders(self):
        """This method returns all orders for users"""
        if len(self.orders) >= 0:
            return self.orders
        return None

    
    def fetch_order(self, order_id):
        """This method fetches a specific order"""
        if self.orders:
            for order in self.orders:
                if order["order_id"] == order_id:
                    return order
            return None
        
    def update_order_status(self, status, order_id):
        for order in self.orders:
            if order["order_id"] == order_id:
                order["status"] == status
        return True

    