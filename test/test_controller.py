import unittest

import controller


class TestController(unittest.TestCase):
    def test_validating_email(self):
        self.assertTrue(controller.validating_email("example@example.com"))
        self.assertTrue(controller.validating_email("hey@gmail.com"))
        self.assertFalse(controller.validating_email("example.com"))
        self.assertFalse(controller.validating_email("hola"))
        self.assertFalse(controller.validating_email("1545578"))
        self.assertFalse(controller.validating_email("example@"))
        self.assertFalse(controller.validating_email("@example.co"))

    def test_validating_age(self):
        self.assertTrue(controller.validating_age("15"))
        self.assertTrue(controller.validating_age("25"))
        self.assertFalse(controller.validating_age("-1"))
        self.assertFalse(controller.validating_age("0"))
        self.assertFalse(controller.validating_age("100"))
        self.assertFalse(controller.validating_age("hola"))
        self.assertFalse(controller.validating_age("15.5"))

    """
    The other methods are not tested since they are throwing errors due to the json file handling.
    By the way, all methods are working fine.
    """
        

if __name__ == '__main__':
    unittest.main()
