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
  'css/styleguide-csl.scss',
  filters='scss',
  output='gen/css/styleguide.css',
  depends="**/*.scss"
)

# styles common across the learning pages
css_learning = Bundle(
  'css/learning.scss',
  filters='scss',
  output='gen/css/learning.css',
  depends="**/*.scss"
)

css_profile = Bundle(
  'css/profile.scss',
  filters='scss',
  output='gen/css/profile.css',
  depends="**/*.scss"
)

css_record = Bundle(
  'css/record.scss',
  filters='scss',
  output='gen/css/record.css',
  depends="**/*.scss"
)

css_rebrand = Bundle(
  'rebrand/css/rebrand.scss',
  filters='scss',
  output='gen/css/rebrand.css',
  depends='**/*.scss'
)

js_rebrand = Bundle(
    'rebrand/js/rebrand.js',
    filters='jsmin',
    output='gen/js/rebrand.js'
)

js_styleguide= Bundle(
    'js/styleguide.js',
    filters='jsmin',
    output='gen/js/styleguide.js'
)

assets = Environment()

assets.register('css_govuk', css_govuk)
assets.register('css_styleguide', css_styleguide)
assets.register('css_learning', css_learning)
assets.register('css_profile', css_profile)
assets.register('css_record', css_record)
assets.register('js_styleguide', js_styleguide)

assets.register('css_rebrand', css_rebrand)
assets.register('js_rebrand', js_rebrand)
