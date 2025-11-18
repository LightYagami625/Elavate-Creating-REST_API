# Flask User REST API
## Simple CRUD operation 

Simple REST API built with Python and Flask to manage users stored in a JSON file (`user-data.json`).  
You can create, read, update, and delete users using `curl` commands.

---

## Features

- Get all users
- Create a new user
- Update an existing user
- Delete a user
- Data persisted in a local JSON file (`user-data.json`)

---

## Project Structure

```bash
.
├── flassk-rest-api.py   # Main Flask app
└── user-data.json       # User data storage (JSON)
```

---

## Installing Dependencies
Copy and Paste the following into your venv or the conda env
```
pip install flask
```
If cURL is not install, else ignore
```
    sudo apt install curl
```

---

## Guide to operate using cURL
1. GET - View all users data
```
curl -X GET http://localhost:5000/users
```

2. POST - Create or add new user data
```
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Uzumaki Naruto",
    "email": "naruto.106@example.com"
  }'

```
3. PUT - Update existing user data
Enter the user id or index at the end of url before updating
```
curl -X PUT http://localhost:5000/users/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice Updated"
  }'
```
4. DELETE - Remove or delete existing user data
Enter user id or index at the end of url before 
```
curl -X DELETE http://localhost:5000/users/3
```
 
 ---

 # BELIEVE IT!
