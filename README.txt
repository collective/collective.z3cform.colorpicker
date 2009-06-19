Introduction
============

The color picker widget allows you to select a color and store its web exadecimal code.

The widget is based on TextLinesWidget (plone.z3cform.textlines) and Farbtastic, a jQuery color picker plug-in (http://acko.net/dev/farbtastic).

Requirements
------------
 * plone >= 3.2.1
 * plone.app.z3cform

Installation
============
Just a simple easy_install collective.z3cform.colorpicker is enough.

Alternatively, buildout users can install collective.z3cform.colorpicker as part of a specific project's buildout, by having a buildout configuration such as: ::

        [buildout]
        ...
        eggs = 
            zope.i18n>=3.4
            collective.z3cform.colorpicker
        ...
        [instance]
        ...
        zcml = 
            collective.z3cform.colorpicker


Usage
=====
You can use this widget setting the "widgetFactory" property of a form field:
::

        from zope import schema
        from z3c.form import form, field
        from collective.z3cform.colorpicker.colorpicker import ColorpickerFieldWidget

        class IColorForm(interface.Interface):
            color = schema.TextLine(title=u"Color",
                                    description=u"",
                                    required=False)

        class Color(object):
            color = '#ff0000'
            def __init__(self, context):
                self.context = context

        class ColorForm(form.Form):
            fields = field.Fields(IColorForm)
            fields['color'].widgetFactory = ColorpickerFieldWidget


for more information see demo directory in the package.

Contributors
============

* Giorgio Borelli - gborelli
* Silvio Tomatis - silviot

