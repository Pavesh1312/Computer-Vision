import cv2
cap = cv2.VideoCapture(r"C:\Users\Pavesh\OneDrive\Pictures\Camera Roll\WIN_20250901_08_13_44_Pro.mp4")
frames = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)
for f in reversed(frames):
    cv2.imshow("Reverse", f)
    if cv2.waitKey(100) == ord('q'): 
        break
cv2.destroyAllWindows()
