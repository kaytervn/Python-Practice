import cv2 as cv

camera_device = 0
# -- 2. Read the video stream
cap = cv.VideoCapture(camera_device)
if not cap.isOpened:
    print("--(!)Error opening video capture")
    exit(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        print("--(!) No captured frame -- Break!")
        break
    cv.imshow("Video", frame)
    # Mã ASCII của ESC là 27
    if cv.waitKey(10) == 27:
        break
