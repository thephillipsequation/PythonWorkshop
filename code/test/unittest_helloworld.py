'''unittest for helloworld.py'''
import unittest
import code.helloworld as foo


class TestStringMethods(unittest.TestCase):
    '''This is our test class'''

    def test_print(self):
        '''test helloworld'''
        self.assertTrue(1 == 1)
        foo.hello_world()


if __name__ == '__main__':
    unittest.main()
