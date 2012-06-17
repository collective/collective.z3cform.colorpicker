import zope.component
import zope.interface
import zope.schema.interfaces

from z3c.form import interfaces
from z3c.form import widget
from z3c.form.browser import text

class IColorpickerAlphaWidget(interfaces.IWidget):
    """Colorpicker widget."""

class ColorpickerAlphaWidget(text.TextWidget):
    maxlength = 7
    size = 8
    readonly = False

    zope.interface.implementsOnly(IColorpickerAlphaWidget)

    def getJS(self):
        return """jq(document).ready(function() {jq('#widgetid').jPicker({
                     window:{expandable:true,
                             title:'Color',
                             position:{y:'bottom', x:'right'},
                             alphaSupport:true,},
                     images:{clientPath: '++resource++colorpicker.jpicker/images/'},
                     color:{
                         alphaSupport: true,
                         active: new jq.jPicker.Color({ ahex: jq('#widgetid').val()}),
                         current: new jq.jPicker.Color({ ahex: jq('#widgetid').val()}),}},
                     function(color, context){
                       var colors = color.val('all');
                       var input = jq('#widgetid');
                       input.val(colors.ahex);}
                     );
           });""".replace('widgetid', self.id)


def ColorpickerAlphaFieldWidget(field, request):
    """IFieldWidget factory for ColorpickerAlphaWidget."""
    return widget.FieldWidget(field, ColorpickerAlphaWidget(request))

