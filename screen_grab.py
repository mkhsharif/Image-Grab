import numpy as np
import cv2
from mss import mss
from PIL import ImageGrab
from PIL import Image


pts = {'x1': 500, 'y1': 400, 'x2': 1000, 'y2': 1000}
screen = {'top': 160, 'left': 160, 'width': 380, 'height': 300}
sct = mss()
cam = cv2.VideoCapture(1)
# save video recording

x = input('Enter 1 for ImageGrab, 2 for MSS, or 3 for Webcam: ')



while x == '1':
    img = ImageGrab.grab(bbox=(pts['x1'], pts['y1'], pts['x2'], pts['y2'])) # x1, y1, x2, y2 
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB) # color correction
    cv2.imshow('ImageGrab', frame)


    if cv2.waitKey(1) == 27:
        break

while x == '2':
    sct.get_pixels(screen)
    img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB) # color correction
    cv2.imshow('MSS', frame)

    if cv2.waitKey(1) == 27:
        break

while x == '3':
    ret, frame = cam.read()
    small = cv2.resize(frame, (0,0), fx=0.5, fy=0.5) # scale input down by 50%
    print(cam.read())
    roi = small[30:700, 240:720]  #[y1:y2, x1:x2], crop sides 
    egdes = cv2.Canny(roi, 500, 500)
    cv2.imshow('Cam Egdes', egdes)
    cv2.imshow('Cam Raw', roi)
    if not ret:
        break

    if cv2.waitKey(1) == 27:
        break


cam.release()
cv2.destroyAllWindows()
