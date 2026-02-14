import cv2
import numpy as np
image = cv2.imread(r"C:\Users\Pavesh\OneDrive\Desktop\Pavesh Clg\Computer Vision\image.png")
rows, cols = image.shape[:2]
pts1 = np.float32([[56,65], [368,52], [28,387], [389,390]])
pts2 = np.float32([[0,0], [300,0], [0,300], [300,300]])
M = cv2.getPerspectiveTransform(pts1, pts2)
perspective = cv2.warpPerspective(image, M, (300,300))
cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformation", perspective)
cv2.waitKey(0)
cv2.destroyAllWindows()
