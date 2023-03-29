import RPi.GPIO as gp
from time import sleep

from board import SCL, SDA
import busio
from oled_text import OledText, BigLine, SmallLine


i2c = busio.I2C(SCL, SDA)
oled = OledText(i2c, 128, 64)
oled.layout = {
    1: BigLine(8, 5, size=26),
    2: SmallLine(0, 40)
    }

sPin=18
redPin=23
greenPin=24
gp.setup(sPin, gp.OUT)
gp.setup(redPin, gp.OUT)
gp.setup(greenPin, gp.OUT)
gp.output(redPin, gp.HIGH)



pwm=gp.PWM(sPin, 50)
pwm.start(0)

def SetAngle(angle):
    duty = angle / 18 + 2
    gp.output(sPin, True)
    pwm.ChangeDutyCycle(duty)
    sleep(.5)
    gp.output(sPin, False)
    pwm.ChangeDutyCycle(0)

def OpenBarrier(plateStr, toPay):
    oled.text(plateStr, 1)
    oled.text("Do zapaty: " + str(toPay) + "zl", 2)
    sleep(.5)
    gp.output(redPin, gp.LOW)
    gp.output(greenPin, gp.HIGH)
    SetAngle(8)
    sleep(4)
    gp.output(greenPin, gp.LOW)
    gp.output(redPin, gp.HIGH)
    SetAngle(90)
    oled.clear()





