import  cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)


while True:
    frame,img = cap.read()
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    green = np.uint8([[[0,255,0]]])
    # print(green)

    green_channel = img[:,:,1]
    print(green_channel)


    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255 ,255])
    mask = cv.inRange(hsv, lower_blue, upper_blue)


    # Range for lower red
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask1 = cv.inRange(hsv, lower_red, upper_red)

    # Range for upper range
    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv.inRange(hsv, lower_red, upper_red)

    mask3 = mask1+mask2

    # Segmenting out the detected red colored cloth
    #
    # mask4 = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    # mask5 = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))
    #
    # # creating an inverted mask to segment out the cloth from the frame
    # mask6 = cv2.bitwise_not(mask1)



    res = cv.bitwise_and(img,img,mask= mask)
    res1 = cv.bitwise_and(img,img,mask=mask3)
    res2 = cv.bitwise_and(img, img, mask=mask)

    cv.imshow('frame', img)
    cv.imshow('mask', mask)
    cv.imshow('mask1', mask3)
    cv.imshow('res1',res1 )

    if cv.waitKey(5) & 0xff == ord('q'):
        break


cv.destroyWindow()