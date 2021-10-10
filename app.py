from flask import Flask
from json import dumps
from flask import request
from flask import Response

app = Flask(__name__)

users = {
    "admin": "root",
}

def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/')
def root_test():
    return 'index'

@app.route('/secret')
def secret_page():
    return Response("Hello", 201, mimetype='application/json')

@app.route('/user', methods=['GET'])
def get_users():
	return dumps(users)

@app.route('/user/<string:username>', methods=['GET'])
def get_profile(username):
	return username + " profile"

@app.route('/user/add/<string:username>/pwd/<string:password>', methods=['POST'])
def add_user(username, password):
	users[username] = password
	return Response("User added" , status=200, mimetype='application/json')

@app.route('/user/<string:username>/pwd/<string:password>', methods=['GET'])
def authenticate_user(username, password):
	resp = Response("Pasword changed" , status=200, mimetype='application/json')
	if not username in users.keys():
		resp = Response("User " + username + " not found!" , status=403, mimetype='application/json')
	elif users[username] == password:
		resp = Response("Authentication Successful!!", 201, mimetype='application/json')
	else:
		resp = Response("Authentication Failed!!", 405, mimetype='application/json')
	return resp

@app.route('/user/<string:username>/pwd/<string:password>', methods=['POST'])
def change_password(username, password):
	resp = Response("Pasword changed" , status=200, mimetype='application/json')
	if not username in users.keys():
		resp = Response("User " + username + " not found!" , status=403, mimetype='application/json')
	else:
		users[username] = password
	return resp

if __name__ == '__main__':
    app.run()
