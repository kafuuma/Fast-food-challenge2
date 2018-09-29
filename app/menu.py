from app.datastruct import DataStruct
store = DataStruct()

class Menu:
    """This class does all the menu related stuff"""
    def __init__(self,menu_name="", description="", menu_id =0):
        self.menu_name = menu_name
        self.description = description
        if len(store.menu) >=1:
            self.menu_id = store.menu[-1].menu_id+1
        else:
            self.menu_id = 1

    def save_menu_item(self):
        store.add_menu(self)

    def fetch_menu_items(self):
        pass