import pytest
from app.app import app, City

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_carriers_valid_route(client):
    # Test for a known route (New York to Washington DC)
    response = client.get('/get-carriers?from_city=New York&to_city=Washington DC')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 3
    assert data[0]['name'] == 'Knight-Swift Transport Services'
    assert data[0]['trucks_per_day'] == 10

def test_get_carriers_default_route(client):
    # Test for a route that uses default carriers (Miami to Chicago)
    response = client.get('/get-carriers?from_city=Miami&to_city=Chicago')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2
    assert data[0]['name'] == 'UPS Inc.'
    assert data[0]['trucks_per_day'] == 11

def test_get_carriers_invalid_cities(client):
    # Test with invalid city names
    response = client.get('/get-carriers?from_city=Invalid&to_city=City')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'One or both cities are not valid.' 