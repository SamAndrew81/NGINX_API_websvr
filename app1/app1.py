from flask import Flask, request, render_template, jsonify
import json  # Import the json module

app1 = Flask(__name__)

# A simple in-memory store to hold incoming data
data_store = []

@app1.route('/')
def show_api():
    # Use the display.html template to display the "Demo SNOW placeholder - Display API test calls" message and the data
    # Format each item in data_store to pretty-printed JSON for better readability
    formatted_data_store = [json.dumps(item, indent=4) for item in data_store]
    # Pass the formatted JSON strings to the template
    return render_template('display.html', message='Demo SNOW placeholder - Display API test calls:', data=formatted_data_store)

# This route might be redundant if '/' route is already formatting and showing the data
@app1.route('/view-data')
def view_data():
    # Format each item in data_store to pretty-printed JSON
    formatted_data_store = [json.dumps(item, indent=4) for item in data_store]
    # Pass the formatted JSON strings to the template
    return render_template('display.html', message='Demo SNOW placeholder - Display API test calls:', data=formatted_data_store)

@app1.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json  # Assume the incoming data is JSON
    data_store.append(data)  # Store the data for display
    return jsonify({"status": "success", "message": "Data received"}), 200

@app1.route('/api/data', methods=['GET'])
def show_data():
    # Return the data_store as JSON, consider formatting for readability if consumed directly
    return jsonify(data_store)

@app1.route('/api/data/<identifier>', methods=['DELETE'])
def delete_data(identifier):
    global data_store  # Access the global data store
    # Filter out items that contain the identifier as a value for any key
    original_len = len(data_store)
    data_store = [item for item in data_store if identifier not in item.values()]
    if len(data_store) < original_len:
        return jsonify({"status": "success", "message": "Data deleted"}), 200
    else:
        return jsonify({"status": "error", "message": "No matching data found to delete"}), 404

if __name__ == '__main__':
    app1.run(debug=True, host='0.0.0.0')
