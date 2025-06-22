import pytest
from app import app, db
from models import MovieReview

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_add_and_get_review(client):
    # Add a review
    res = client.post('/reviews', json={
        "movie_title": "Interstellar",
        "reviewer": "Keerthi",
        "rating": 5,
        "review": "Amazing!"
    })
    assert res.status_code == 201

    # Get all reviews
    res = client.get('/reviews')
    assert res.status_code == 200
    data = res.get_json()
    assert len(data) == 1
    assert data[0]['movie_title'] == "Interstellar"
