import random
class Base(object):
    def __init__(self):
        super(Base,self).__init__()
        self._id =str(type(self).__name__) + str(int(1000*random.random()))
        return;
    def id(self): 
        return str(self._id)
    def toString(self):
        return type(self)
