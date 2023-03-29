# import the necessary packages
import cv2


def GetPlate(frame, res, showImages):
	img = frame.array
	crop = img[int(res[1]*0.5):int(res[1]*0.95), int(res[0]*0.05):int(res[0]*0.9)]
	grayImg = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
	grayImg = cv2.bilateralFilter(grayImg, 11, 17, 17)
	edgedImg = cv2.Canny(grayImg, 30, 200)
	
	contours, new = cv2.findContours(edgedImg.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	img1 = crop.copy()
	cv2.drawContours(img1, contours, -1, (0, 255, 0), 3)
	
	
	contours = sorted(contours, key = cv2.contourArea, reverse = True)[:30]
	screenCnt = None
	img2 = crop.copy()
	cv2.drawContours(img2, contours, -1, (0, 255, 0), 3)
	
	count = 0
	idx = 7
	for c in contours:
		contour_perimeter = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.018 * contour_perimeter, True)
		screenCnt = approx
		# Look for contours with 4 corners
		if len(approx) == 4:
			screenCnt = approx
			x, y, w, h = cv2.boundingRect(c)
			plate = crop [ y: y + h, x: x + w]
			break
		else:
			plate = crop [ 0: 1, 0: 1] 

	# draws the license plate contour on original image
	cv2.drawContours(crop , [screenCnt], -1, (0, 255, 0), 3)
	if(showImages):
		cv2.imshow("img1", img1)
		cv2.imshow("img2", img2)
		cv2.imshow("detected license plate", crop )
		cv2.imshow("Plate", plate )
	
	return plate


cv2.destroyAllWindows()

