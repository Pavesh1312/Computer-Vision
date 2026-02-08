import cv2
image = cv2.imread(r"C:\Users\Pavesh\OneDrive\Desktop\Pavesh Clg\Computer Vision\image.png")
blur = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow("Original Image", image)
cv2.imshow("Gaussian Blurred Image", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
