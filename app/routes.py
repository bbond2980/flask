from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Ben'}
	posts = [
		{
			'author': {'username': 'Ben'},
			'body': 'First!'
		},
		{
			'author': {'username': 'John'},
			'body': 'Beautiful day in Detroit!'
		},
		{
			'author': {'username': 'Susan'},
			'body': 'The Avengers movie was so cool!'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)
