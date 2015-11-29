import promus.core.events.EventDispatcher
class Environment(Base):
    def __init__(gpio,mode="BCM"):
        self.__gpio = gpio
        self.__gpio.setmode(mode)
        self.__sensors = []
        self.__displays = []
        self.__servers = []
        self.__threads = []
        return;
    def addSensor(sensorInstance):
        sensorInstance.gpio= self.__gpio
        self.__sensors.append()
        return;
    def removeSensorById(sensorID):
        return;
    def removeSensor(sensorInstance):
        return;
    def addDisplay(displayInstance):
        return;
    def removeDisplay(displayInstance):
        return;
