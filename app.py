from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Aplicación funcionando correctamente"})

@app.route("/suma/<int:a>/<int:b>")
def suma(a, b):
    return jsonify({"resultado": a + b})

if __name__ == "__main__":
    app.run(debug=True)
