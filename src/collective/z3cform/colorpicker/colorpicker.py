from z3c.form.interfaces import IFormLayer
from z3c.form.interfaces import IFieldWidget

from z3c.form.interfaces import IWidget
from z3c.form.widget import FieldWidget
from z3c.form.browser.text import TextWidget
from zope.component import adapter
from zope.interface import implementer
from zope.interface import implementsOnly
from zope.schema.interfaces import IField


class IColorpickerWidget(IWidget):
    """Colorpicker widget."""


class ColorpickerWidget(TextWidget):
    implementsOnly(IColorpickerWidget)
    maxlength = 7
    size = 8
    klass = u'pat-colorpicker'


@adapter(IField, IFormLayer)
@implementer(IFieldWidget)
def ColorpickerFieldWidget(field, request):
    """IFieldWidget factory for ColorpickerWidget."""
    return FieldWidget(field, ColorpickerWidget(request))
