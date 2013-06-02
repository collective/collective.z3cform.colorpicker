.. contents::

Introduction
============

collective.z3cform.colorpicker provides two different jQuery based widgets:

- `Farbtastic <http://acko.net/dev/farbtastic>`_, a simple color picker.
- `jPicker <http://www.digitalmagicpro.com/jPicker/>`_, a jQuery Color Picker Plugin supporting transparency.


Requirements
============

* plone >= 3.2.1
* plone.app.z3cform


Installation
============

This addon can be installed has any other addons, please follow official
documentation_.


Usage
=====

You can use this widget setting the "widgetFactory" property of a form field:
::

        from zope import schema
        from z3c.form import form, field
        from collective.z3cform.colorpicker.colorpicker import ColorpickerFieldWidget
        from collective.z3cform.colorpicker.colorpickeralpha import ColorpickerAlphaFieldWidget

        class IColorForm(interface.Interface):
            color = schema.TextLine(title=u"Color",
                                    description=u"",
                                    required=False)
            alphacolor = schema.TextLine(title=u"Color with alpha layer support",
                                         description=u"",
                                         required=False)

        class Color(object):
            color = '#ff0000'
            alphacolor = 'ff0000cc'

            def __init__(self, context):
                self.context = context

        class ColorForm(form.Form):
            fields = field.Fields(IColorForm)
            fields['color'].widgetFactory = ColorpickerFieldWidget
            fields['alphacolor'].widgetFactory = ColorpickerAlphaFieldWidget

            ...


for more information see demo directory in the package sources.


.. _documentation: http://plone.org/documentation/kb/installing-add-ons-quick-how-to
