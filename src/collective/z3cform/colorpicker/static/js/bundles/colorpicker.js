
define([
  'jquery',
  'mockup-registry',
  'mockup-patterns-base',
//   Uncomment the line below to include all patterns from plone-mockup
//   'mockup-bundles-widgets',
//   <!~~ Add patterns below this line ~~!>
  'colorpicker-patterns-colorpicker'
], function($, Registry, Base) {
  'use strict';

  var colorpickerBundle = Base.extend({
    name: 'mockup-bundles-colorpicker',
    init: function() {
      var self = this;
    }
  });

  // initialize only if we are in top frame
  if (window.parent === window) {
    $(document).ready(function() {
      $('body').addClass('pat-colorpicker-bundle');
      Registry.scan($('body'));
    });
  }

  return colorpickerBundle;
});
