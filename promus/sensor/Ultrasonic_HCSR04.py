import time
from promus.core.events import Event
from promus.core.events import EventDispatcher

class Ultrasonic_HCSR04(events.EventDispatcher):
    def __init__(self,trigPin,echoPin,gpio):
        super(Ultrasonic_HCSR04,self).__init__()
        self.trigPin = trigPin
        self.echoPin = echoPin
        self.__gpio = gpio
        self.__signalon  = 0
        self.__signaloff = 0
        return;
    def setup(self):
        self.__gpio.setup(self.trigPin, self.__gpio.OUT)
        self.__gpio.setup(self.echoPin, self.__gpio.IN)
        self.__gpio.output(self.trigPin, self.__gpio.LOW)
        time.sleep(0.3)
        return;
    def trigger(self):
        self.__gpio.output(self.trigPin, self.__gpio.HIGH)
        time.sleep(0.00001)
        self.__gpio.output(self.trigPin, self.__gpio.LOW)
        while self.__gpio.input(self.echoPin) == 0:
            self.__signaloff = time.time()
        while self.__gpio.input(self.echoPin) == 1:
            self.__signalon = time.time()
        timepassed = self.__signalon - self.__signaloff
        distance = timepassed * 17250
        evt = events.Event(Event.EVT_OBJECT_DETECTED)
        evt.target=self
        evt.distance = distance
        self.dispatchEvent(evt)
        return;
