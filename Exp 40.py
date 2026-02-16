import cv2
cap = cv2.VideoCapture(r"C:\Users\Pavesh\Videos\Screen Recordings\Screen Recording 2026-01-28 122718.mp4")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Video Frames", frame)
    if cv2.waitKey(30) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
