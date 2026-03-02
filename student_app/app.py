from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aamir@123",
    database="student_db"
)
cursor = db.cursor(dictionary=True)

# ======================
# Normal Web App Routes
# ======================

@app.route("/")
def home():
    return redirect(url_for("students"))

@app.route("/students")
def students():
    cursor.execute("SELECT id, name, course FROM students")
    data = cursor.fetchall()
    return render_template("index.html", students=data)

@app.route("/add", methods=["POST"])
def add_student():
    name = request.form["name"]
    course = request.form["course"]

    cursor.execute(
        "INSERT INTO students (name, course) VALUES (%s, %s)",
        (name, course)
    )
    db.commit()
    return redirect(url_for("students"))

@app.route("/delete/<int:id>")
def delete_student(id):
    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    db.commit()
    return redirect(url_for("students"))

@app.route("/edit/<int:id>", methods=["POST"])  # edit.html nahi hai, isliye direct POST
def edit_student(id):
    name = request.form["name"]
    course = request.form["course"]

    cursor.execute(
        "UPDATE students SET name=%s, course=%s WHERE id=%s",
        (name, course, id)
    )
    db.commit()
    return redirect(url_for("students"))

# ======================
# REST API Routes (New)
# ======================

@app.route("/api/students", methods=["GET"])
def api_get_students():
    cursor.execute("SELECT id, name, course FROM students")
    data = cursor.fetchall()
    return jsonify(data)

@app.route("/api/students", methods=["POST"])
def api_add_student():
    data = request.get_json()
    name = data.get("name")
    course = data.get("course")

    cursor.execute(
        "INSERT INTO students (name, course) VALUES (%s, %s)",
        (name, course)
    )
    db.commit()

    return jsonify({"message": "Student added"}), 201

@app.route("/api/students/<int:id>", methods=["PUT"])
def api_update_student(id):
    data = request.get_json()
    name = data.get("name")
    course = data.get("course")

    cursor.execute(
        "UPDATE students SET name=%s, course=%s WHERE id=%s",
        (name, course, id)
    )
    db.commit()

    return jsonify({"message": "Student updated"})

@app.route("/api/students/<int:id>", methods=["DELETE"])
def api_delete_student(id):
    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    db.commit()
    return jsonify({"message": "Student deleted"})

if __name__ == "__main__":
    app.run(debug=True)
    
