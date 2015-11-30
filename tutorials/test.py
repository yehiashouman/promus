import time
import RPi.GPIO as GPIO
import promus.led.SingleColorLed
import
import Environment from promus.system.Environmente

env = Environment(GPIO, GPIO.BCM)
myUltraSonicSensor = Ultrasonic_HCSR04(18,26,GPIO)

def ultraSonicHandler(evt):
{
    print evt.distance
    myGreenLed.on()

}
myUltraSonicSensor.addEventListener(Event.OBJECT_DETECTED,ultraSonicHandler)
myGreenLed = SingleColorLed(23,GPIO)

env.addObject(myGreenLed)
env.addObject(myUltraSonicSensor)

myUltraSonicSensor.trigger()
