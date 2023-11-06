python
Copy
code
from flask import Flask, jsonify, request
import googlemaps
from datetime import datetime

app = Flask(__name__)

# Replace this with your actual Google API key
API_KEY = 'YOUR_GOOGLE_API_KEY'
gmaps = googlemaps.Client(key=API_KEY)


@app.route('/route_planning', methods=['GET'])
def route_planning ():
    origin = request.args.get('origin')  # Get the origin from the query string
    destination = request.args.get('destination')  # Get the destination from the query string

    # Check if the parameters are provided
    if not origin or not destination:
        return jsonify({"error": "Missing origin or destination parameters"}), 400

    try:
        # Call Google Maps Directions API
        directions_result = gmaps.directions(origin,
                                             destination,
                                             mode="walking",  # Scooters can use walking paths
                                             departure_time=datetime.now())
        return jsonify(directions_result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/surface_alerts', methods=['GET'])
def surface_alerts ():
    # This would be based on user-generated data, which we don't have access to in this example.
    # You would need a database to store and retrieve this information.
    return jsonify({"alerts": ["Rough surface on 5th Street", "Hole near 6th Street"]})


@app.route('/parking_spots', methods=['GET'])
def parking_spots ():
    location = request.args.get('location')

    if not location:
        return jsonify({"error": "Missing location parameter"}), 400

    try:
        # Call Google Places API for nearby parking
        parking_results = gmaps.places_nearby(location=location,
                                              keyword='parking',
                                              rank_by='distance')
        return jsonify(parking_results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/report_issue', methods=['POST'])
def report_issue ():
    # You'd store this in a database in a real app
    data = request.json
    print(f"Issue reported: {data}")
    # For now, just acknowledge the report
    return jsonify({"status": "success", "message": "Issue reported successfully"}), 200


@app.route('/emergency_alert', methods=['POST'])
def emergency_alert ():
    # In a real application, you'd send an email or SMS.
    data = request.json
    print(f"Emergency alert for user at {data['location']}")
    return jsonify({"status": "success", "message": "Emergency contact has been alerted"}), 200


if __name__ == '__main__':
    app.run(debug=True)
