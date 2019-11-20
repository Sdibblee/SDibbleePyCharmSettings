import cv2
import numpy as np

def facecrop(img):

    modelfile = "opencv_face_detector_uint8.pb"
    configfile = "opencv_face_detector.pbtxt"
    net = cv2.dnn.readNetFromTensorflow(modelfile, configfile)

    minisize = (img.shape[0], img.shape[1])
    # height is img.shape[0], width is img.shape[1]]
    miniframe = cv2.resize(img, minisize)

    blob = cv2.dnn.blobFromImage(miniframe, 1.0, (300, 300), [104, 117, 123], False, False)
    (frameHeight, frameWidth) = miniframe.shape[:2]
    net.setInput(blob)
    detections = net.forward()
    # bBoxes = []
    # gryCl = cv2.cvtColor(miniframe, cv2.COLOR_BGR2GRAY)
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            xstart = int(detections[0, 0, i, 3] * frameWidth)
            ystart = int(detections[0, 0, i, 4] * frameHeight)
            xend = int(detections[0, 0, i, 5] * frameWidth)
            yend = int(detections[0, 0, i, 6] * frameHeight)
            cv2.rectangle(miniframe, (xstart, ystart), (xend, yend), (255, 0, 0), 2)
        # sub_face = img[y:y+h, x+x+w]
        # face_file_name = "faces/face_" + str(y) + ".jpg"
        # print(face_file_name)
        # str(y) is a vertex coordinate, awful way to name
        # cv2.imwrite(face_file_name, sub_face)
    # print('Attempt at facecrop')
    # cv2.imshow('image', img)
    # while cv2.waitKey(1) & 0xFF != ord('q'):
        # cv2.waitKey(1)
    return
