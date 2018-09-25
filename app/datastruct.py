
class DataStruct:
    """
    This class implements the data structure with 3 liststo store dictionary items 
    """
    menu  =   []
    orders =  []
    users =   []
    
    def add_orders(self, order):
        self.orders.append(order)
            

    def add_menu(self, menu):
        self.menu.append(menu)

    def add_user(self, user_id, full_name, password, email, contact, user_role):
        user = {
                "user_id": user_id,
                "name": full_name,
                "password": password,
                "email": email,
                "contact": contact,
                "user_role": user_role
            }
        self.users.append(user)

    def empty_data(self):
        self.menu[:] = []
        self.orders[:] = []
        self.orders[:] =[]
