# 🎬 Keploy Movie Review API

This project demonstrates a simple Flask-based REST API for managing movie reviews. It showcases how to use **Keploy** to automatically record, generate, and replay test cases from real API traffic. It also includes integration with **GitHub Actions CI/CD** pipeline.

---

## 📁 Project Structure

movie-review-api/
├── app.py # Flask application
├── models.py # SQLAlchemy database model
├── docs/
│ └── openapi.yaml # OpenAPI schema for Keploy
├── requirements.txt # Dependencies
├── .github/
│ └── workflows/
│ └── keploy-ci.yml # GitHub Actions CI workflow
└── README.md # You're here!

yaml
Copy
Edit

---

## 📌 Features

✅ REST API built with Flask  
✅ SQLAlchemy for database  
✅ Swagger documentation using Flasgger  
✅ OpenAPI 2.0 spec in YAML format  
✅ Keploy-based test recording & testing  
✅ GitHub Actions CI/CD integration  

---

## 🧪 API Endpoints

| Method | Endpoint          | Description              |
|--------|-------------------|--------------------------|
| GET    | `/reviews`        | Get all movie reviews    |
| POST   | `/reviews`        | Add a new movie review   |
| GET    | `/reviews/<id>`   | Get review by ID         |
| PUT    | `/reviews/<id>`   | Update a review by ID    |
| DELETE | `/reviews/<id>`   | Delete a review by ID    |

### 🔸 Sample POST `/reviews` Request:

```json
{
  "movie_title": "Inception",
  "reviewer": "Keerthi",
  "rating": 5,
  "review": "Amazing!"
}
📖 OpenAPI Schema
The openapi.yaml file located in the docs/ directory defines your API in Swagger format. It is used by Keploy to auto-generate test cases and simulate API traffic.

Use https://editor.swagger.io to visualize or edit it.

⚙ Running Keploy Tests
✅ Record API Traffic
bash
Copy
Edit
keploy.exe record --proxy
→ While Keploy proxy is running, make API calls using Postman, browser, or curl.
→ All traffic is captured automatically into testcases.

🔁 Test Replay
bash
Copy
Edit
keploy.exe test --command "python app.py"
→ Keploy replays previously recorded tests and validates actual vs expected responses.

🔁 CI/CD Integration
The .github/workflows/keploy-ci.yml workflow automates:

✅ Python setup

✅ Dependency installation

✅ Keploy test execution

🛠 Workflow File: keploy-ci.yml
yaml
Copy
Edit
name: Keploy CI

on:
  push:
    branches:
      - main

jobs:
  keploy-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.11'

      - name: Install Dependencies
        run: pip install -r requirements.txt

      - name: Download Keploy
        run: |
          wget https://github.com/keploy/keploy/releases/download/v0.1.6/keploy_linux_amd64.tar.gz
          tar -xvzf keploy_linux_amd64.tar.gz
          chmod +x keploy

      - name: Run Keploy Tests
        run: ./keploy test --command "python app.py"
✍ Author
👩‍💻 Keerthi Sri
Passionate about developing reliable APIs and exploring API testing automation using Keploy.

