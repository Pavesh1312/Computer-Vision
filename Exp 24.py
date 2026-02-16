import cv2
import numpy as np
image = cv2.imread("input.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Black Hat Result", blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()
