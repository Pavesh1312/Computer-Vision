import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Pavesh\OneDrive\Desktop\Pavesh Clg\Computer Vision\image.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.magnitude(sobelx, sobely)
cv2.imshow("Original", img)
cv2.imshow("Sobel Edge Detection", sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()
