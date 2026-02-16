import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Pavesh\OneDrive\Desktop\Pavesh Clg\Computer Vision\image.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = np.array([0,100,100])
upper = np.array([10,255,255])
mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask))
cv2.imshow("Foreground Removed", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
