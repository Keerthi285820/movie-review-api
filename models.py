from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MovieReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(100), nullable=False)
    reviewer = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review = db.Column(db.Text, nullable=False)
