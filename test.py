import inspect,sys
import time
import RPi.GPIO as GPIO
from promus.media.Buzzer import Buzzer
from promus.led.SingleColorLed import SingleColorLed
from promus.sensor.Ultrasonic_HCSR04 import Ultrasonic_HCSR04
from  promus.system.Environment import Environment
from promus.core.events import Event
from threading import Thread
from multiprocessing import Process
buzzInterval=1

try:
    def makeClassInstance(cls, *args, **kwargs):
        try:
            return globals()[cls](*args, **kwargs)
        except:
            raise NameError("Class %s is not defined" % cls)
    def print_classes(mod):
        return inspect.getmembers(sys.modules[mod], inspect.isclass);
        for name, obj in inspect.getmembers(sys.modules[mod]):
            if inspect.isclass(obj):
                print(obj)
        return; 
    def handle_events(evt):
        global buzzInterval
        print evt.target.id() + " dispatched event:"+  evt.type + " Buzz Interval: "+str(buzzInterval)
        if hasattr(evt,"distance"):
            buzzInterval = 1 * (evt.distance/60)
        if(evt.target.id()==buzzer.id() and evt.type ==Event.EVT_COMPLETE):
            #print "Buzz "+str(buzzInterval)
            time.sleep(buzzInterval);
            buzzer.buzz(800,buzzInterval)
        return;

    env = Environment(False,GPIO, GPIO.BCM)

    myGreenLed = SingleColorLed(12,GPIO)
    myGreenLed.addEventListener(Event.EVT_COMPLETE,handle_events)
    myGreenLed.addEventListener(SingleColorLed.EVT_FLASH,handle_events)

    buzzer = Buzzer(16,GPIO)
    buzzer.addEventListener(Event.EVT_COMPLETE,handle_events)

    uSonic = Ultrasonic_HCSR04(13,6,GPIO)
    uSonic.addEventListener(Ultrasonic_HCSR04.EVT_OBJECT_DETECTED,handle_events)


    buzz = Process(target= buzzer.buzz,args= (404,1))
    light = Process(target= myGreenLed.flash,args = (2,0.5))
    sonic = Process(target= uSonic.trigger,args = [0.5])

    buzz.start()
    #light.start()
    sonic.start()
    #buzzer.buzz(800,0.2)



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
