from flask import Flask, request, jsonify, send_from_directory
import re
app = Flask(__name__)

def assess_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short. Minimum length should be 8 characters.")
    
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")
    
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")
    
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should include at least one number.")
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Password should include at least one special character.")
    
    if not re.search(r'(.)\1{2,}', password):
        score += 1
    else:
        feedback.append("Password should not have three consecutive identical characters.")
    
    common_patterns = ['123', 'abc', 'password', 'qwerty', 'admin']
    if not any(pattern in password.lower() for pattern in common_patterns):
        score += 1
    else:
        feedback.append("Password contains common patterns which are easy to guess.")

    if score == 6:
        strength = "Strong"
    elif 4 <= score < 6:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/styles.css')
def styles():
    return send_from_directory('', 'styles.css')

@app.route('/script.js')
def script():
    return send_from_directory('', 'script.js')

@app.route('/check-password', methods=['POST'])
def check_password():
    data = request.get_json()
    password = data.get('password')
    strength, feedback = assess_password_strength(password)
    return jsonify({"strength": strength, "feedback": feedback})

if __name__ == '__main__':
    app.run(debug=True)
