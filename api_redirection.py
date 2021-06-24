from flask import Flask, jsonify, request
import process_transaction as process

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/transaction/add', methods=['POST'])
def api_transaction_add():
    if request.is_json:  # check if the request is json or not
        posted_data = request.get_json()
        order_total = process.get_total_amount(posted_data)  # processing the request
    else:
        return "Invalid Json Body", 400

    return jsonify("{order_total: " + str(order_total) + "}")


@app.errorhandler(404)
def not_found(e):
    return "Unexpected error" + str(e), 404

app.run()
