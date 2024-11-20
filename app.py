from flask import Flask, request, jsonify
from datetime import date

app = Flask(__name__)

@app.route('/check_rooms', methods=['POST'])
def check_rooms():
    # Get the JSON data from the request
    reservations = request.json
    
    # Get today's date in the same format as the input data
    today = date.today().isoformat()
    
    # Initialize the result dictionary
    result = {
        "checked-in": [],
        "checked-out": []
    }
    
    # Process each reservation
    for reservation in reservations:
        if reservation.get("checkOutDate") == today:
            room_number = reservation.get("roomNumber")
            if reservation.get("checkedIn"):  # True -> checked-in
                result["checked-in"].append(room_number)
            else:  # False -> checked-out
                result["checked-out"].append(room_number)
    
    # Return the result as JSON
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port = 5001)
