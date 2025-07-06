from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/")
def Hello():
    return "Hello World"

users = {
    1: {"name":"Alice", "email":"alice@gmail.com"},
    2: {"name":"Wonderland","email":"inthewonderland@gmail.com" }
}

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users),200

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    new_id = max(users.keys()) + 1

    users[new_id] = {
        "name": data["name"],
        "email": data["email"]
    }

    return jsonify({"message":"User created", "id": new_id}),201

if __name__ == "__main__":
    app.run(debug=True)
