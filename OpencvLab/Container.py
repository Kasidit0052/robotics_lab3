import cv2
import sys
import os.path

def detect(filename):
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 170, 255, cv2.THRESH_BINARY)
    cv2.imshow('Original image',image)
    cv2.imshow('Gray image', blackAndWhiteImage)
    cv2.waitKey()
    cv2.destroyAllWindows()

if len(sys.argv) != 2:
    sys.stderr.write("usage: detect.py <filename>\n")
    sys.exit(-1)
    
detect(sys.argv[1])