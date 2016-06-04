import cv2
import numpy as np
from matplotlib import pyplot as plt
import thread

cam = cv2.VideoCapture(0)
ret, img = cam.read()
img2 = img
img3 = img
img4 = img

def sift_thread( picname, delay):
	sift = cv2.xfeatures2d.SIFT_create()
	(kps, descs) = sift.detectAndCompute(gray, None)
	cv2.drawKeypoints(gray,kps,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	cv2.imshow( picname , img )


def surf_thread( picname2, delay):
	surf = cv2.xfeatures2d.SURF_create()
	(kps2, descs2) = surf.detectAndCompute(gray, None)
	cv2.drawKeypoints(gray,kps2,img2,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	cv2.imshow( picname2 , img2 )

def fast_thread( picname3, delay):
	fast = cv2.FastFeatureDetector_create()
	kps3 = fast.detect(gray, None)
	cv2.drawKeypoints(gray,kps3,img3,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	cv2.imshow( picname3, img3)

def orb_thread( picname4, delay):
	orb = cv2.ORB_create()
	kps4 = orb.detect(gray,None)
	kps4, des4 = orb.compute(gray, kps4)
	cv2.drawKeypoints(gray,kps4,img4,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	cv2.imshow( picname4,img4)

while True:
	ret, img = cam.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	try:
#		thread.start_new_thread( sift_thread, ("SIFT Algorithm", 0))
		thread.start_new_thread( surf_thread, ("SURF Algorithm", 0))
#		thread.start_new_thread( fast_thread, ("FAST Algorithm", 0))
		thread.start_new_thread( orb_thread, ("ORB Algorithm", 0))

	except:
		print "Error: unable to start thread"

	if cv2.waitKey(1) == 27:
		break
