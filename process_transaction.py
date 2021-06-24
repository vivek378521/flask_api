#processing the transaction data
import json


def calculate_delivery_cost(distance):
    with open("delivery_pricing.json") as f:
        data = f.read()
    json_pricing_data = json.loads(data)
    for price in json_pricing_data["delivery_cost"]:
        if price["from"] < distance <= price["to"]:
            return int(price["price"])*100  # converting rupee to paisa


def calculate_discount(offer, delivery):
    if offer["offer"]["offer_type"] == "FLAT":  # checking the kind of offer applied
        return offer["offer"]["offer_val"]
    elif offer["offer"]["offer_type"] == "DELIVERY":
        return delivery


def get_total_amount(json_data):
    order_data = json_data["order_items"]
    order_total = 0
    discount = 0
    for order in order_data:
        order_total += order["quantity"] * order["price"]  # adding all the prices
    delivery_charges = calculate_delivery_cost(json_data["distance"]/1000)  # converting meter to kilometer
    order_total += delivery_charges
    if "offer" in json_data:
        discount = calculate_discount(json_data, delivery_charges)
    if discount > order_total:
        return "Invalid Discount Applied"
    return order_total - discount



#calculate_delivery_cost(100)