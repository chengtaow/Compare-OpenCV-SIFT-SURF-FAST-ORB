# Compare-OpenCV-SIFT-SURF-FAST-ORB
A multi threaded Python program runs OpenCV SIFT SURF FAST ORB.

This program will get the video from the camera and use SIFT SURF FAST ORB algorithms to draw the keypoint.
The result let you compare different algorithms.

It runs under Ubuntu 14.04 and OpenCV 3.1.0.

To run:
$ python featuredetect.py

The image shows the result.
The SIFT provides the most accurate feature detection, while ORB and FAST requires the least computational time. The orientation is not computed in FAST. In real time feature matching problem, I will prefer ORB algorithm. 
