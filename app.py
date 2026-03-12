from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Sample in-memory data
students = [
    {"id": 1, "name": "Juan", "grade": 85, "section": "Zechariah"},
    {"id": 2, "name": "Maria", "grade": 90, "section": "Zechariah"},
    {"id": 3, "name": "Pedro", "grade": 70, "section": "Zion"}
]

# =========================
# HOME PAGE (redirect to student list)
# =========================
@app.route('/')
def home():
    return redirect(url_for('list_students'))

# =========================
# LIST STUDENTS
# =========================
@app.route('/students')
def list_students():
    html = """
    <h2>Student List</h2>
    <a href="/add_student">Add New Student</a><br><br>
    <ul>
    {% for s in students %}
        <li>
            ID: {{s.id}} - {{s.name}} (Grade: {{s.grade}}, Section: {{s.section}})
            [<a href="/edit_student/{{s.id}}">Edit</a>]
            [<a href="/delete_student/{{s.id}}" onclick="return confirm('Delete this student?');">Delete</a>]
        </li>
    {% endfor %}
    </ul>
    """
    return render_template_string(html, students=students)

# =========================
# ADD STUDENT
# =========================
@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        new_id = students[-1]['id'] + 1 if students else 1
        students.append({
            "id": new_id,
            "name": request.form["name"],
            "grade": int(request.form["grade"]),
            "section": request.form["section"]
        })
        return redirect(url_for('list_students'))

    html = """
    <h2>Add New Student</h2>
    <form method="POST">
        Name: <input type="text" name="name" required><br><br>
        Grade: <input type="number" name="grade" required><br><br>
        Section: <input type="text" name="section" required><br><br>
        <button type="submit">Add Student</button>
    </form>
    <br>
    <a href="/students">Back to List</a>
    """
    return render_template_string(html)

# =========================
# EDIT STUDENT
# =========================
@app.route('/edit_student/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = next((s for s in students if s["id"] == id), None)
    if not student:
        return "Student not found", 404

    if request.method == 'POST':
        student["name"] = request.form["name"]
        student["grade"] = int(request.form["grade"])
        student["section"] = request.form["section"]
        return redirect(url_for('list_students'))

    html = """
    <h2>Edit Student</h2>
    <form method="POST">
        Name: <input type="text" name="name" value="{{student.name}}" required><br><br>
        Grade: <input type="number" name="grade" value="{{student.grade}}" required><br><br>
        Section: <input type="text" name="section" value="{{student.section}}" required><br><br>
        <button type="submit">Update</button>
    </form>
    <br>
    <a href="/students">Back to List</a>
    """
    return render_template_string(html, student=student)

# =========================
# DELETE STUDENT
# =========================
@app.route('/delete_student/<int:id>')
def delete_student(id):
    global students
    students = [s for s in students if s["id"] != id]
    return redirect(url_for('list_students'))

# =========================
# RUN SERVER
# =========================
if __name__ == '__main__':
    app.run(debug=True)True)

