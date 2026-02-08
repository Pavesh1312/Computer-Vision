import cv2
import matplotlib.pyplot as plt
image = cv2.imread(r"C:\Users\Pavesh\OneDrive\Desktop\Pavesh Clg\Computer Vision\image.png")
colors = ('b', 'g', 'r')
for i, color in enumerate(colors):
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
plt.title("Color Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.show()
