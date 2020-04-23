from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(ok=True, description="Deployed :D", status_code=200)

if __name__ == '__main__':
    app.run()