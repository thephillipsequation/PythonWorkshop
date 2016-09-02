''' i am a module '''
# pylint: disable=too-few-public-methods


class Helloworld(object):
    ''' i am a class '''

    @classmethod
    def helloworld(cls, a, b):
        ''' i am a method '''
        if a == b:
            print "yyyyyy"
        return 3

    @classmethod
    def nomnomnom(cls):
        ''' i am a method '''
        return 3
