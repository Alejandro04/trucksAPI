import pytest
from flask import Flask
from app.app import app 

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_cities(client):
    response = client.get('/cities')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) > 0 
    expected_keys = {"name", "lat", "lng"}
    for city in data:
        assert expected_keys.issubset(city.keys())

def test_get_carriers_valid_route(client):
    response = client.get('/carriers', query_string={"from_city": "New York", "to_city": "Washington DC"})
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) > 0
    expected_keys = {"name", "trucks_per_day"}
    for carrier in data:
        assert expected_keys.issubset(carrier.keys())

def test_get_carriers_invalid_city(client):
    response = client.get('/carriers', query_string={"from_city": "InvalidCity", "to_city": "Washington DC"})
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "One or both cities are not valid."

def test_get_carriers_default_route(client):
    response = client.get('/carriers', query_string={"from_city": "San Francisco", "to_city": "Chicago"})
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) > 0 
    assert any(carrier["name"] == "UPS Inc." for carrier in data)

