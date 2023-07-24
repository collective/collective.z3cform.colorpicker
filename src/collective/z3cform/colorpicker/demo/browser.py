from plone.z3cform.layout import wrap_form
from z3c.form import form, field, button
from zope.interface import Interface
from collective.z3cform.colorpicker import Color


class IColorForm(Interface):
    color = Color(
        title=u"Color",
        description=u"",
        required=False,
        default=u"#6298c9")


class ColorDemoForm(form.Form):
    """Example color picker form"""

    fields = field.Fields(IColorForm)
    ignoreContext = True

    label = u"Colopicker Demo"
    description = (
        u"Color picker widget using native color input support."
    )

    def __init__(self, context, request):
        super(ColorDemoForm, self).__init__(context, request)
        self.request.set('disable_border', True)

    @button.buttonAndHandler(u'Save')
    def handleApply(self, action):
        # data, errors = self.extractData()
        return

Demo = wrap_form(ColorDemoForm)
