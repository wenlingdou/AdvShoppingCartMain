import unittest
import adshopcart_locators as locators
import adshopcart_methods as methods

class PositiveTestCases(unittest.TestCase):

    @staticmethod   # signal to Unittest that this is a function inside class (vs @classmethod)
    def test_create_new_user():  # test_ in the name is mandatory
        methods.setUp()

        methods.tearDown()