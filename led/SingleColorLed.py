import core.Base.EventDispatcher
class SingleColorLed(EventDispatcher.EventDispatcher):
    def __init__(pin,gpio)
        self.pin = ledPin
        self.gpio = gpio
        self.gpio.setup(self.pin, self.gpio.OUT)
        return;
    def on():
        self.gpio.output(self.pin,gpio.HIGH)
        self.dispatchEvent(Event.ON)
        return;
    def off():
        self.gpio.output(self.pin,gpio.LOW)
        self.dispatchEvent(Event.OFF)
        return;
