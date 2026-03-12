from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# Sample data (temporary list for demo)
students = [
    {"id": 1, "name": "Juan", "grade": 85, "section": "Stallman"},
    {"id": 2, "name": "Maria", "grade": 90, "section": "Stallman"},
]

# =========================
# HOME PAGE
# =========================
@app.route('/')
def home():
    return "Welcome to the Student API! Go to /add_student_form to add a student."

# =========================
# FORM PAGE
# =========================
@app.route('/add_student_form')
def add_student_form():

    html = """
    <h2>Add New Student</h2>

    <form action="/add_student" method="POST">
        Name: <input type="text" name="name" autofocus><br><br>
        Grade: <input type="number" name="grade"><br><br>
        Section: <input type="text" name="section"><br><br>
        <input type="submit" value="Add Student">
    </form>

    <br>
    <a href="/students">View Students</a>
    """

    return render_template_string(html)

# =========================
# ADD STUDENT
# =========================
@app.route('/add_student', methods=['POST'])
def add_student():

    name = request.form.get("name")
    grade = request.form.get("grade")
    section = request.form.get("section")

    if not name or not grade or not section:
        return jsonify({"error": "Missing student information"}), 400

    new_id = len(students) + 1

    new_student = {
        "id": new_id,
        "name": name,
        "grade": int(grade),
        "section": section
    }

    students.append(new_student)

    return jsonify({
        "message": "Student added successfully!",
        "student": new_student
    })

# =========================
# VIEW ALL STUDENTS
# =========================
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# =========================
# RUN SERVER
# =========================
if __name__ == '__main__':
    app.run(debug=True)
