import time
import RPi.GPIO as GPIO
import promus.led.SingleColorLed
import Environment from promus.system.Environmente

try:
    env = Environment(GPIO, GPIO.BCM)

    def ultraSonicHandler(evt):
    {
        print evt.target.id + " dispatched event:"+  evt.type +" with distance: "+ evt.distance
        myGreenLed.on()

    }
    myUltraSonicSensor.addEventListener(Event.OBJECT_DETECTED,ultraSonicHandler)

    env.addObject(SingleColorLed,(23,GPIO))
    env.addObject(Ultrasonic_HCSR04,(18,26,GPIO))

    myUltraSonicSensor.trigger()

except KeyboardInterrupt:
    print "exiting..."
    env.exit()
