import tensorflow as tf
import numpy as np
import cv2

clip = cv2.VideoCapture('2019-10-11 23-02-23.mp4')
count = 0

while clip.isOpened():
    checkFrame, frame = clip.read()
    # loop as long as there is a frame to read

    if checkFrame:

        count = count + 1
        print(str(count))

        cv2.imshow('frame', frame)
        cv2.waitKey(1)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #   break
    else:
        break

clip.release()
cv2.destroyAllWindows()
