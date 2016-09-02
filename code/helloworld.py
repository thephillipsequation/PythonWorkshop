''' i am a module '''
# pylint: disable=too-few-public-methods


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
