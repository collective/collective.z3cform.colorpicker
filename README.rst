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

        from z3c.form import form, field
        from collective.z3cform.colorpicker import Color
        from collective.z3cform.colorpicker import ColorAlpha

        class IColorForm(interface.Interface):
            color = Color(
                title=u"Color",
                description=u"",
                required=False,
                default="#ff0000"
            )
            alphacolor = ColorAlpha(
                title=u"Color with alpha layer support",
                description=u"",
                required=False,
                default=u"rgba(104,191,144,0.55)"
            )


        class ColorForm(form.Form):
            fields = field.Fields(IColorForm)
            ...

for more information see demo directory in the package sources.


.. _documentation: http://plone.org/documentation/kb/installing-add-ons-quick-how-to
