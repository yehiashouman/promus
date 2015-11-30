import thread
from  promus.core.events import EventDispatcher
class Environment(EventDispatcher):
    def __init__(self, warningsFlag,gpio ,mode="BCM"):
        super(Environment,self).__init__()
        self.__gpio = gpio
        self.__gpio.setwarnings(warningsFlag)
        self.__gpio.setmode(mode)
        self.__objects = []
        self.__threads = []
        return;
    def addObject(self,className,args):
        thread= thread.start_new_thread(className, args)
        self.__objects.append(thread)
        return;
    def removeObjectById(self,objID):
        for obj in self.__objects:
            if obj.id == objID:
                self.__objects.remove(obj)
        return;
    def removeObject(self,objInstance):
            self.__objects.remove(objInstance)
            return;
    def exit(self):
        self.__gpio.cleanup()
        #TODO: terminate threads
        return;
