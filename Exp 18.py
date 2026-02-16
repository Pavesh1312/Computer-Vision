import cv2
img = cv2.imread(r"C:\Users\Pavesh\OneDrive\Desktop\Pavesh Clg\Computer Vision\image.png")
roi = img[100:300, 100:300]
img[300:500, 300:500] = roi
cv2.imshow("ROI Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
