import inspect,sys
import time
import RPi.GPIO as GPIO
from promus.media.Buzzer import Buzzer
from promus.led.SingleColorLed import SingleColorLed
from  promus.system.Environment import Environment
from promus.core.events import Event
from threading import Thread

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
        print evt.target.id() + " dispatched event:"+  evt.type
        return;

    env = Environment(False,GPIO, GPIO.BCM)
    myGreenLed = SingleColorLed(12,GPIO)
    myGreenLed.addEventListener(Event.EVT_COMPLETE,handle_events)
    myGreenLed.addEventListener(SingleColorLed.EVT_FLASH,handle_events)
    buzzer = Buzzer(16,GPIO)
    buzzer.addEventListener(Event.EVT_COMPLETE,handle_events)

    #myGreenLed.flash(3,0.5)
    #buzzer.buzz(404,1)

    buzz = Thread(target= buzzer.buzz,args= (404,4))
    light = Thread(target= myGreenLed.flash,args = (40,0.1))

    buzz.start()
    light.start()
    buzz.join()
    light.join()

    exit()


    #led = makeClassInstance("SingleColorLed",12,GPIO)
    #led.flash(3,1)
    #exit()

    led_routineID = env.createThread("SingleColorLed",12,GPIO)
    obj = env.getObjectByRoutineName(led_routineID)
    obj.addEventListener(Event.EVT_COMPLETE,handle_events)
    obj.addEventListener(SingleColorLed.EVT_FLASH,handle_events)

    led_routineID2 = env.createThread("Buzzer",16,GPIO)
    obj2 = env.getObjectByRoutineName(led_routineID2)
    obj2.addEventListener(Event.EVT_COMPLETE,handle_events)

    buzz = Thread(obj2.buzz,300,1)
    light = Thread(obj.flash,3,0.5)
    buzz.start()
    light.start()

    #obj2.buzz(300,1)
    #obj.flash(3,0.5)
    #obj2.buzz(404,1)
    #print env.objects()

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
