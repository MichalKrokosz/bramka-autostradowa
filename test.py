import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)

gp.setup(17, gp.OUT)

gp.output(17 , gp.HIGH)
time.sleep(50000)


gp.cleanup()

