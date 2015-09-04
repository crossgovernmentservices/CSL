from flask import (
  Blueprint,
  render_template,
)


blueprint = Blueprint(
  'rebrand',
  __name__,
  static_folder='static',
  template_folder='templates')

# ------------------------------------
# Rebrand pages
# ------------------------------------
@blueprint.route('/')
def signin():
  return render_template('signin.html')

@blueprint.route('/professions')
def professions():
  return render_template('professions.html')

@blueprint.route('/guide-priority-learning')
def priorities():
  return render_template('priority-learning.html')

@blueprint.route('/commercial')
def commercial():
  return render_template('commercial.html')