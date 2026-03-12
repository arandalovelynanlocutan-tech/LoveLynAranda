from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary database (list)
students = [
    {
        "id": 1,
        "name": "Ana Cruz",
        "grade": 10,
        "section": "Zechariah"
    }
]

# Home Route
@app.route('/')
def home():
    return "Student API is running"

# ==============================
# GET ALL STUDENTS
# ==============================
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# ==============================
# GET STUDENT BY ID
# ==============================
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):

    for student in students:
        if student['id'] == id:
            return jsonify(student)

    return jsonify({"error": "Student not found"}), 404

# ==============================
# ADD STUDENT
# ==============================
@app.route('/students', methods=['POST'])
def add_student():

    data = request.json

    if not data.get('name') or not data.get('grade') or not data.get('section'):
        return jsonify({"error": "Missing data"}), 400

    new_student = {
        "id": students[-1]['id'] + 1 if students else 1,
        "name": data['name'],
        "grade": data['grade'],
        "section": data['section']
    }

    students.append(new_student)

    return jsonify({
        "message": "Student added successfully",
        "student": new_student
    })

# ==============================
# UPDATE STUDENT
# ==============================
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):

    data = request.json

    for student in students:

        if student['id'] == id:

            student['name'] = data.get('name', student['name'])
            student['grade'] = data.get('grade', student['grade'])
            student['section'] = data.get('section', student['section'])

            return jsonify({
                "message": "Student updated successfully",
                "student": student
            })

    return jsonify({"error": "Student not found"}), 404


# ==============================
# DELETE STUDENT
# ==============================
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):

    for student in students:

        if student['id'] == id:
            students.remove(student)

            return jsonify({
                "message": "Student deleted successfully"
            })

    return jsonify({"error": "Student not found"}), 404


# ==============================
# SEARCH STUDENT
# ==============================
@app.route('/students/search', methods=['GET'])
def search_student():

    name = request.args.get('name')

    result = [s for s in students if name.lower() in s['name'].lower()]

    return jsonify(result)


# ==============================
# API STATUS
# ==============================
@app.route('/status')
def status():
    return jsonify({"status": "API running"})


# RUN SERVER
if __name__ == '__main__':
    app.run(debug=True)
