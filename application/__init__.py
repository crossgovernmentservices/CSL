from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

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

