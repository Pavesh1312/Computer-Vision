import cv2

image = cv2.imread(r"C:\Users\Pavesh\OneDrive\Desktop\Pavesh Clg\Computer Vision\image.png")
rotated = cv2.rotate(image, cv2.ROTATE_180)

cv2.imshow("Original Image", image)
cv2.imshow("180 Degree Rotation", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
