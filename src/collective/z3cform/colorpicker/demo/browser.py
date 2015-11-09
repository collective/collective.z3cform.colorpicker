from plone.z3cform.layout import wrap_form
from z3c.form import form, field, button
from zope import schema
from zope.interface import Interface
from collective.z3cform.colorpicker import ColorpickerFieldWidget
from collective.z3cform.colorpicker import ColorpickerAlphaFieldWidget


class IColorForm(Interface):
    color = schema.TextLine(
        title=u"Color",
        description=u"",
        required=False,
        default=u"#6298c9")

    alphacolor = schema.TextLine(
        title=u"Color with alpha layer support",
        description=u"",
        required=False,
        default=u"rgba(104,191,144,0.55)")


class ColorDemoForm(form.Form):
    """Example color picker form"""

    fields = field.Fields(IColorForm)
    fields['color'].widgetFactory = ColorpickerFieldWidget
    fields['alphacolor'].widgetFactory = ColorpickerAlphaFieldWidget
    ignoreContext = True

    label = u"Colopicker Demo"
    description = (
        u"Color picker widget based on "
        u"http://mjolnic.com/bootstrap-colorpicker/"
    )

    def __init__(self, context, request):
        super(ColorDemoForm, self).__init__(context, request)
        self.request.set('disable_border', True)

    @button.buttonAndHandler(u'Save')
    def handleApply(self, action):
        # data, errors = self.extractData()
        return

Demo = wrap_form(ColorDemoForm)
