import time
import promus.core.events
class SingleColorLed(events.EventDispatcher):
    def __init__(pin,gpio):
        self.pin = pin
        self.__gpio = gpio
        return;
    def setup():
        self.__gpio.setup(self.pin, self.__gpio.OUT)
        return;
    def on():
        self.__gpio.output(self.pin,self.__gpio.HIGH)
        evt = events.Event(events.Event.ON)
        evt.target= self
        self.dispatchEvent(evt)
        return;
    def off():
        self.__gpio.output(self.pin,self.__gpio.LOW)
        evt = events.Event(events.Event.OFF)
        evt.target= self
        self.dispatchEvent(evt)
        return;
    def flash(times,delay):
        self.__gpio.output(self.pin,self.__gpio.LOW)
        time.sleep(delay)
        self.__gpio.output(self.pin,self.__gpio.LOW)
        time.sleep(delay)
        evt = events.Event(events.Event.COMPLETE)
        evt.target = self
        self.dispatchEvent(evt)
        return;
