import cv2
import numpy as np
import face_recognition


imgFinnur = face_recognition.load.image.file('Imagebasics/Finnur.png')
imgFinnur = cv2.cvtColor(imgFinnur,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load.image.file('Imagebasics/Finnur-test.png')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)


cv2.imshow('Finnur Gauti.',imgFinnur)
cv2.imshow('Finnur Gauti.',imgTest)
cv2.waitKey(0)