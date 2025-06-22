import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_reviews_route(client):
    response = client.get('/reviews')
    assert response.status_code == 200
