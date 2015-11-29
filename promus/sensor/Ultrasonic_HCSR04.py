import Base promus.core.Base
import promus.core.events
class Ultrasonic_HCSR04(events.EventDispatcher):
    def __init__(trigPin,echoPin,gpio):
        self.trigPin = trigPin
        self.echoPin = echoPin
        self.__gpio = gpio
        self.__gpio.setup(self.trigPin, self.__gpio.OUT)
        self.__gpio.setup(self.echoPin, self.__gpio.IN)
        return;
    def trigger():

        """" detect event here
        """"
        self.dispatchEvent(events.Event(events.Event.OBJECT_DETECTED))
        return;
