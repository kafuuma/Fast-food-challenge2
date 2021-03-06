
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
        self.app_context = app.app_context()
        self.app_context.push()

        self.store = DataStruct()
        self.menu = Menu()
        self.user = Users()
        self.order = Orders()
        
        Menu("Hot Burgar", "served with juice & ketchup").save_menu_item()
        Users("henry henry","@hhenry","myemail@gmail.com","555 555 555","user").save_user()
        
    def tearDown(self):
        self.store = DataStruct()
        self.store.empty_data()
        
    def post_data(self):
        """This method posts test data to datastructure object"""
        response = self.test_client.post(
                    "/api/v1/orders",
                    content_type="application/json",
                    data=json.dumps(
                        {
                            "user_name":"henry henry",
                            "menu_id":1
                        }
                    )
                )
        return response

    def test_user_object_creation(self):
        self.assertIsInstance(self.user, Users)
       
    def test_menu_object_creation(self):
        self.assertIsInstance(self.menu, Menu)

    def test_order_object_creation(self):
        self.assertIsInstance(self.order, Orders)
    
    def test_place_an_order(self):
        self.post_data()
        response = self.post_data()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data.decode()),{"response":"success"})
        self.assertEqual(len(self.store.orders),2)

    def test_fetch_all_orders(self):
        self.post_data()
        response = self.test_client.get(
                "/api/v1/orders",

        )
        self.assertEqual(response.status_code,201)
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
            "/api/v1/orders",

        )
        self.assertEqual(json.loads(response.data.decode()),{"response":"Empty orders"})
        self.assertEqual(response.status_code,400)

    def test_fetch_order_byId(self):
         self.post_data()
         response = self.test_client.get(
                    "/api/v1/orders/1"
                )
         self.assertEqual(response.status_code,201)
         self.assertEqual(
             json.loads(response.data.decode()),
                    {"response":[
                        {
                            "menu_id": 1,
                            "order_id": 1, 
                            "status":"pending",
                            "user_name":"henry henry"
                        }
                    ]
                
                })
    
    def test_fetch_non_existing_order_ByID(self):
        response = self.test_client.get(
                    "/api/v1/orders/1"
                )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data.decode()),{"response":"order doesn't exist"})

    def test_update_order_status(self):
        self.post_data()
        response = self.test_client.put(
                    "/api/v1/orders/1",
                    content_type="application/json",
                    data=json.dumps(
                        {
                            "status":"delivered",
                            
                        }
                )
            )
        self.assertEqual(response.status_code,201)
        self.assertEqual(
             json.loads(response.data.decode()),
                    {"response":[
                        {
                            "menu_id": 1,
                            "order_id": 1, 
                            "status":"delivered",
                            "user_name":"henry henry"
                        }
                    ]
                
                })
        
    def test_update_nonexisting_order_status(self):
        response = self.test_client.put(
                    "/api/v1/orders/3",
                    content_type="application/json",
                    data=json.dumps(
                        {
                            "status":"delivered",
                            
                        }
                )
            )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data.decode()),{"response":"no such order exists"})
            
     
if __name__ == '__main__':
    unittest.main()

