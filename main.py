### 03/30/19 ###

from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('signup_form.html')

@app.route("/", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    if not username:
        username_error = 'must enter valid username'
    if not password:
        password_error = 'must enter valid password'
    if not verify_password:
        verify_password_error = 'passwords don\'t match'
    if not email:
        email_error = 'must enter email'

    if not username_error and not password_error and not verify_password_error and not email_error:
        # all errors are empty; there are no errors; welcome
        return redirect('/welcome?username={0}&password={1}&verify_password={2}&email={3}'.format(' ', ' ', ' ', ' '))
    else:
        return render_template('signup_form.html', username_error=username_error, password_error=password_error, verify_password_error=verify_password_error, email_error=email_error)

@app.route('/welcome', methods=['GET','POST'])
def welcome():
    return render_template('welcome.html', title="Welcome!")

app.run()