================
ColorPicker Widget
================

The color picker widget allows you to select a color and store its web exadecimal code.
Widget based on TextLinesWidget - plone.z3cform.textlines

As for all widgets, the text lines widget must provide the new ``IWidget``
interface:

  >>> from zope.interface.verify import verifyClass
  >>> from z3c.form import interfaces
  >>> from collective.z3cform.colorpicker import colorpicker

  >>> from plone.z3cform.tests import setup_defaults
  >>> setup_defaults()

  >>> verifyClass(interfaces.IWidget, colorpicker.ColorpickerWidget)
  True

The widget can be instantiated only using the request:

  >>> from z3c.form.testing import TestRequest
  >>> request = TestRequest()

  >>> widget = colorpicker.ColorpickerWidget(request)

Before rendering the widget, one has to set the name and id of the widget:

  >>> widget.id = 'id'
  >>> widget.name = 'name'

We also need to register the template for at least the widget and request:

  >>> import zope.component
  >>> from zope.pagetemplate.interfaces import IPageTemplate
  >>> from z3c.form.widget import WidgetTemplateFactory
  >>> import os.path
  >>> template = os.path.join(os.path.dirname(colorpicker.__file__),
  ...     'colorpicker_input.pt')
  >>> factory = WidgetTemplateFactory(template, 'text/html')

  >>> zope.component.provideAdapter(
  ...     factory,
  ...     (None, None, None, None, colorpicker.IColorpickerWidget),
  ...     IPageTemplate, name=interfaces.INPUT_MODE)

If we render the widget we get an input widget that include farbastic js:

  >>> print widget.render()
  <script type="text/javascript" src="++resource++colorpicker.farbtastic/farbtastic.js"></script>
  <style type="text/css">
      @import "++resource++colorpicker.farbtastic/farbtastic.css";
  </style>
  <BLANKLINE>
  <input type="text" id="id" name="name"
         class="text-widget color" readonly="readonly"
         size="8" maxlength="7" value="" />
  <BLANKLINE>
  <BLANKLINE>
  <a href="" onclick="return false" id="id-show">Choose color</a>
  <BLANKLINE>
  <div class="color-popup" id="id-popup">
    <div class="color-popup-header"><a title="Close popup"
      id="id-close">(x)</a></div>
    <div id="id-colorpicker"></div>
  </div>
  <BLANKLINE>
  <script type="text/javascript">jQuery(document).ready(function() {
              jQuery("#id-close").click(function(){
                    jQuery("#id-popup").hide(400);
              });
  <BLANKLINE>
              jQuery("#id-show").click(function(){
                    jQuery("#id-popup").toggle(400);
              });
              jQuery('#id-colorpicker').farbtastic('#id');
          });</script>
  <BLANKLINE>


Adding some more attributes to the widget will make it display more:

  >>> widget.id = 'my-widget-id'
  >>> widget.name = 'my-widget-name'
  >>> widget.value = u'#ff0000'

  >>> print widget.render()
  <script type="text/javascript" src="++resource++colorpicker.farbtastic/farbtastic.js"></script>
  <style type="text/css">
      @import "++resource++colorpicker.farbtastic/farbtastic.css";
  </style>
  <BLANKLINE>
  <input type="text" id="my-widget-id" name="my-widget-name"
         class="text-widget color" readonly="readonly"
         size="8" maxlength="7" value="#ff0000" />
  <BLANKLINE>
  <BLANKLINE>
  <a href="" onclick="return false" id="my-widget-id-show">Choose color</a>
  <BLANKLINE>
  <div class="color-popup" id="my-widget-id-popup">
    <div class="color-popup-header"><a title="Close popup"
      id="my-widget-id-close">(x)</a></div>
    <div id="my-widget-id-colorpicker"></div>
  </div>
  <BLANKLINE>
  <script type="text/javascript">jQuery(document).ready(function() {
              jQuery("#my-widget-id-close").click(function(){
                    jQuery("#my-widget-id-popup").hide(400);
              });
  <BLANKLINE>
              jQuery("#my-widget-id-show").click(function(){
                    jQuery("#my-widget-id-popup").toggle(400);
              });
              jQuery('#my-widget-id-colorpicker').farbtastic('#my-widget-id');
          });</script>
  <BLANKLINE>

