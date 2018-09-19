
import unittest
import json
from run import app
from app.datastruct import DataStruct
from app.menu import Menu
from app.users import Users
from app.orders import Orders


class TestFastFood(unittest.TestCase):
    
    def setUp(self):
        self.app = app
        self.test_client = self.app.test_client()
        # self.app_context = app.app_context()
        # self.app_context.push()
        self.store = DataStruct()
        self.menu = Menu()
        self.user = Users()
        self.order = Orders()
        
        #create 3 menu items
        
        self.menu1 = Menu("Hot Burgar", "served with juice & ketchup").save_menu_item()
        self.user1 = Users("henry henry","@hhenry","myemail@gmail.com","555 555 555","user").save_user()
        
    def tearDown(self):
        self.store = DataStruct()
        self.store.menu[:] = []
        self.store.orders[:] = []
        self.store.orders[:] =[]

    def test_user_object_creation(self):
        self.assertIsInstance(self.user, Users)
       

    def test_menu_object_creation(self):
        self.assertIsInstance(self.menu, Menu)

    def test_order_object_creation(self):
        self.assertIsInstance(self.order, Orders)
    
    def test_place_an_order(self):
        response = self.test_client.post(
                "/api/v1/users/orders",
                content_type="application/json",
                data=json.dumps(
                    {
                        "user_name":"henry henry",
                        "menu_id":1
                    }
                )
        )
        self.test_client.post(
                "/api/v1/users/orders",
                content_type="application/json",
                data=json.dumps(
                    {
                        "user_name":"henry henry",
                        "menu_id":1
                    }
                )
        )
        self.assertEqual(response.status_code, 200)

        self.assertEqual(json.loads(response.data.decode()),{"response":"success"})
        self.assertEqual(len(self.store.orders),2)
        
    def test_place_noexisting_menu_order(self):
        response = self.test_client.post(
            "/api/v1/users/orders",
            content_type="application/json",
            data=json.dumps(
                {
                    "user_name":"henry henry",
                    "menu_id":0
                }
            )
        )
        self.assertEqual(response.status_code,400)
        self.assertEqual(len(self.store.orders),0)
        self.assertEqual(json.loads(response.data.decode()),{"reponse":"failure"})

    def test_fetch_all_orders(self):
        self.test_client.post(
                "/api/v1/users/orders",
                content_type="application/json",
                data=json.dumps(
                    {
                        "user_name":"henry henry",
                        "menu_id":1
                    }
                )
        )
        self.test_client.post(
                "/api/v1/users/orders",
                content_type="application/json",
                data=json.dumps(
                    {
                        "user_name":"henry henry",
                        "menu_id":1
                    }
                )
        )

        response = self.test_client.get(
                "/api/v1/users/orders",

        )

        self.assertEqual(response.status_code,200)
        self.assertIn({
                "menu_id": 1,
                "order_id": 1, 
                "status":"pending",
                "user_name":"henry henry"
            },  
            json.loads(response.data.decode())["response"]
        )


    def test_etch_non_existing_orders(self):
        response = self.test_client.get(
            "/api/v1/users/orders",

        )
        self.assertEqual(json.loads(response.data.decode()),{"response":"Empty orders"})
        self.assertEqual(response.status_code,400)

    # def test_fetch_order_byId(self):
    #      self.test_client.post(
    #             "/api/v1/users/orders",
    #             content_type="application/json",
    #             data=json.dumps(
    #                 {
    #                     "user_name":"henry henry",
    #                     "menu_id":1
    #                 }
    #             )
    #      )
    #      response = self.test_client.get(
    #                 "/api/v1/users/orders/2"
    #             )

    #      self.assertEqual(response.status_code,200)
    #      self.assertIn(
    #          json.loads(response.data.decode()),
    #                 {"response":[
    #                     {
    #                         "menu_id": 1,
    #                         "order_id": 1, 
    #                         "status":"pending",
    #                         "user_name":"henry henry"
    #                     }
    #                 ]
                
    #             })

    
            




      
  

     
if __name__ == '__main__':
    unittest.main()

