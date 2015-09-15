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

@blueprint.route('/how-use-competency-framework')
def guide_competency_framework():
  return render_template('guides/competency-framework.html')

# ------------------------------------
# Rebrand course pages
# ------------------------------------
@blueprint.route('/course/digital-by-default')
def course_d_by_d():
  return render_template('courses/digital-by-default.html')

@blueprint.route('/course/unconscious-bias')
def course_unconscious_bias():
  with open('application/data/courses/unconscious_bias.json') as data_file:
    course = json.load( data_file )
  return render_template('course_layout.html', course=course)

@blueprint.route('/course/neuroscience-of-leadership')
def course_neuroscience_leadership():
  with open('application/data/courses/neuroscience_of_leadership.json') as data_file:
    course = json.load( data_file )
  return render_template('course_layout.html', course=course)

@blueprint.route('/course/communicating-with-customers')
def course_communicating_with_customers():
  with open('application/data/courses/communicating_with_customers.json') as data_file:
    course = json.load( data_file )
  return render_template('course_layout.html', course=course)

@blueprint.route('/course/constructive-conversations')
def course_constructive_conversations():
  with open('application/data/courses/constructive_conversations.json') as data_file:
    course = json.load( data_file )
  return render_template('courses/constructive_conversations.html', course=course)

@blueprint.route('/course/running-small-projects')
def course_running_small_projects():
  with open('application/data/courses/running_small_projects.json') as data_file:
    course = json.load( data_file )
  return render_template('courses/running_small_projects.html', course=course)

@blueprint.route('/course/good-complaint-handling')
def course_good_complaint_handling():
  with open('application/data/courses/good_complaint_handling.json') as data_file:
    course = json.load( data_file )
  return render_template('course_layout.html', course=course)

@blueprint.route('/course/economics-for-policy-advisors')
def course_economics_for_policy_advisors():
  with open('application/data/courses/economics_for_policy_advisors.json') as data_file:
    course = json.load( data_file )
  return render_template('course_layout.html', course=course)

@blueprint.route('/course/change-leaders-for-senior-management')
def course_change_leaders_for_senior_management():
  with open('application/data/courses/change_leaders_for_senior_management.json') as data_file:
    course = json.load( data_file )
  return render_template('course_layout.html', course=course)

# ------------------------------------
# Priority areas
# ------------------------------------
@blueprint.route('/guide-priority-learning')
def priorities():
  return render_template('priority-learning.html')

@blueprint.route('/commercial')
def commercial():
  with open('application/data/commercial.json') as data_file:
    courses = json.load( data_file )
  return render_template('commercial.html', courses=courses)

@blueprint.route('/digital')
def digital():
  with open('application/data/digital.json') as data_file:
    courses = json.load( data_file )
  return render_template('digital.html', courses=courses)

@blueprint.route('/change-leadership')
def change_leadership():
  with open('application/data/change_leadership.json') as data_file:
    courses = json.load( data_file )
  return render_template('change_leadership.html', courses=courses)

@blueprint.route('/project-delivery')
def project_delivery():
  with open('application/data/project_delivery.json') as data_file:
    courses = json.load( data_file )
  return render_template('project_delivery.html', courses=courses)