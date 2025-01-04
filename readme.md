# Carriers Service API

The Carriers Service API is a lightweight Flask-based backend that provides transport company details based on the specified origin and destination cities. It includes predefined routes and carriers for common routes and defaults to general carriers for other routes.

## Features
City-based Routing: Provides transporters for specific city pairs.
Default Routing: Returns general transporters for any unspecified routes.
Enum Validation: Ensures valid city names through an enumeration.

## Endpoints
GET /get-carriers
Returns a list of transporters for a given origin and destination city.

## Query Parameters:

from_city (string): Name of the origin city (e.g., "New York").
to_city (string): Name of the destination city (e.g., "Washington DC").
Response:

Success (200): A JSON array containing the transporters and their daily truck capacity.
Error (400): If one or both city names are invalid.
Example Request:

## bash
curl -X GET "http://localhost:5000/get-carriers?from_city=New%20York&to_city=Washington%20DC"

## Example Response:

json
[
  {"name": "Knight-Swift Transport Services", "trucks_per_day": 10},
  {"name": "J.B. Hunt Transport Services Inc", "trucks_per_day": 7},
  {"name": "YRC Worldwide", "trucks_per_day": 5}
]

## Mocked Data
The service includes the following predefined data:

Routes and Transporters
New York to Washington DC:

Knight-Swift Transport Services: 10 trucks/day
J.B. Hunt Transport Services Inc: 7 trucks/day
YRC Worldwide: 5 trucks/day
San Francisco to Los Angeles:

XPO Logistics: 9 trucks/day
Schneider: 6 trucks/day
Landstar Systems: 2 trucks/day
Default Route (Other Cities):

UPS Inc.: 11 trucks/day
FedEx Corp: 9 trucks/day

## Database model
![image](https://github.com/user-attachments/assets/176b5cc9-bfc7-40ed-9b20-49ba86ce1b83)
