import cv2
cap = cv2.VideoCapture(r"C:\Users\Pavesh\OneDrive\Desktop\Pavesh Clg\Kaviya Kumara.mp4")
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter("reverse_output.avi",
                      cv2.VideoWriter_fourcc(*'XVID'),
                      fps, (width, height))
for i in range(frame_count-1, -1, -1):
    cap.set(cv2.CAP_PROP_POS_FRAMES, i)
    ret, frame = cap.read()
    if ret:
        out.write(frame)
cap.release()
out.release()
print("Reverse video created successfully!")
