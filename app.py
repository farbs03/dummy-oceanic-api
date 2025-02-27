from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(
    app, origins=["http://localhost:3000"]
)

@app.route("/test-endpoint", methods=["POST"])
def testEndpoint():
    return jsonify("<p>Hi</p>")


if __name__ == "__main__":
    app.run(debug=True, port=5050)
