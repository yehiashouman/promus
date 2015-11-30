import time
import promus.core.events
class Buzzer(events.EventDispatcher):
    def __init__(pin,gpio):
        self.pin = pin
        self.__gpio = gpio
        return;
    def setup():
        self.__gpio.setup(self.pin, self.__gpio.OUT)
        return;
    def buzz(self,pitch, duration):   #create the function “buzz” and feed it the pitch and duration)
        period = 1.0 / pitch     #in physics, the period (sec/cyc) is the inverse of the frequency (cyc/sec)
        delay = period / 2     #calcuate the time for half of the wave
        cycles = int(duration * pitch)   #the number of waves to produce is the duration times the frequency
        for i in range(cycles):
            self.__gpio.output(self.pin, True)   #set pin 18 to high
            time.sleep(delay)
            self.__gpio.output(self.pin, False)
            time.sleep(delay)
        evt = events.Event(events.Event.COMPLETE)
        evt.target = self
        self.dispatchEvent(evt)
        return;
