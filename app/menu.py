from datastruct import DataStruct
store = DataStruct()

class Menu:
    """This class does all the menu related stuff"""
    def __init__(self,menu_name="", description=""):
        self.menu_name = menu_name
        self.description = description

    def save_menu_item(self):
        if len(store.menu) >=1:
            self.menu_id = store.menu[-1]+1
        else:
            self.menu_id = 1
        menu = Menu()
        store.add_menu(menu)

    def fetch_menu_items(self):
        pass