from flask import (
  Blueprint,
  render_template,
)


blueprint = Blueprint(
  'rebrand',
  __name__,
  static_folder='static',
  template_folder='templates')


@blueprint.route('/')
def signin():
  return render_template('signin.html')
