import cv2

img = cv2.imread(r"C:\Users\Pavesh\OneDrive\Desktop\Pavesh Clg\Computer Vision\image.png")

watermark = img.copy()
cv2.putText(watermark, "WATERMARK", (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1,
            (0, 0, 255), 2)

output = cv2.addWeighted(watermark, 0.5, img, 0.5, 0)

cv2.imshow("Watermarked Image", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
