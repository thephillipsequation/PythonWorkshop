''' i am a test module '''
import unittest
from mypackage.helloworld import Helloworld, Foobar, HelloRequests
from mockito import mock
from mockito import verify
from mockito import verifyNoMoreInteractions
from mockito import when


class TestRequests(unittest.TestCase):
    ''' tests for the requests class '''

    def test_make_request(self):
        ''' test making a request '''
        retval = HelloRequests().make_request()
        self.assertIn('GOOGLE', retval.upper())


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
        when(self.hello_world).helloworld(7, 8).thenReturn(1000)
        self.assertEqual(self.foobar.do_stuff(), "hello")
        verify(self.hello_world).helloworld(7, 8)
        verifyNoMoreInteractions(self.hello_world)

    def test_do_stuff_2_or_whatever(self):
        ''' test do stuff '''
        when(self.hello_world).helloworld(7, 8).thenReturn(50)
        self.assertEqual(self.foobar.do_stuff(), "goodbye")
        verify(self.hello_world).helloworld(7, 8)
        verifyNoMoreInteractions(self.hello_world)
