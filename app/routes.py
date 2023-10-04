from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user

@app.route('/')
@app.route('/index')
def index():
    '''mock objects'''
    user = {'username': 'Mayank'} 
    posts = [
            {
                'author': {'username' : 'John'},
                'body': 'Beautiful day in Portland'
            },
            {
                'author': {'username': 'Susan'},
                'body': 'The Oppenheimer movie was so good!'

            }
            ]

    return render_template('index.html', title='Home', user=user, posts=posts)

'''
methods arg tells Flask that this view func accepts GET and POST requests(overriding the default, which is to accept only GET requests.)
The HTTP protocol states that GET requests are those that return information to the client(web browser in this case). POST requests are used when browser submits form data to the server
By providing methods argument, we tell Flask which request method should be accepted. '''

'''

'''
@app.route('/login', methods=['GET', 'POST']) 
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()

	'''
	this function returns false when browser sends a GET request, renders the login page
	returns true  when browser send a POST request, redirects to /index
	When the browser sends the POST request as a result of the user pressing the submit button, form.validate_on_submit() is going to gather all the data, run all validators attached to fields 
	and ONLY IF EVERYTHING IS RIGHT, IT WILL RETURN TRUE : indicating that the data is valid and can be processed by the application. Even if one field fails validation, it will return False"
	'''
	if form.validate_on_submit():
			user = User.query.filter_by(username=form.username.data).first()
			if user is None or not user.check_password(form.password.data):
				flash('Invalid username or password')
				return redirect(url_for('login'))
			login_user(user, remember=form.remember_me.data)
			return redirect(url_for('index'))
	return render_template('login.html', title = 'Sign In', form = form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))