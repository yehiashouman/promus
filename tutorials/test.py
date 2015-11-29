import time
import RPi.GPIO as GPIO
import promus.led.SingleColorLed
import
import Environment from promus.system.Environmente

env = Environment(GPIO, GPIO.BCM)
myUltraSonicSensor = Ultrasonic_HCSR04(18,26,GPIO)
myUltraSonicSensor.addEventListener(Event.OBJECT_DETECTED,handler)
myGreenLed = SingleColorLed(23,GPIO)

env.addObject(myGreenLed)
env.addObject(myUltraSonicSensor)


def handler():
{
    myGreenLed.on()

}
