import cv2
img = cv2.imread(r"C:\Users\Pavesh\OneDrive\Pictures\Camera Roll\WIN_20241112_11_37_52_Pro.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face = cv2.CascadeClassifier(
    cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
faces = face.detectMultiScale(gray,1.3,5)
print("Faces:", len(faces))
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
