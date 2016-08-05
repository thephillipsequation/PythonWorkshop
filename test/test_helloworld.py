import unittest
from code.helloworld import Helloworld


class TestStringMethods(unittest.TestCase):
    '''This is our test class'''

    def test_print(self):
        '''test helloworld'''
        self.assertEquals(Helloworld().helloworld(), 3)

