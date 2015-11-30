import time
from promus.core.events import Event
from promus.core.events import EventDispatcher

class Buzzer(EventDispatcher):
    def __init__(self, pin , gpio):
        super(Buzzer,self).__init__()
        self.pin = pin
        self.__gpio = gpio
        self.setup()
        return;
    def setup(self):
        self.__gpio.setup(self.pin, self.__gpio.OUT)
        return;
    def buzz(self,pitch, duration):   #create the function buzz and feed it the pitch and duration)
        period = 1.0 / pitch     #in physics, the period (sec/cyc) is the inverse of the frequency (cyc/sec)
        delay = period / 2     #calcuate the time for half of the wave
        cycles = int(duration * pitch)   #the number of waves to produce is the duration times the frequency
        for i in range(cycles):
            self.__gpio.output(self.pin, True)   #set pin 18 to high
            time.sleep(delay)
            self.__gpio.output(self.pin, False)
            time.sleep(delay)
        evt = Event(Event.EVT_COMPLETE)
        evt.target = self
        self.dispatchEvent(evt)
        return;
