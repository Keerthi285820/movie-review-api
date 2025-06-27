from flask import Flask, request, jsonify
from models import db, MovieReview
from flasgger import Swagger

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

swagger = Swagger(app)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/reviews', methods=['POST'])
def add_review():
    """
    Add a new movie review
    ---
    tags:
      - Reviews
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - movie_title
              - reviewer
              - rating
              - review
            properties:
              movie_title:
                type: string
              reviewer:
                type: string
              rating:
                type: number
              review:
                type: string
    responses:
      201:
        description: Review added successfully
    """
    data = request.get_json()
    new_review = MovieReview(**data)
    db.session.add(new_review)
    db.session.commit()
    return jsonify({"message": "Review added!"}), 201

@app.route('/reviews', methods=['GET'])
def get_reviews():
    """
    Get all movie reviews
    ---
    tags:
      - Reviews
    responses:
      200:
        description: A list of movie reviews
    """
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
    """
    Get a review by ID
    ---
    tags:
      - Reviews
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: Review ID
    responses:
      200:
        description: A single movie review
      404:
        description: Review not found
    """
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
    """
    Update a review by ID
    ---
    tags:
      - Reviews
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: Review ID
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              movie_title:
                type: string
              reviewer:
                type: string
              rating:
                type: number
              review:
                type: string
    responses:
      200:
        description: Review updated successfully
      404:
        description: Review not found
    """
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
    """
    Delete a review by ID
    ---
    tags:
      - Reviews
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: Review ID
    responses:
      200:
        description: Review deleted successfully
      404:
        description: Review not found
    """
    r = MovieReview.query.get_or_404(id)
    db.session.delete(r)
    db.session.commit()
    return jsonify({"message": "Review deleted!"})

if __name__ == '__main__':
    app.run(debug=True)
