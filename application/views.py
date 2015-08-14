from flask import render_template
import json
import os
from application import app

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

# ------------------------------------
# MVP pages
# ------------------------------------

@app.route('/profile')
def profile():
  with open('application/data/courses.json') as data_file:
    courses = json.load(data_file)
  return render_template('profile.html', courses=courses)

@app.route('/record')
def record():
  with open('application/data/courses.json') as data_file:
    courses = json.load(data_file)
  return render_template('record.html', courses=courses)

@app.route('/search')
def mvp_search():
  return render_template('course_search_mvp.html')

# ------------------------------------
# Future pages
# ------------------------------------
@app.route('/future/search')
def future_search():
  return render_template('course_search.html')

# ------------------------------------
# Styleguide pages
# ------------------------------------
@app.route('/styleguide')
def styleguide():
  return render_template('styleguide.html')

@app.route('/styleguide/forms')
def sg_forms():
  return render_template('styleguide/forms.html')

@app.route('/styleguide/search')
def sg_search():
  return render_template('styleguide/search.html')
