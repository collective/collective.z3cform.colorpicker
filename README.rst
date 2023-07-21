.. contents::

Introduction
============

collective.z3cform.colorpicker provides a color picker widget, which uses the Browser native color input.

.. image:: https://raw.githubusercontent.com/collective/collective.z3cform.colorpicker/master/screenshot.png


Requirements
============

* Plone >= 5.0
* plone.app.z3cform

For previous Plone versions use a version collective.z3cform.colorpicker
less than 2.x


Installation
============

Install collective.z3cform.colorpicker by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.z3cform.colorpicker


and then running ``bin/buildout``

or installing it via ``pip install collective.z3cform.colorpicker``


Usage
=====

You can use this widget setting the "widgetFactory" property of a form field:
::

        from z3c.form import form, field
        from collective.z3cform.colorpicker import Color

        class IColorForm(interface.Interface):
            color = Color(
                title=u"Color",
                description=u"",
                required=False,
                default="#ff0000"
            )


        class ColorForm(form.Form):
            fields = field.Fields(IColorForm)
            ...

for more information see demo directory in the package sources.
