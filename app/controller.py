# Importing flask library
from app import app
from flask import Flask, redirect, make_response, render_template, url_for, session, request, escape, flash
import os
app.secret_key = os.environ.get('SECRET_KEY') or 'hard to guess string'

@app.route('/')
@app.route('/index')
def index():
    print session
    #check if the user is already in session, if so, direct the user to survey.html
    if 'usr' in session: 
        username = session['usr']
        resp = render_template('survey.html', name=username)
    else:
        resp = render_template('login.html')
    return resp

@app.route('/login', methods=['POST']) # You need to specify something here for the function to get requests
def login():
    # Here, you need to have logic like if there's a post request method, 
    # store the username and email from the form into session dictionary
    if(request.method =='POST'):
        session['usr'] = request.form['usr']
        session['eml'] = request.form['eml']
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
	session.pop('usr', None)
	session.pop('eml', None)
	return redirect(url_for('index'))

@app.route('/submit-survey', methods=['GET', 'POST'])
def submitSurvey():
    email = ''
    if'usr' in session: #check if user in session
        username = session['usr']

        surveyResponse = {}
        surveyResponse['color'] = request.form.get('color')
        surveyResponse['food'] = request.form.get('food')
        surveyResponse['vacation'] = request.form.get('vacation')
        surveyResponse['fe-before'] = request.form.get('feBefore')
        surveyResponse['fe-after'] = request.form.get('feAfter')
        if surveyResponse['fe-after'] > surveyResponse['fe-before']:
            surveyResponse['msg'] = 'Great job!'
        else:
            surveyResponse['msg'] = "Keep trying at it. You'll get there"
        resp = render_template('results.html', name=username, surveyResponse=surveyResponse)
    else:
        resp = render_template('login.html')
        # return redirect(url_for('login')) why doesn't this equally work??
        # why can't we use redirect(url_for('route')) the same way we do make_response(render_template('route.html'))
        # what is the difference between make_response(render_template()) and just render_template()
    return resp 


@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404
