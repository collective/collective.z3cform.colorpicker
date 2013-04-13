/*global window, jQuery, document */
(function ($) {
    "use strict";

    $.fn.initJPicker = function () {
        this.find('.jpicker-widget').each(function () {
            var el = $(this),
                val = el.val(),
                position = el.position();
            el.jPicker({
                window: {
                    title: 'Color',
                    position: {
                        y: Math.round(position.top) + 300,
                        x: 'screenCenter'
                    },
                    alphaSupport: true,
                    expandable: true
                },
                images: {
                    clientPath: '++resource++colorpicker.jpicker/images/'
                },
                color: {
                    alphaSupport: true,
                    active: new $.jPicker.Color({ahex: val}),
                    current: new $.jPicker.Color({ahex: val})
                }
            },
                function (color, context) {
                    var colors = color.val('all'),
                        input = el;
                    input.val(colors.ahex);
                });
        });
    };

    $(document).ready(function () {
        $('body').initJPicker();
    });

}(jQuery));
