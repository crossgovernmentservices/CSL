# -*- coding: utf-8 -*-
from flask_assets import Bundle, Environment

# GOV.UK assets
css_govuk = Bundle(
  'css/govuk.scss',
  filters='scss',
  output='gen/css/govuk.css',
  depends="**/*.scss"
)

css_styleguide = Bundle(
  'css/govuk.scss',
  'css/styleguide.scss',
  filters='scss',
  output='gen/css/styleguide.css',
  depends="**/*.scss"
)

css_record = Bundle(
  'css/record.scss',
  filters='scss',
  output='gen/css/record.css',
  depends="**/*.scss"
)

assets = Environment()

assets.register('css_govuk', css_govuk)
assets.register('css_styleguide', css_styleguide)
assets.register('css_record', css_record)
