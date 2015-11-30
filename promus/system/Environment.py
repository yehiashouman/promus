import thread
import promus.core.events.EventDispatcher
class Environment(Base):
    def __init__(gpio,mode="BCM"):
        self.__gpio = gpio
        self.__gpio.setmode(mode)
        self.__objects = []
        self.__threads = []
        return;
    def addObject(className,args):
        thread.start_new_thread(className, args)
        self.__objects.append(objInstance)
        return;
    def removeObjectById(objID):
        for obj in self.__objects:
            if(obj.id=objID):
                self.__objects.remove(obj)
        return;
    def removeObject(objInstance):
            self.__objects.remove(objInstance)
        return;
    def exit():
        self.__gpio.cleanup()
        #TODO: terminate threads
        return;
