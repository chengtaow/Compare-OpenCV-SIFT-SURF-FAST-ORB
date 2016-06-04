import cv2
import numpy as np
from matplotlib import pyplot as plt
import threading

cam = cv2.VideoCapture(0)
(ret, img) = cam.read()
img2 = img
img3 = img
img4 = img

def sift_thread():
	sift = cv2.xfeatures2d.SIFT_create()
	(kps, descs) = sift.detectAndCompute(gray, None)
	cv2.drawKeypoints(gray, kps, img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	cv2.imshow('SIFT Algorithm', img)


def surf_thread():
	surf = cv2.xfeatures2d.SURF_create()
	(kps2, descs2) = surf.detectAndCompute(gray, None)
	cv2.drawKeypoints(gray, kps2, img2, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	cv2.imshow('SURF Algorithm', img2)

def fast_thread():
	fast = cv2.FastFeatureDetector_create()
	kps3 = fast.detect(gray, None)
	cv2.drawKeypoints(gray, kps3, img3, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	cv2.imshow('FAST Algorithm', img3)

def orb_thread():
	orb = cv2.ORB_create()
	kps4 = orb.detect(gray, None)
	(kps4, des4) = orb.compute(gray, kps4)
	cv2.drawKeypoints(gray, kps4, img4, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	cv2.imshow('ORB Algorithm', img4)

while True:
	(ret, img) = cam.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	t1 = threading.Thread(name = 'SIFT Algorithm', target = sift_thread)
	t2 = threading.Thread(name = 'SURF Algorithm', target = surf_thread)
	t3 = threading.Thread(name = 'FAST Algorithm', target = fast_thread)
	t4 = threading.Thread(name = 'ORB Algorithm', target = orb_thread)
	t1.start()
	t2.start()
	t3.start()
	t4.start()
	t1.join()
	t2.join()
	t3.join()
	t4.join()

	if cv2.waitKey(1) == 27:
		break

cv2.destroyAllWindows()
