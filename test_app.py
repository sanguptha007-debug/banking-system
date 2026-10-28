import pytest
from app import app, account

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_check_balance(client):
    account["balance"] = 100.0
    response = client.get('/balance')
    assert response.status_code == 200

def test_deposit_money(client):
    account["balance"] = 100.0
    response = client.post('/deposit', json={"amount": 50.0})
    assert response.status_code == 200

def test_withdraw_successful(client):
    account["balance"] = 100.0
    response = client.post('/withdraw', json={"amount": 40.0})
    assert response.status_code == 200
    assert response.get_json()['new_balance'] == 60.0

def test_withdraw_insufficient_funds(client):
    account["balance"] = 100.0
    response = client.post('/withdraw', json={"amount": 150.0})
    assert response.status_code == 400
    assert response.get_json()['error'] == "Insufficient funds"
