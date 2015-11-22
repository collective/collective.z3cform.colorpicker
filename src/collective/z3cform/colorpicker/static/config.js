(function() {
  'use strict';

  var requirejsOptions = {
    baseUrl: './',
    wrap: true,
    almond: true,
    optimize: 'none',
    paths: {
      'bootstrap-tooltip': 'bower_components/bootstrap/js/tooltip',
      'mjolnic-bootstrap-colorpicker': 'bower_components/mjolnic-bootstrap-colorpicker/dist/js/bootstrap-colorpicker',
      'jquery': 'bower_components/jquery/dist/jquery',
      'mockup-registry': 'bower_components/mockup-core/js/registry',
      'mockup-patterns-base': 'bower_components/mockup-core/js/pattern',
      'mockup-bundles-colorpicker': 'js/bundles/colorpicker',
      'colorpicker-patterns-colorpicker': 'js/patterns/colorpicker'
    },
    shim: {
      'bootstrap-tooltip': { deps: ['jquery'] },
      'mjolnic-bootstrap-colorpicker': { deps: ['jquery'] }
    },
    wrapShim: true
  };

  if (typeof exports !== "undefined" && typeof module !== "undefined") {
    module.exports = requirejsOptions;
  }
  if (typeof requirejs !== "undefined" && requirejs.config) {
    requirejs.config(requirejsOptions);
  }

}());
