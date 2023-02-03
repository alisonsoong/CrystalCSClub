#import the necessary packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time
import glob
import math
import qrcode


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
	help="max buffer size")
args = vars(ap.parse_args())

pts = deque(maxlen=args["buffer"])
# if a video path was not supplied, grab the reference
# to the webcam
if not args.get("video", False):
	vs = VideoStream(src=0).start()
# otherwise, grab a reference to the video file
else:
	vs = cv2.VideoCapture(args["video"])
# allow the camera or video file to warm up
print(len(args))
vs = cv2.VideoCapture(0)
time.sleep(2.0)
print(vs)


# # if we are not using a video file, stop the camera video stream
# if not args.get("video", False):
# 	vs.stop()
# # otherwise, release the camera
# else:
# 	vs.release()
# # close all windows
# cv2.destroyAllWindows()