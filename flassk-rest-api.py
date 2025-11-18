from flask import Flask, jsonify, request
import os
import json

app = Flask(__name__)

# path to user-data.json located next to this script
DATA = os.path.join(os.path.dirname(__file__), "user-data.json")


def find_user(user_id, users_list):
    
    return next((user for user in users_list if user.get("id") == user_id), None)

def load_users():
    if not os.path.exists(DATA):
        return []  # Return empty list if file doesn't exist
    try:
        with open(DATA, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return [] # Return empty list if file is empty/corrupt

# Helper: Save users to the JSON file
def save_users(users_list):
    # always write using utf-8 and keep JSON readable
    with open(DATA, 'w', encoding='utf-8') as f:
        json.dump(users_list, f, indent=4, ensure_ascii=False)

### GET
@app.route('/users', methods=['GET'])
def get_users():
    users = load_users()
    return jsonify({
        "count": len(users),
        "users": users
    }), 200

### POST
@app.route('/users', methods=['POST'])
def create_user():
    users = load_users()
    
    data = request.get_json()


    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Bad Request: 'name' and 'email' are required"}), 400


    new_id = max([u['id'] for u in users]) + 1 if users else 1
    
    new_user = {
        "id": new_id,
        "name": data['name'],
        "email": data['email']
    }
    
    users.append(new_user)
    save_users(users)
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    users = load_users()
    user = find_user(user_id, users)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json() or {}

    # Update fields if they exist in the request
    user['name'] = data.get('name', user.get('name'))
    user['email'] = data.get('email', user.get('email'))

    # Persist changes
    save_users(users)

    return jsonify(user), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    users = load_users()
    user = find_user(user_id, users)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # remove and persist
    users = [u for u in users if u.get('id') != user_id]
    save_users(users)

    return jsonify({"message": f"User {user_id} deleted successfully"}), 200

if __name__ == '__main__':

    app.run(debug=True, port=5000)