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
    klass = u'jpicker-widget'

    zope.interface.implementsOnly(IColorpickerAlphaWidget)

    # def getJS(self):
    #     return """jq(document).ready(function() {jq('#widgetid').jPicker({
    #             window:{title:'Color',
    #                     alphaSupport:true,},
    #             images:{clientPath: '++resource++colorpicker.jpicker/images/'},
    #        });""".replace('widgetid', self.id)


def ColorpickerAlphaFieldWidget(field, request):
    """IFieldWidget factory for ColorpickerAlphaWidget."""
    return widget.FieldWidget(field, ColorpickerAlphaWidget(request))
