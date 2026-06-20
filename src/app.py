from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    # Instead of just a print(), this serves a functional API endpoint
    return jsonify({"status": "healthy", "message": "CI/CD Lab Running Successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
