Changelog
=========

2.1.0 (2021-09-17)
------------------

- Python 3 support.  [espen]


2.0 (2017-12-21)
----------------

- Added Color and ColorAlpha fields for colorpicker widgets
  [giorgio]

- Removed JPicker and farbastic javascripts
  [gborelli]

- Added colorpicker patterns based on bootstrap-colorpicker
  [gborelli]

- Added plone5.0 resource registry support
  [gborelli]

- Added Docker configuration for development
  [gborelli]

- Improved demo page - http://<yourplonesite>/@@colorpicker-demo
  [gborelli]


1.4 (2015-11-11)
----------------

- Added Dutch translations.
  [maurits]

- Made the close button translatable.
  Found with ``i18ndude find-untranslated .``.
  [maurits]


1.3 (2015-10-05)
----------------

- Remove from jpicker js file the bad chars from the begining
  [bloodbare]

- Renamed txt files to rst, without symlinks.  Symlinks can give
  installation problems, due to either the symlink or the original
  file missing from the distribution or being empty, because the link
  can end up the wrong way around.  Fixes issue #1.
  [maurits]


1.2 (2015-05-02)
----------------

- Updated classifiers list for package [macagua]
- Added Spanish translation [macagua]


1.1 (2013-06-02)
----------------

- fix MANIFEST.in
  [gborelli]


1.0 (2013-06-02)
----------------

- add z3cform_colorpicker.js to initialize JPicker widget
  [gborelli]

- add internationalization support
  [gborelli]

- add css and javascript to Plone registry in order to make html valid
  [gborelli]

- add profile to install colorpicker package
  [gborelli]

- change some jpicker styles
  [gborelli]

- update jpicker to v1.1.6
  [gborelli]

- egg layout refactoring
  [gborelli]

- change Browser import from Testing.testbrowser
  [gborelli]


0.2 (2010-10-31)
----------------

- include jPicker widget for alpha transparency support
  [gborelli]

0.1 (2009-06-19)
----------------

* Initial release
