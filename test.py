import time
import RPi.GPIO as GPIO
from promus.media.Buzzer import Buzzer
from promus.led.SingleColorLed import SingleColorLed
from  promus.system.Environment import Environment
from promus.core.events import Event
try:
    def handle_events(evt):
        print evt.target.id() + " dispatched event:"+  evt.type
        return;

    env = Environment(False,GPIO, GPIO.BCM)
    myGreenLed = SingleColorLed(12,GPIO)
    myGreenLed.addEventListener(Event.EVT_COMPLETE,handle_events)
    myGreenLed.addEventListener(SingleColorLed.EVT_FLASH,handle_events)
    myGreenLed.flash(3,0.5)
    buzzer = Buzzer(16,GPIO)
    buzzer.addEventListener(Event.EVT_COMPLETE,handle_events)
    buzzer.buzz(404,1)
    while True:
        pass

    #Ultrasonic_HCSR04 = Ultrasonic_HCSR04(18,26,GPIO)

    #myUltraSonicSensor.addEventListener(Event.EVT_OBJECT_DETECTED,ultraSonicHandler)

    #env.addObject(SingleColorLed,(23,GPIO))
    #env.addObject(Ultrasonic_HCSR04,(18,26,GPIO))

    #myUltraSonicSensor.trigger()

except KeyboardInterrupt:
    print "exiting..."
    env.exit()
