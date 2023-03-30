# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import pytesseract as tess
import cv2
import re
import camera as cameraScript
import barrier
import car
import carService

showImages = False  


camera = PiCamera()
res=(1280, 720)
camera.resolution = res
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=res)


time.sleep(0.1)
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    plateImg = cameraScript.GetPlate(frame, res, showImages)
    text = tess.image_to_string(plateImg)
    print(text)
    if(len(text) > 5):
        for car in carService.carList:
            if(car.getPlate() in text):
                carService.setToPayDB(car.getCarID(), 1.1)
                print("Otwieranie")
                barrier.OpenBarrier(car.getPlate(), car.getToPay())
                carService.getDBData()


    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
pwm.stop()
gp.cleanup()


