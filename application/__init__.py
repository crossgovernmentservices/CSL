import os
import sys
import logging
from flask import Flask

app = Flask(__name__)

from application.settings import DevConfig, ProdConfig
# set up basic auth if in prod environment
if os.environ.get("APPLICATION_ENV") == 'prod':
    app.config.from_object(ProdConfig)
else:
    app.config.from_object(DevConfig)
print(app.config)

# Small thing to allow source code examples in a template
app.jinja_env.globals['include_raw'] = lambda filename : app.jinja_loader.get_source(app.jinja_env, filename)[0]

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

from application import views
from application.assets import assets
assets.init_app(app)

# use pattern below to if app context required
# with app.app_context():

# to do (use extension.asset_locator)
# see http://stackoverflow.com/questions/4383571/importing-files-from-different-folder-in-python
from application.asset_locator import AssetLocator
asset_locator = AssetLocator()
asset_locator.init_app(app)

from flask_basicauth import BasicAuth
basic_auth = BasicAuth(app)

from application import rebrand
app.register_blueprint(rebrand.views.blueprint, url_prefix='/test')

