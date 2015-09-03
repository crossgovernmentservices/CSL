from flask import render_template
import json
import os
from application import app

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

# ------------------------------------
# Rebrand pages
# ------------------------------------
@app.route('/rebrand/signin')
def rb_signin():
  return render_template('rebrand/signin.html')

@app.route('/rebrand/professions')
def rb_professions():
  return render_template('rebrand/professions.html')

@app.route('/rebrand/guide-priority-learning')
def rb_priorities():
  return render_template('rebrand/priority-learning.html')

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

@app.route('/courses/digital-by-default')
def course_d_by_d():
  return render_template('courses/digital_by_default.html', type="e-learning")

@app.route('/courses/communication-skills')
def course_comm_skills():
  return render_template('courses/communication_skills.html')

@app.route('/courses/unconcious-bias')
def course_unconscious_bias():
  return render_template('courses/unconscious_bias.html', type="e-learning", status="completed")

# ------------------------------------
# Future pages
# ------------------------------------
@app.route('/future/search')
def future_search():
  return render_template('course_search.html')

@app.route('/future/calendar-view')
def future_calendar_view():
  return render_template('calendar-view.html')

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

@app.route('/styleguide/typography')
def sg_typog():
  return render_template('styleguide/typography.html')

@app.route('/styleguide/components')
def sg_components():
  return render_template('styleguide/components.html')
