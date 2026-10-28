from flask import Flask, jsonify, request

app = Flask(__name__)
account = {"balance": 100.0}

@app.route('/balance', methods=['GET'])
def check_balance():
    return jsonify({"balance": account["balance"]}), 200

@app.route('/deposit', methods=['POST'])
def deposit_money():
    data = request.get_json()
    if not data or 'amount' not in data:
        return jsonify({"error": "Invalid request parameters"}), 400
    
    amount = float(data['amount'])
    if amount <= 0:
        return jsonify({"error": "Deposit amount must be positive"}), 400
        
    account["balance"] += amount
    return jsonify({"message": "Deposit successful", "new_balance": account["balance"]}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
