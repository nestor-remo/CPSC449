from flask import Flask

app = Flask(__name__)

global name
name = "Nestor"

@app.route("/", methods=["GET"])
def hello():
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)