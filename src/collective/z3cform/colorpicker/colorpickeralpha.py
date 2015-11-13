from z3c.form.interfaces import IFormLayer
from z3c.form.interfaces import IFieldWidget
from z3c.form.interfaces import IWidget
from z3c.form.widget import FieldWidget
from z3c.form.browser.text import TextWidget
from zope.component import adapter
from zope.interface import implementer
from zope.interface import implementsOnly
from zope.schema.interfaces import IField


class IColorpickerAlphaWidget(IWidget):
    """Colorpicker widget with alpha support."""


class ColorpickerAlphaWidget(TextWidget):
    implementsOnly(IColorpickerAlphaWidget)
    size = 10
    klass = u'pat-colorpicker'


@adapter(IField, IFormLayer)
@implementer(IFieldWidget)
def ColorpickerAlphaFieldWidget(field, request):
    """IFieldWidget factory for ColorpickerAlphaWidget."""
    return FieldWidget(field, ColorpickerAlphaWidget(request))
