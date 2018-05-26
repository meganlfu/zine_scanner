#okay,
#1. repo [x]
#2. hook up open cv, get it to take in paper and output dividing lines
#3. take diving lines and export them as images
import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('image.jpg',0)
#find edges, but only creases in paper
#show image then destroy
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
