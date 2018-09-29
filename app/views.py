from flask import Flask, jsonify, json, request
from app.datastruct import DataStruct
from app.menu import Menu
from app.users import Users
from app.orders import Orders

app = Flask(__name__)

@app.route("/api/v1/orders", methods=["GET"])
def get_all_orders():
    """creates end point to fetch all food orders"""
    store_data = DataStruct()
    all_orders = store_data.fetch_all_orders()
    if all_orders:
        return jsonify({"response": all_orders}), 201
    return jsonify({"response":"Empty orders"}),400
    



@app.route("/api/v1/orders/<order_id>", methods=["GET"])
def fetch_order(order_id):
    """This route fetches a sigle order by id"""
    store_data = DataStruct()
    user_order = store_data.fetch_order(int(order_id))
    if user_order:
        return jsonify({"response":user_order}),201
    return jsonify({"response":"order doesn't exist"}),404

@app.route("/api/v1/orders", methods=["POST"])
def palce_order():
    store_data = DataStruct()
    user_order = request.get_json()
    if user_order:
        user_name = user_order.get("user_name")
        menu_id = user_order.get("menu_id")
        Menu("chicken pizza", "delicious").save_menu_item()
        Orders(user_name, menu_id).save_order()
        if store_data.orders:
            return jsonify({"response":"success"}),200
        return jsonify({"reponse":"failure"}),400
    return jsonify({"response":"no data supplied"}),404




@app.route("/api/v1/orders/<int:order_id>", methods=["PUT"])
def update_order_status(order_id):
    store_data = DataStruct()
    status = request.get_json()
    if status:
        order_status = status.get("status")
        response = store_data.update_order_status(order_status, order_id)
        if response:
            return jsonify({"response": response}), 201
        return jsonify({"response":"no such order exists"}),404
    return jsonify({"response":"please supply status"})

    