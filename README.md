# 🎬 Movie Review API

A simple RESTful API built with **Flask** and a frontend using **Streamlit**, allowing users to create, view, update, and delete movie reviews. The application uses **SQLite** for local data storage and supports API testing via **Postman**.

---

## 🚀 Features

- ✅ Add a new movie review (POST)
- 📃 View all movie reviews (GET)
- ✏️ Update a review by ID (PUT)
- 🗑️ Delete a review by ID (DELETE)
- 🌐 Streamlit interface for easy interaction
- 🔌 Postman support for full API testing

---

## 🛠️ Tech Stack

| Layer     | Technology         |
|-----------|--------------------|
| Backend   | Python, Flask      |
| Database  | SQLite, SQLAlchemy |
| Frontend  | Streamlit          |
| Testing   | Postman            |

---

## 📁 Project Structure

movie-review-api/
├── app.py # Flask backend with API routes
├── models.py # SQLAlchemy model for MovieReview
├── database.db # SQLite DB (auto-created)
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── frontend/
└── streamlit_app.py # Streamlit user interface

yaml
Copy
Edit

---

## 📦 Setup Instructions

### 🔧 1. Clone the Repository
```bash
git clone https://github.com/your-username/movie-review-api.git
cd movie-review-api
💽 2. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
▶️ 3. Run Flask Backend
bash
Copy
Edit
python app.py
Your server will start at:

cpp
Copy
Edit
http://127.0.0.1:5000/
🧪 API Testing with Postman
✅ Add Review – POST
Method: POST

URL: http://127.0.0.1:5000/reviews

Body (raw JSON):

json
Copy
Edit
{
  "movie_title": "Inception",
  "reviewer": "Keerthi",
  "rating": 4.7,
  "review": "Mind-blowing!"
}
📃 Get All Reviews – GET
Method: GET

URL: http://127.0.0.1:5000/reviews

✏️ Update Review – PUT
Method: PUT

URL: http://127.0.0.1:5000/reviews/1

Body (raw JSON):

json
Copy
Edit
{
  "movie_title": "Inception (Updated)",
  "reviewer": "Keerthi Sri",
  "rating": 5,
  "review": "Updated review content"
}
❌ Delete Review – DELETE
Method: DELETE

URL: http://127.0.0.1:5000/reviews/1

🎨 Optional: Streamlit Frontend
▶️ Run the Streamlit UI
bash
Copy
Edit
streamlit run frontend/streamlit_app.py
It connects with the Flask backend to:

Submit new reviews

View existing ones

Update/delete interactively

📌 Author
Keerthi Sri S
Department of Artificial Intelligence and Data Science
Built with ❤️ using Python and Flask

