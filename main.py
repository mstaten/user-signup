### 03/30/19 ###

from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('signup_form.html', title='Signup')


def is_username_valid(username):
    if len(username) < 3 or len(username) > 20:
        return 'invalid length'
    elif ' ' in username:
        return 'no whitespace in username'
    else:
        return ''
        

def is_password_valid(password):
    if len(password) < 3 or len(password) > 20:
        return 'invalid length'
    elif ' ' in password:
        return 'no whitespace in password'
    else:
        return ''
        

def do_passwords_match(password, verify_password):

    # if empty or lengths don't match
    if not verify_password or len(password) != len(verify_password):
        return 'passwords don\'t match'
    
    # if password invalid
    elif is_password_valid(password):
        # want verify_password to give same error warning as password
        return is_password_valid(password)

    elif ' ' in verify_password:
        return 'no whitespace in password'

    for i in range(len(password)):
        if password[i] != verify_password[i]:
            return 'passwords don\'t match'
    return ''


def is_email_valid(email):
    if not email:   # if empty
        return ''
    elif len(email) < 3 or len(email) > 20:
        return 'invalid length'
    elif ' ' in email:
        return 'no whitespace in email'
    elif email.count('@')!=1 or email.count('.')!=1:
        return "must contain one '@' and one '.'"
    else:
        return ''


@app.route("/", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    # test input for validity, set error equal to the results
    username_error = is_username_valid(username)
    password_error = is_password_valid(password)
    verify_password_error = do_passwords_match(password, verify_password)
    email_error = is_email_valid(email)

    # if any errors at all, must re-render form with 
    # appropriate errors and clear passwords
    if username_error or password_error or verify_password_error or email_error:
        return render_template('signup_form.html', title="Signup", username_error=username_error, password_error=password_error, verify_password_error=verify_password_error, email_error=email_error, password='', verify_password='')
    else:
        return redirect('/welcome?username={0}'.format(username))
    
@app.route('/welcome', methods=['GET','POST'])
def welcome():
    if request.method == 'POST':
        username = request.form['username']
    else:
        username = request.args.get('username')
    return render_template('welcome.html', name=username, title="Welcome!")

app.run()