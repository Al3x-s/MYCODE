import pytest
from app import app
import json
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_42(client, requests_mock):
    #client.post('/answer', json={"value": 42}) int value didnt work
    response = client.post("/answer", json={'value': '42'})
    assert response.data.decode('utf-8') == "yessir"


def test_43(client, requests_mock):
    response = client.post("/answer", json={'value': '43'})
    assert response.data.decode('utf-8') == "sike"
