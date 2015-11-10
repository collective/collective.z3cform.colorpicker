
define([
  'jquery',
  'mockup-registry',
  'mockup-patterns-base',
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
