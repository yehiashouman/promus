import promus.core.events
class SingleColorLed(events.EventDispatcher):
    def __init__(pin,gpio)
        self.pin = ledPin
        self.__gpio = gpio
        self.__gpio.setup(self.pin, self.__gpio.OUT)
        return;
    def on():
        self.__gpio.output(self.pin,self.__gpio.HIGH)
        self.dispatchEvent(Event.ON)
        return;
    def off():
        self.__gpio.output(self.pin,self.__gpio.LOW)
        self.dispatchEvent(Event.OFF)
        return;
