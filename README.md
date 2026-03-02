# Student Management System (Flask + MySQL + API)

A simple Student Management web app built using:
- Python (Flask)
- MySQL Database
- HTML & CSS
- REST API (GET, POST, DELETE)

## Features
- Add new student
- View all students
- Delete student by ID
- Data stored in MySQL
- API endpoints to fetch students

## Tech Stack
- Flask
- MySQL
- HTML, CSS

## How to Run
1. Install requirements:
   pip install -r requirements.txt

2. Create database and table using `schema.sql`

3. Run the app:
   python app.py

4. Open browser:
   http://127.0.0.1:5000

## API Endpoints
- GET /api/students
- POST /api/students
- DELETE /api/students/<id>
