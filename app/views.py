from flask import Flask, jsonify, json, request
from datastruct import DataStruct
from menu import Menu
from users import Users
from orders import Orders

app = Flask(__name__)

@app.route("/api/v1/users/orders", methods=["GET"])
def get_all_orders():
    """creates end point to fetch all food orders"""
    store = DataStruct()
    all_orders = store.fetch_all_orders()
    if len(all_orders)>=1:
        return jsonify({"response": all_orders}), 200
    return jsonify({"response":"Empty orders"}),400



@app.route("/api/v1/users/orders/<order_id>", methods=["GET"])
def fetch_order(order_id):
    """This route fetches a sigle order by id"""
    store = DataStruct()
    user_order = store.fetch_order(int(order_id))
    if user_order:
        return jsonify({"response":user_order}),200
    return jsonify({"response":"order doesn't exist"}),400
    

@app.route("/api/v1/users/orders", methods=["POST"])
def palce_order():
    store = DataStruct()
    user_order = request.get_json()
    user_name = user_order.get("user_name")
    menu_id = user_order.get("menu_id")
    Orders(user_name, menu_id).save_order()
    if len(store.orders)>0:
        return jsonify({"response":"success"}),200
    return jsonify({"reponse":"failure"}),400




@app.route("/api/v1/users/orders/<int:order_id>", methods=["PUT"])
def update_order_status(order_id):
    store = DataStruct()
    status = request.get_json()
    order_status = status.get("status")
    response = store.update_order_status(order_status, order_id)
    if response:
        return jsonify({"response": response}), 200
    return jsonify({"response":"no such order exists"}),400


    