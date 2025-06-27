from flask import Flask, request, jsonify
from flasgger import Swagger
from models import db, MovieReview

app = Flask(__name__)

# ✅ Swagger config
app.config['SWAGGER'] = {
    'title': 'Movie Review API',
    'uiversion': 3
}

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Movie Review API",
        "description": "API documentation for managing movie reviews.",
        "version": "1.0"
    },
    "basePath": "/",
    "schemes": ["http"],
}
swagger = Swagger(app, template=swagger_template)

# ✅ Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    return "🎬 Movie Review API is running!"

@app.route('/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    new_review = MovieReview(**data)
    db.session.add(new_review)
    db.session.commit()
    return jsonify({"message": "Review added!"}), 201

@app.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = MovieReview.query.all()
    return jsonify([{
        "id": r.id,
        "movie_title": r.movie_title,
        "reviewer": r.reviewer,
        "rating": r.rating,
        "review": r.review
    } for r in reviews])

@app.route('/reviews/<int:id>', methods=['GET'])
def get_review(id):
    r = MovieReview.query.get_or_404(id)
    return jsonify({
        "id": r.id,
        "movie_title": r.movie_title,
        "reviewer": r.reviewer,
        "rating": r.rating,
        "review": r.review
    })

@app.route('/reviews/<int:id>', methods=['PUT'])
def update_review(id):
    r = MovieReview.query.get_or_404(id)
    data = request.get_json()
    r.movie_title = data.get("movie_title", r.movie_title)
    r.reviewer = data.get("reviewer", r.reviewer)
    r.rating = data.get("rating", r.rating)
    r.review = data.get("review", r.review)
    db.session.commit()
    return jsonify({"message": "Review updated!"})

@app.route('/reviews/<int:id>', methods=['DELETE'])
def delete_review(id):
    r = MovieReview.query.get_or_404(id)
    db.session.delete(r)
    db.session.commit()
    return jsonify({"message": "Review deleted!"})

if __name__ == '__main__':
    app.run(debug=True)
