import zope.component
import zope.interface
import zope.schema.interfaces

from z3c.form import interfaces
from z3c.form import widget
from z3c.form.browser import text


class IColorpickerWidget(interfaces.IWidget):
    """Colorpicker widget."""


class ColorpickerWidget(text.TextWidget):
    maxlength = 7
    size = 8
    readonly = True

    zope.interface.implementsOnly(IColorpickerWidget)

    def getJS(self):
        return """jQuery(document).ready(function() {
            jQuery("#%s-close").click(function(){
                  jQuery("#%s-popup").hide(400);
            });

            jQuery("#%s-show").click(function(){
                  jQuery("#%s-popup").toggle(400);
            });
            jQuery('#%s-colorpicker').farbtastic('#%s');
        });""".replace('%s', self.id)


def ColorpickerFieldWidget(field, request):
    """IFieldWidget factory for ColorpickerWidget."""
    return widget.FieldWidget(field, ColorpickerWidget(request))
