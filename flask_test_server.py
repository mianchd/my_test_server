# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, url_for, request
import json
app = Flask(__name__)

@app.route('/success/<sucessful_user>')
def success_login(sucessful_user):
   # name is the variable in success_login.html
   return render_template('success_login.html', name = sucessful_user)

@app.route('/')
def main_page():
   # View -- Interacts with User
   return render_template('home_page.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   # Controller -- Communicates between Views such as main_page, success_login
   if request.method == 'POST':
      some_user = request.form['nm']
      return redirect(url_for('success_login', sucessful_user = some_user))

# A model is what interacts with a database with requests from controller
# Model notifies controller of changes, etc

global auth_code, company_id
auth_code = None
company_id = None

@app.route('/mysimpleapp/mysimplehandler', methods = ['POST', 'GET'])
def got_code():
#   raw_string = request.data
#   response_status = request.args.get('state')
    global auth_code, company_id
    auth_code = request.args.get('code')
    company_id = request.args.get('realmId')
    return "Got the response!<br />  Code: {}<br />  Company ID: {}".format(auth_code, company_id)

@app.route('/successful_authorisation/')
def return_data():
    global auth_code, company_id
    data = {'auth_code':auth_code, 'company_id':company_id}
    return json.dumps(data)


if __name__ == '__main__':
   app.run(debug = True, port=9000) #host='0.0.0.0' # Server accessable from computer's IP