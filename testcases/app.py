from flask import Flask, request

app = Flask(__name__)

@app.route('/answer', methods=['POST'])
def checkval():
    data = request.json
    correct = "42"

    answer = data.get("value")

    if answer == '42':
        return("yessir")
    else:
        return("sike")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=2225)
