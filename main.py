from flask import Flask, request, jsonify
import random
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Dummy Scan API Server", "endpoints": ["/scan"]})

@app.route('/scan', methods=['POST'])
def scan():
    try:
        # Get JSON data from request
        data = request.get_json(force=True)

        # Generate a random risk score between 1-100
        risk_score = round(random.uniform(1.0, 100.0), 2)

        return jsonify({
            "risk_score": risk_score
        })

    except Exception as e:
        return jsonify({
            "error": str(e),
            "message": "Failed to process request"
        }), 400

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
