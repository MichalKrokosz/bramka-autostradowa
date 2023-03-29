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

carList = []
carList.append(car.Car("Smigacz", "SB 841AL", 13.45))
carList.append(car.Car("Czrnuch", "WCI 48323", 1.20))



showImages = False  

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
res=(1280, 720)
camera.resolution = res
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=res)


time.sleep(0.1)
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	plateImg = cameraScript.GetPlate(frame, res, showImages)
	#barrier.OpenBarrier()
	
	text = tess.image_to_string(plateImg)
	#text = "f7e3h 7daSB 841ALfWE R*76fd "
	#tablicaStr = re.search("[A-Z][A-Z]\s\w\w\w\w\w", text)
	#plateTag = re.match("\w\w\w\w\w\w", text)
	print(text)
	if(len(text) > 5):
		for car in carList:
			if(car.getPlate() in text):
				print("Otwieranie")
				barrier.OpenBarrier(car.getPlate(), car.getToPay())
	
	
	
	
	key = cv2.waitKey(1) & 0xFF
	rawCapture.truncate(0)
	if key == ord("q"):
		break
	
	
	
cv2.destroyAllWindows()
pwm.stop()
gp.cleanup()


