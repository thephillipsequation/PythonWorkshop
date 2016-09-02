''' i am a test module '''
import unittest
from code.helloworld import Helloworld


class TestStringMethods(unittest.TestCase):
    '''This is our test class'''

    def test_print_branch1(self):
        '''test helloworld'''
        self.assertEquals(Helloworld().helloworld(1, 1), 3)

    def test_print_branch2(self):
        '''test helloworld'''
        self.assertEquals(Helloworld().helloworld(1, 2), 3)

    def test_nomnomnom(self):
        '''test helloworld'''
        self.assertEquals(Helloworld.nomnomnom(), 3)
