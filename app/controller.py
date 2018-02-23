# Importing flask library
from app import app
from flask import Flask, redirect, make_response, render_template, url_for, session, request, escape, flash
import os
app.secret_key = os.environ.get('SECRET_KEY') or 'hard to guess string'

@app.route('/')
@app.route('/index')
def index():
    print session
    if 'usr' in session: #check if the user is already in session, if so, direct the user to survey.html Hint: render_template with a variable
        username = session['usr']
        resp = make_response(render_template('survey.html', name=username))
        # resp.
        return resp
    else:
        return render_template('login.html')

@app.route('/login', methods=['POST']) # You need to specify something here for the function to get requests
def login():
    # Here, you need to have logic like if there's a post request method, store the username and email from the form into
    # session dictionary
    if(request.method=='POST'):
        session['usr'] = request.form['usr']
        session['eml'] = request.form['eml']
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
	session.pop('username', None)
	session.pop('email', None)
	return redirect(url_for('index'))

@app.route('/submit-survey', methods=['GET', 'POST'])
def submitSurvey():
    username = ''
    email = ''
    if(): #check if user in session
        username = session.get('username')
        surveyResponse = {}
        #get the rest o responses from users using request library Hint: ~3 lines of code
        surveyResponse['fe-before'] = request.form.get('feBefore')
        surveyResponse['fe-after'] = request.form.get('feAfter')
        return render_template('results.html') # pass in variables to the template
    else:
        return render_template('login.html')

@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404
