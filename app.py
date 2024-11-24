from flask import Flask, jsonify, request
import random
import string

app = Flask(__name__)

# Helper function to generate the password
def generate_password(length, include_uppercase, include_numbers, include_special):
    # Define possible characters
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Base characters that will always be included
    characters = lower_chars
    if include_uppercase:
        characters += upper_chars
    if include_numbers:
        characters += digits
    if include_special:
        characters += special_chars

    # Randomly generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Route to generate the password
@app.route('/generate-password', methods=['POST'])
def generate():
    data = request.get_json()
    length = data.get('length', 12)
    include_uppercase = data.get('include_uppercase', False)
    include_numbers = data.get('include_numbers', False)
    include_special = data.get('include_special', False)

    password = generate_password(length, include_uppercase, include_numbers, include_special)
    return jsonify({"password": password})

if __name__ == '__main__':
    app.run(debug=True)
