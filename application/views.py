from flask import render_template
from application import app

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/profile')
def profile():
  return render_template('profile.html')
