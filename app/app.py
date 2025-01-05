from flask import Flask, jsonify, request
from flask_cors import CORS
from enum import Enum

app = Flask(__name__)
CORS(app)

class City(Enum):
    NEW_YORK = {"name": "New York", "lat": 40.7128, "lng": -74.0060}
    WASHINGTON_DC = {"name": "Washington DC", "lat": 38.9072, "lng": -77.0369}
    SAN_FRANCISCO = {"name": "San Francisco", "lat": 37.7749, "lng": -122.4194}
    LOS_ANGELES = {"name": "Los Angeles", "lat": 34.0522, "lng": -118.2437}
    CHICAGO = {"name": "Chicago", "lat": 41.8781, "lng": -87.6298}

def create_route_key(from_city: City, to_city: City) -> str:
    return f"{from_city.name}-{to_city.name}"

mock_carriers = {
    create_route_key(City.NEW_YORK, City.WASHINGTON_DC): [
        {"name": "Knight-Swift Transport Services", "trucks_per_day": 10},
        {"name": "J.B. Hunt Transport Services Inc", "trucks_per_day": 7},
        {"name": "YRC Worldwide", "trucks_per_day": 5},
    ],
    create_route_key(City.SAN_FRANCISCO, City.LOS_ANGELES): [
        {"name": "XPO Logistics", "trucks_per_day": 9},
        {"name": "Schneider", "trucks_per_day": 6},
        {"name": "Landstar Systems", "trucks_per_day": 2},
    ],
    "default": [
        {"name": "UPS Inc.", "trucks_per_day": 11},
        {"name": "FedEx Corp", "trucks_per_day": 9},
    ],
}

@app.route('/carriers', methods=['GET'])
def get_carriers():
    from_city = request.args.get('from_city', '').strip()
    to_city = request.args.get('to_city', '').strip()

    try:
        from_city_enum_name = from_city.upper().replace(' ', '_')
        to_city_enum_name = to_city.upper().replace(' ', '_')
        
        from_city_enum = City[from_city_enum_name]
        to_city_enum = City[to_city_enum_name]

    except (KeyError, ValueError):
        return jsonify({"error": "One or both cities are not valid."}), 400

    route_key = create_route_key(from_city_enum, to_city_enum)
    carriers = mock_carriers.get(route_key, mock_carriers["default"])

    return jsonify(carriers)

@app.route('/cities', methods=['GET'])
def get_cities():
    return jsonify([city.value for city in City])

if __name__ == '__main__':
    app.run(debug=True)
