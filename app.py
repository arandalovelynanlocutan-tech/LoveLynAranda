from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample student data (temporary storage)
student = {
    "name": "Your Name",
    "grade": 10,
    "section": "Zechariah"
}

# Home Route
@app.route('/')
def home():
    return "Welcome to my Flask API!"

# GET Student
@app.route('/student', methods=['GET'])
def get_student():
    return jsonify(student)

# UPDATE / MODIFY Student
@app.route('/student', methods=['PUT'])
def update_student():
    data = request.json

    if 'name' in data:
        student['name'] = data['name']

    if 'grade' in data:
        student['grade'] = data['grade']

    if 'section' in data:
        student['section'] = data['section']

    return jsonify({
        "message": "Student updated successfully",
        "student": student
    })

if __name__ == '__main__':
    app.run(debug=True)
