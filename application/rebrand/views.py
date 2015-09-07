from flask import (
  Blueprint,
  render_template,
)
import json


blueprint = Blueprint(
  'rebrand',
  __name__,
  static_folder='static',
  template_folder='templates')

# ------------------------------------
# Rebrand pages
# ------------------------------------
@blueprint.route('/')
@blueprint.route('/signin')
def signin():
  return render_template('signin.html')

@blueprint.route('/home')
def home():
  return render_template('home.html')

@blueprint.route('/user')
def user():
  return render_template('user.html')

@blueprint.route('/course-e-learning')
def course_e_learning():
  return render_template('course-e-learning.html')

@blueprint.route('/professions')
def professions():
  return render_template('professions.html')

@blueprint.route('/guide-priority-learning')
def priorities():
  return render_template('priority-learning.html')

@blueprint.route('/commercial')
def commercial():
  with open('application/data/commercial.json') as data_file:
    courses = json.load( data_file )
  return render_template('commercial.html', courses=courses)