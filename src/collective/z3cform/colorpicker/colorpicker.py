from z3c.form.interfaces import IWidget
from z3c.form.widget import FieldWidget
from z3c.form.browser.text import TextWidget
from zope.interface import implementsOnly


class IColorpickerWidget(IWidget):
    """Colorpicker widget."""


class ColorpickerWidget(TextWidget):
    implementsOnly(IColorpickerWidget)
    maxlength = 7
    size = 8
    klass = u'pat-colorpicker'


def ColorpickerFieldWidget(field, request):
    """IFieldWidget factory for ColorpickerWidget."""
    return FieldWidget(field, ColorpickerWidget(request))
