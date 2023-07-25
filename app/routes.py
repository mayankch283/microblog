from flask import render_template
from app import app

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


@app.route('/index/something')
def smth():
    return render_template('smth.html')
