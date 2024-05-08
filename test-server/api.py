from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=['GET'])
def test_endpoint():
    response = {
        "field1": "val1",
        "field2": 42,
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
