import cv2
import numpy as np
def draw_circle():
    w = int(input("Enter width: "))
    h = int(input("Enter height: "))
    img = np.ones((h, w, 3), dtype=np.uint8) * 255
    cv2.circle(img, (w//2, h//2), min(w, h)//4, (0, 0, 0), -1)
    cv2.imshow("Circle Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
draw_circle()
