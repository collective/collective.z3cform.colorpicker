from zope.interface import implementer
from zope.schema import TextLine
from zope.schema.interfaces import ITextLine


class IColorAlpha(ITextLine):
    pass


@implementer(IColorAlpha)
class ColorAlpha(TextLine):
    pass


class IColor(ITextLine):
    pass


@implementer(IColor)
class Color(TextLine):
    pass
