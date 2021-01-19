from flask import Flask
from flask_cors import CORS
from flask import make_response
from flask import request
from flask import jsonify
from random_username.generate import generate_username
app = Flask(__name__)
CORS(app)
#FINISHED
@app.route('/')
def hello_world():
    return 'Hello World'
users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}
@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      if search_username and search_job:
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username and user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict
      if search_username :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd["id"] = generate_username(1)[0]
      users['users_list'].append(userToAdd)
      resp = make_response(jsonify(userToAdd), 201)
      return resp
   elif request.method == 'DELETE':
      user_id = request.args.get('id')
      if user_id:
         subdict = {'users_list': []}
         for user in users['users_list']:
            if user['id'] != user_id:
               subdict['users_list'].append(user)
         resp = make_response(jsonify(success=True), 204)
         return resp
      return users

@app.route('/users/<id>')
def get_user(id):
   if id :
      for user in users['users_list']:
        if user['id'] == id:
           return user
      return ({})
   return users
