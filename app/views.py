from flask import Flask, jsonify, json, request
from datastruct import DataStruct
from menu import Menu
from users import Users
from orders import Orders

app = Flask(__name__)

@app.route("/api/v1/orders", methods=["GET"])
def get_all_orders():
    """creates end point to fetch all food orders"""
    order_obj = Orders()
    all_orders = order_obj.fetch_all_orders()
    if len(all_orders)>=1:
        return jsonify({"response": all_orders}), 201
    return jsonify({"response":"Empty orders"}),400
    



@app.route("/api/v1/orders/<order_id>", methods=["GET"])
def fetch_order(order_id):
    """This route fetches a sigle order by id"""
    order_obj = Orders()
    user_order = order_obj.fetch_order(int(order_id))
    if user_order:
        return jsonify({"response":user_order}),201
    return jsonify({"response":"order doesn't exist"}),404
    

@app.route("/api/v1/orders", methods=["POST"])
def palce_order():
    store = DataStruct()
    user_order = request.get_json()
    if user_order:
        user_name = user_order.get("user_name")
        menu_id = user_order.get("menu_id")
        Menu("Hot Burgar", "served with juice & ketchup").save_menu_item()
        Orders(user_name, menu_id).save_order()
        if len(store.orders):
            return jsonify({"response":"success"}),200
        return jsonify({"reponse":"failure"}),400
    return jsonify({"response":"no data supplied"}),404




@app.route("/api/v1/orders/<int:order_id>", methods=["PUT"])
def update_order_status(order_id):
    order_obj = Orders()
    status = request.get_json()
    if status:
        order_status = status.get("status")
        response = order_obj.update_order_status(order_status, order_id)
        if response:
            return jsonify({"response": response}), 201
        return jsonify({"response":"no such order exists"}),404
    return jsonify({"response":"please supply status"})

    