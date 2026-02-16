import cv2
car_cascade = cv2.CascadeClassifier("haarcascade_car.xml")
if car_cascade.empty():
    print("Error: Cascade file not loaded")
    exit()
cap = cv2.VideoCapture(r"C:\Users\Pavesh\Downloads\12821026_3840_2160_60fps.mp4")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 3)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
    cv2.imshow("Vehicle Detection", frame)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()
