from flask import Flask, jsonify, json, request
from data_struct import DataStruct
from menu import Menu
from users import Users
from orders import Orders

app = Flask(__name__)

@app.route("/api/v1/orders/",methods=["GET"])
def get_all_orders():
    """creates end point to fetch all food orders"""
    store = DataStruct()
    all_orders = store.fetch_all_orders()
    if all_orders:
        return jsonify({"response": all_orders}), 200
    return jsonify({"response":"Empty orders"})



@app.route("/api/v1/orders/<order_id>", methods=["GET"])
def fetch_order(order_id):
    """This route fetches a sigle order by id"""
    store = DataStruct()
    user_order = store.fetch_order(int(order_id))
    if user_order:
        return jsonify({"response":user_order}),200
    return jsonify({"response":"order doesn't exist"})
    

@app.route("/api/v1/orders", methods=["POST"])
def palce_order():
    store = DataStruct()
    user_order = request.get_json()
    menu_id = user_order.get("menu_id")
    user_name = user_order.get("user_name")
    Orders(user_name, menu_id)
    if len(store.orders)>0:
        return jsonify({"response":"success"}),200
    return jsonify({"response":"failure"})

    

@app.route("/api/v1/orders/<order_id>", methods=["PUT"])
def update_order_status(order_id):
    store = DataStruct()
    status = request.get_json()
    order_status = status.get("status")
    response = store.update_order_status(order_status, order_id)
    if response:
        return jsonify({"response": "success"}), 200
    return jsonify({"response":"no such order exists"})
    