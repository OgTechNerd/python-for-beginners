# The term metaprogramming refers to the potential for a program to have knowledge of or manipulate itself. 
# Python supports a form of metaprogramming for classes called metaclasses.
# Metaclasses are an esoteric OOP concept, lurking behind virtually all Python code. 
# You are using them whether you are aware of it or not. For the most part, you don’t need to be aware of it. 
# Most Python programmers rarely, if ever, have to think about metaclasses.
# When the need arises, however, Python provides a capability that not all 
# object-oriented languages support: you can get under the hood and define custom metaclasses. 
# The use of custom metaclasses is somewhat controversial, as suggested by the following quote from Tim Peters,
# the Python guru who authored the Zen of Python:

# Here's a more concrete example
# Lets write down the definition for a metaclasss


class MyMeta(type):
    def __call__(cls, *args, **kwds):
        print '__call__ of ', str(cls)
        print '__call__ *args=', str(args)
        return type.__call__(cls, *args, **kwds)

class MyKlass(object):
    __metaclass__ = MyMeta

    def __init__(self, a, b):
        print 'MyKlass object with a=%s, b=%s' % (a, b)

print 'gonna create foo now...'
foo = MyKlass(1, 2)