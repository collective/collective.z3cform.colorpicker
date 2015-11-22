/* Colorpicker
 *
 * Options:
 *    format(string): define the color format used by the widget
 *                    it could be chosen between hex, rgb or rgba;
 *
 * Documentation:
 *   # Colorpicker widget
 *
 *   A color picker widget based on http://mjolnic.com/bootstrap-colorpicker/
 *
 *   # Example
 *
 *   {{ EXAMPLE_ANCHOR }}
 *
 * Example: EXAMPLE_ANCHOR
 *
 *     <div class="field">
 *       <label for="colorpicker">Standard colorpicker</label>
 *       <div class="input-group pat-colorpicker"
 *            data-pat-colorpicker="format: hex">
 *         <input type="text"
 *                name="colorpicker"
 *                value="#6298c9"
 *                class="form-control" />
 *         <span class="input-group-addon"><i></i></span>
 *       </div>
 *     </div>
 *
 */
define([
  'jquery',
  'mockup-patterns-base',
  'bootstrap-tooltip',
  'mjolnic-bootstrap-colorpicker'
], function($, Base) {
  'use strict';
  var colorpickerPattern = Base.extend({
    // The name for this pattern
    name: 'colorpicker',

    defaults: {
      format: 'hex'  // hex, rgb or rgba
    },

    init: function() {
      var self = this,
          initial_color = $('input', self.$el).val();

      self.$el.colorpicker({
        color: initial_color,
        format: self.options.format
      });
    }

  });

  return colorpickerPattern;

});
