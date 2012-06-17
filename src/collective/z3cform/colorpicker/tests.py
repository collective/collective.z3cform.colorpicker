import unittest
import doctest

from zope.component import testing
from zope.interface import implements
from zope.publisher.browser import TestRequest as baseRequest

# from Products.Five import zcml
from Zope2.App import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
from z3c.form.interfaces import IFormLayer
ptc.setupPloneSite()

import collective.z3cform.colorpicker


class TestRequest(baseRequest):
    implements(IFormLayer)


class TestCase(ptc.PloneTestCase):
    class layer(PloneSite):
        @classmethod
        def setUp(cls):
            fiveconfigure.debug_mode = True
            zcml.load_config('configure.zcml',
                             collective.z3cform.colorpicker)
            fiveconfigure.debug_mode = False

        @classmethod
        def tearDown(cls):
            pass


def test_suite():
    return unittest.TestSuite([

        # Unit tests
        doctest.DocFileSuite(
           'README.txt', package='collective.z3cform.colorpicker',
           setUp=testing.setUp, tearDown=testing.tearDown),
        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
