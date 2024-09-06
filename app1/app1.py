from flask import Flask, request, render_template, jsonify
import json

app1 = Flask(__name__)

# A simple in-memory store to hold incoming data
data_store = []

@app1.route('/')
def show_api():
    formatted_data_store = [json.dumps(item, indent=4) for item in data_store]
    return render_template('display.html', message='Demo "ticket" placeholder - Display API test calls:', data=formatted_data_store)

@app1.route('/view-data')
def view_data():
    formatted_data_store = [json.dumps(item, indent=4) for item in data_store]
    return render_template('display.html', message='Demo "ticket" placeholder - Display API test calls:', data=formatted_data_store)

@app1.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json
    data_store.append(data)
    return jsonify({"status": "success", "message": "Data received"}), 200

@app1.route('/api/data', methods=['GET'])
def show_data():
    return jsonify(data_store)

@app1.route('/api/data/<identifier>', methods=['DELETE'])
def delete_data(identifier):
    global data_store
    original_len = len(data_store)
    data_store = [item for item in data_store if identifier not in item.values()]
    if len(data_store) < original_len:
        return jsonify({"status": "success", "message": "Data deleted"}), 200
    else:
        return jsonify({"status": "error", "message": "No matching data found to delete"}), 404

@app1.route('/reset', methods=['POST'])
def reset():
    global data_store
    data_store = []
    return jsonify({"status": "success", "message": "Data store cleared"}), 200

if __name__ == '__main__':
    app1.run(debug=True, host='0.0.0.0')
