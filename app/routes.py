from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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
	form = LoginForm()

	'''
	this function returns false when browser sends a GET request, renders the login page
	returns true  when browser send a POST request, redirects to /index
	When the browser sends the POST request as a result of the user pressing the submit button, form.validate_on_submit() is going to gather all the data, run all validators attached to fields 
	and ONLY IF EVERYTHING IS RIGHT, IT WILL RETURN TRUE : indicating that the data is valid and can be processed by the application. Even if one field fails validation, it will return False"
	'''
	if form.validate_on_submit():
        	#flash() : useful way to show a message to the user. Lets user know if some action has been useful or not.
        	#When you call the flash() function, Flask stores the message, but flashed messages will not magically appear in web pages.
        	#The templates of the application need to render these flashed messages in a way that works for the site layout.
		flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title = 'Sign In', form = form)
