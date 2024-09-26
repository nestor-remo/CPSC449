from flask import Flask, request, jsonify

app = Flask(__name__)

global name
name = "Nestor"

@app.route("/", methods=["GET"])
def hello():
    return f"Hello, {name}!"


@app.route("/json", methods=["POST"])
def user():
    data = request.get_json()
    if len(data) < 5:
        return jsonify({"error": "Enter at least 5 fields of data"}), 400
    return jsonify(data), 200

@app.route("/mixed", methods=["GET", "POST"])
def combined():
    if request.method == "GET":
        return "This is a GET request"
    elif request.method == "POST":
        data = request.get_json()
        return jsonify(data), 200

if __name__ == "__main__":
    app.run(debug=True)

