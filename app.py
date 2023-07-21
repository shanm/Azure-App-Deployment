from flask import Flask, request, jsonify, make_response
from datetime import datetime, timedelta
from flask_cors import CORS, decorator

app = Flask(__name__)

#print(app.config)

@app.route("/home")
def home():
	return "Flask API get endpoint running"

if __name__ == "__main__":
	app.run(debug=True)