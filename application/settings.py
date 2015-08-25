import os

class ProdConfig(object):
  DEBUG = False
  ASSETS_DEBUG = True
  BASIC_AUTH_FORCE = os.environ.get('BASIC_AUTH_FORCE')
  BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME')
  BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD')

class DevConfig(object):
  DEBUG = True
  ASSETS_DEBUG = True
