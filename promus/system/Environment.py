import promus.core.events.EventDispatcher
class Environment(Base):
    def __init__(gpio,mode="BCM"):
        self.__gpio = gpio
        self.__gpio.setmode(mode)
        self.__objects = []
        self.__threads = []
        return;
    def addObject(objInstance):
        objInstance.gpio= self.__gpio
        self.__sensors.append()
        return;
    def removeObjectById(objID):
        return;
    def removeObject(objInstance):
        return;
