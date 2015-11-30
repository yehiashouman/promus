import time
from promus.core.events import Event
from promus.core.events import EventDispatcher

class SingleColorLed(EventDispatcher):
    EVT_FLASH = "flash"
    def __init__(self, pin , gpio):
        super(SingleColorLed,self).__init__()
        self.pin = pin
        self.__gpio = gpio
        self.setup()
        return;
    def setup(self):
        self.__gpio.setup(self.pin, self.__gpio.OUT)
        return;
    def on(self):
        self.__gpio.output(self.pin,self.__gpio.HIGH)
        evt = Event(Event.EVT_ON)
        evt.target= self
        self.dispatchEvent(evt)
        return;
    def off(self):
        self.__gpio.output(self.pin,self.__gpio.LOW)
        evt = Event(Event.EVT_OFF)
        evt.target= self
        self.dispatchEvent(evt)
        return;
    def flash(self,times,delay):
        for i in range(times):
            self.__gpio.output(self.pin,self.__gpio.HIGH)
            time.sleep(delay)
            self.__gpio.output(self.pin,self.__gpio.LOW)
            time.sleep(delay)
            evt = Event(SingleColorLed.EVT_FLASH)
            evt.target = self
            self.dispatchEvent(evt)
        evt = Event(Event.EVT_COMPLETE)
        evt.target = self
        self.dispatchEvent(evt)
        return;
