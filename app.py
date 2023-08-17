from flask import Flask, request, jsonify, make_response
from datetime import datetime, timedelta
from flask_cors import CORS, decorator

app = Flask(__name__)

#print(app.config)

@app.route("/api")
def home():
	return "Flask API get endpoint running"

@app.route("/api/getUsers")
def getUsers():
	return jsonify({"first_name":"shanmuga", "last_name":"raja", "email":"shanmugaraj.kumar@gmail.com"})

if __name__ == "__main__":
	app.run(debug=True)
