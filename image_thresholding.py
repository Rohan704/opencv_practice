# import numpy as np
# import cv2
#
# #change to your video path
# cap = cv2.VideoCapture(0)
#
# while(cap.isOpened()):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#
#
#     if (ret!=True):
#          break
#
#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     thres1 = cv2.threshold(frame,127,255,cv2.THRESH_BINARY)
#
#
#
#     # Display the resulting frame
#     cv2.imshow('frame', gray)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()


import  cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("data/cat.jpeg")
print(type(img))


def resized(img,scale_percent ):
    scale_percent = scale_percent # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized

resie = resized(img, 20)
print(resie)
cv2.imshow('resie', resie)

ret , thresh1 = cv2.threshold(resie,127,255,cv2.THRESH_BINARY)
ret , thresh2 = cv2.threshold(resie,127,255,cv2.THRESH_TOZERO)
ret , thresh3 = cv2.threshold(resie,127,255,cv2.THRESH_TOZERO_INV)
ret , thresh4 = cv2.threshold(resie,127,255,cv2.THRESH_TRUNC)
ret , thresh5 = cv2.threshold(resie,127,255,cv2.THRESH_BINARY_INV)


titles = ['Original Image','BINARY','Tozero','TOZERO_INV','TRUNC','BINARY_INV']
images = [resie, thresh1, thresh2,thresh3, thresh4,thresh5]


for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
    
plt.show()
    



# cv2.imshow('img' )
cv2.waitKey()

