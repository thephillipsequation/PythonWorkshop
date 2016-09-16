''' i am a test module '''
import unittest
from code.helloworld import Helloworld, Foobar
from mockito import mock
from mockito import verify
from mockito import verifyNoMoreInteractions


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


class TestFoobar(unittest.TestCase):
    ''' tests for foobar '''

    def setUp(self):
        ''' set up test '''
        self.hello_world = mock()
        self.foobar = Foobar(self.hello_world)

    def test_do_stuff(self):
        ''' test do stuff '''
        self.foobar.do_stuff()
        verify(self.hello_world).helloworld(7, 8)
        verifyNoMoreInteractions(self.hello_world)
