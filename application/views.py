from flask import render_template
import json
import os
from application import app

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/profile')
def profile():
  with open('application/data/courses.json') as data_file:
    courses = json.load(data_file)
  return render_template('profile.html', courses=courses)
