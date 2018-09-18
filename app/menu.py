from data_struct import DataStruct
store = DataStruct()

class Menu:
    """This class does all the menu related stuff"""
    def __init__(self,menu_name, description):
        self.menu_name = menu_name
        self.description = description

    def save_menu_item(self):
        if len(store.menu) >=1:
            self.menu_id = store.menu[-1]["menu_id"]+1
        else:
            self.menu_id = 1

        self.menu_item = {
            "menu_id": self.menu_id,
            "menu_name": self.menu_name,
            "description": self.description
        }

        store.add_menu_item(self.menu_item)