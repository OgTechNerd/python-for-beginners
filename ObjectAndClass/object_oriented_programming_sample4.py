# Destroying Objects GarbageCollection
# Python deletes unneeded objects built − intypesorclassinstances automatically to free the memory space.
# The process by which Python periodically reclaims blocks of memory that no longer are in use is
# termed Garbage Collection.
# Python's garbage collector runs during program execution and is triggered when an object's
# reference count reaches zero. An object's reference count changes as the number of aliases that
# point to it changes.
# An object's reference count increases when it is assigned a new name or placed in a container
# list, tuple, or dictionary. The object's reference count decreases when it's deleted with del, its reference
# is reassigned, or its reference goes  out of scope. When an object's reference count reaches zero,
# Python collects it automatically.

class Sample2(object):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __del__(self):
        className = self.__class__.__name__
        print ("destroyed {} of {}".format(object, className))
    
if __name__ == "__main__":
    object1 = Sample2( "shaun", 2000)
    object2 = object1
    object1.__del__()
    print(object2)

 
 
