from flask import Flask, jsonify, request
from enum import Enum

app = Flask(__name__)

class City(Enum):
    NEW_YORK = "New York"
    WASHINGTON_DC = "Washington DC"
    SAN_FRANCISCO = "San Francisco"
    LOS_ANGELES = "Los Angeles"
    MIAMI = "Miami"
    CHICAGO = "Chicago"

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

@app.route('/get-carriers', methods=['GET'])
def get_carriers():
    from_city = request.args.get('from_city', '').strip()
    to_city = request.args.get('to_city', '').strip()

    try:
        from_city_enum = City(from_city)
        to_city_enum = City(to_city)
    except ValueError:
        return jsonify({"error": "One or both cities are not valid."}), 400

    route_key = create_route_key(from_city_enum, to_city_enum)
    carriers = mock_carriers.get(route_key, mock_carriers["default"])

    return jsonify(carriers)

if __name__ == '__main__':
    app.run(debug=True)
