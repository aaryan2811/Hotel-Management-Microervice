from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/check_rooms', methods=['POST'])
def check_rooms():
    reservations = request.json
    if not reservations:
        return jsonify({"error": "No data provided or invalid JSON format"}), 400

    today = datetime.date.today().isoformat()
    result = {"checked-in": [], "checked-out": []}

    for reservation in reservations:
        if not all(key in reservation for key in ["checkOutDate", "roomNumber", "checkedIn"]):
            return jsonify({"error": "Invalid reservation format"}), 400

        if reservation.get("checkOutDate") == today:
            room_number = reservation.get("roomNumber")
            if reservation.get("checkedIn"):
                result["checked-in"].append(room_number)
            else:
                result["checked-out"].append(room_number)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
