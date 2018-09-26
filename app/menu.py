from datastruct import DataStruct
store = DataStruct()

class Menu:
    """This class does all the menu related stuff"""
    def __init__(self,menu_name="", description="", menu_id =0):
        self.menu_name = menu_name
        self.description = description
        self.menu_id = menu_id

    def save_menu_item(self):
        if len(store.menu) >=1:
            self.menu_id = store.menu[-1].menu_id+1
        else:
            self.menu_id = 1
        store.add_menu(Menu(self.menu_name, self.description, self.menu_id))

    def fetch_menu_items(self):
        pass