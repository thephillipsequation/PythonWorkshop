''' i am a module '''
# pylint: disable=too-few-public-methods
import requests


class HelloRequests(object):
    ''' class for requests '''

    def make_request(self):
        ''' simple request method '''
        response = requests.get('https://www.google.com')
        return response.text


class Helloworld(object):
    ''' i am a class '''

    @classmethod
    def helloworld(cls, alpha, beta):
        ''' i am a method '''
        if alpha == beta:
            print "yyyyyy"
        return 3

    @classmethod
    def nomnomnom(cls):
        ''' i am a method '''
        return 3


class Foobar(object):
    ''' i am a class '''

    def __init__(self, hello_world):
        self.hello_world = hello_world

    def do_stuff(self):
        ''' i will do stuff '''
        my_bar = self.hello_world.helloworld(7, 8)
        if my_bar > 100:
            return "hello"
        return "goodbye"
