import core.events.EventDispatcher
class Environment(Base):
    def __init__(gpio,mode="BCM"):
        self.gpio = gpio
        gpio.setmode(mode)
        self.sensors = []
        self.displays = []
        self.servers = []
        self.threads = []
        return;
    def addSensor(sensorInstance):
        sensorInstance.gpio= self.gpio
        self.id = "obj_"+rand(1000)
        self.sensors.append()
        return;
    def removeSensorById(sensorID):
        return;
    def removeSensor(sensorInstance):
        return;
    def addDisplay(displayInstance):
        return;
    def removeDisplay(displayInstance):
        return;
