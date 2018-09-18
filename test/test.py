
import unittest
import json
from run import app
from app.datastruct import DataStruct
from app.menu import Menu
from app.users import Users


class TestFastFood(unittest.TestCase):
    
    def setUp(self):
        from run import app
        self.app = app
        self.test_client = self.app.test_client()
        self.store = DataStruct()
        
        #create 3 menu items
        
        self.menu1 = Menu("Hot Burgar", "served with juice & ketchup").save_menu_item()
        self.menu2 = Menu("Big Pizza", "Buy one get one free").save_menu_item()
        self.menu3 = Menu("Steamed Chicken", "2 pieces & 500ml soda").save_menu_item()
        #create a user
        self.user1 = Users("henry henry","@hhenry","myemail@gmail.com","555 555 555","user").save_user()


    def tearDown(self):
        pass

    def test_menu_object_creation(self):
        self.menu = Menu()
        self.assertIsInstance(self.menu, Menu)
        self.assertEqual(len(self.store.menu),3)

    def test_user_object_creation(self):
        self.user1 = Users()
        self.assertIsInstance(self.user1, Users)
        self.assertEqual(len(self.store.users),1)
        
    

if __name__ == '__main__':
    unittest.main()

