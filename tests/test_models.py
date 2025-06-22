from models import MovieReview

def test_movie_review_model():
    review = MovieReview(
        movie_title="Inception",
        reviewer="Keerthi",
        rating=5,
        review="Mind-blowing!"
    )
    assert review.movie_title == "Inception"
    assert review.reviewer == "Keerthi"
    assert review.rating == 5
    assert review.review == "Mind-blowing!"
