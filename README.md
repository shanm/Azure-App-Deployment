# Azure-App-Service

# Steps to be followed to set-up on development environment

git clone https://github.com/shanm/Azure-App-Deployment.git # Clone the repository

cd /Azure/Azure-App-Deployment # change directory

py -m venv .venv # create virtual environment; if you're using Linux, `python3 -m venv .venv`

env/Scripts/activate # activate virtual environment, if you're using Linux, source env/bin/activate

pip install -r requirements.txt # install dependencies

flask run

You can test that all the endpoints are working by testing the app in an API testing tool with http://127.0.0.1:5000/, like Postman.
