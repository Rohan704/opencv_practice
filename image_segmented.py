import cv2 as cv
import numpy as np
import imutils

capture = cv.VideoCapture('output.avi')

while True:
    ret, img = capture.read()
    img = imutils.resize(img, width=350)
    cv.imshow('Input Image', img)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
    # noise removal
    kernel = np.ones((11, 11), np.uint8)
    opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=3)
    # sure background area
    sure_bg = cv.dilate(opening, kernel, iterations=3)
    # Finding sure foreground area
    dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
    ret, sure_fg = cv.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv.subtract(sure_bg, sure_fg)

    # Marker labelling
    ret, markers = cv.connectedComponents(sure_fg)
    # markers = np.uint8(markers)
    # Add one to all labels so that sure background is not 0, but 1
    markers = markers + 14
    # Now, mark the region of unknown with zero
    markers[unknown == 255] = 0

    markers = cv.watershed(img, markers)
    img[markers == -1] = [255, 0, 0]

    cv.imshow('Image', img)
    cv.imshow('Gray', gray)
    cv.imshow('Threshold', thresh)
    cv.imshow('Opening Morphology', opening)
    cv.imshow('Dialation Morphology(Background)', sure_bg)
    cv.imshow('Distance Transform(Gradient)', dist_transform)
    cv.imshow('Dis_trans(Threshold)', sure_fg)
    cv.imshow('Subtraction(Background:Dialation - Foreground:Threshold:Dis_transform)', unknown)
    # cv.imshow('Markers(Connected Components',markers)
    cv.imshow('Segmented Image', img)

    cv.waitKey(1)
    # print(frame)
    # if cv.waitKey(1) == ord('q'):
    #     break

capture.release()
cv.destroyAllWindows()


