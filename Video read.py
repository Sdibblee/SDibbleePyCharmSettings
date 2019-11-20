import numpy
import cv2
from facecrop import facecrop

print(0xFF)
print(ord('q'))
count = 0
clip = cv2.VideoCapture('Test clip #1.mp4')

while clip.isOpened():
    checkframe, frame = clip.read()
    # loop as long as there is a frame to read

    if checkframe:
        count = count + 1
        print(str(count))
        # grycl = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # facecrop(grycl)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

clip.release()
cv2.destroyAllWindows()
