import unittest
import adshopcart_locators as locators
import adshopcart_methods as methods

class PositiveTestCases(unittest.TestCase):

    @staticmethod   # signal to Unittest that this is a function inside class (vs @classmethod)
    def test_create_new_user():  # test_ in the name is mandatory
        methods.setUp()
        methods.check_homepage()
        methods.create_new_account()
        methods.register()
        methods.check_fullname()
        methods.check_orders()
        methods.logout()
        methods.login()
        methods.delete_account()
        methods.login()
        methods.check_delete()
        methods.tearDown()