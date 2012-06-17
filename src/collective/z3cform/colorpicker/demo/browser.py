from zope.interface import implements
from zope.interface import Interface
from z3c.form import form, field, button
from zope import schema
from plone.z3cform.layout import wrap_form
from ..colorpicker import ColorpickerFieldWidget
from ..colorpickeralpha import ColorpickerAlphaFieldWidget


class IColorForm(Interface):
    color = schema.TextLine(title=u"Color",
                               description=u"",
                               required=False)

    alphacolor = schema.TextLine(title=u"Color with alpha layer support",
                               description=u"",
                               required=False)


class Color(object):
    implements(IColorForm)
    color = '#ff0000'
    alphacolor = 'ff0000cc'

    def __init__(self, context):
        self.context = context


class ColorDemoForm(form.Form):
    """Example color picker form"""

    fields = field.Fields(IColorForm)
    fields['color'].widgetFactory = ColorpickerFieldWidget
    fields['alphacolor'].widgetFactory = ColorpickerAlphaFieldWidget

    def __init__(self, context, request):
        super(ColorDemoForm, self).__init__(context, request)
        self.request.set('disable_border', True)

    @button.buttonAndHandler(u'Save')
    def handleApply(self, action):  # pylint: disable=W0613
        # data, errors = self.extractData()
        return

Demo = wrap_form(ColorDemoForm)
