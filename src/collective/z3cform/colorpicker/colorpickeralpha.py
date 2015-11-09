from z3c.form.interfaces import IWidget
from z3c.form.widget import FieldWidget
from z3c.form.browser.text import TextWidget
from zope.interface import implementsOnly


class IColorpickerAlphaWidget(IWidget):
    """Colorpicker widget with alpha support."""


class ColorpickerAlphaWidget(TextWidget):
    implementsOnly(IColorpickerAlphaWidget)
    size = 10
    klass = u'pat-colorpicker'


def ColorpickerAlphaFieldWidget(field, request):
    """IFieldWidget factory for ColorpickerAlphaWidget."""
    return FieldWidget(field, ColorpickerAlphaWidget(request))
