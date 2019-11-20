import numpy
import cv2
import dlib
import tensorflow as tf
import os
print('hello world')
numpyver = numpy.version.version
opencvver = cv2.getVersionString()
dlibver = dlib.__version__
tfver = tf.version
print('numpy version ' + numpyver + ' ')
print('opencv version ' + opencvver + ' ')
print('dlib version ' + dlibver + ' ')
print('tensorflow version ' + str(tfver) + ' ')
