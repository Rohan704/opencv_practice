# import numpy as np
# import cv2
# img = cv2.imread("lena.jpg", -1)
# print(img)
# cv2.imshow('image', img)
# k = cv2.waitKey(0) & 0xff
#
# if k == 27:
#     cv2.destroyAllWindows()
# elif k == ord('s'):
#     cv2.imwrite('lena_copy.png', img)
#     cv2.destroyAllWindows()



# life stream capture image using cammera
import cv2
cap = cv2.VideoCapture(0);
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640, 480))
# print(cap.isOpened())

while(True):
    ret, frame = cap.read()
    imgcanny = cv2.Canny(frame, 100, 200)
    cv2.imshow('canny', frame)
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # out.write(frame)
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('gray', frame)

        imgcanny = cv2.Canny(frame, 100, 200)
        cv2.imshow('canny', frame)



cap.release()
cv2.destroyAllWindows()
#
# #
#qqqqs
#
# cap.release()
# cv2.destroyAllWindows()
#



# shape and ressize


# # # img = np.zeros([512, 512, 3], np.uint8)
# img = cv2.line(img , (0, 0), (177, 177), (147, 96, 44), 5)
# #
# img = cv2.arrowedLine(img, (0,255), (255,255), (255, 0, 0), 10)
# img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 10)
# font = cv2.FONT_HERSHEY_COMPLEX
# img = cv2.putText(img, 'openCv', (0, 500), font, 4, (0, 255, 255), 10, cv2.LINE_AA)
#
#
#
#
# import numpy as np
# import cv2
#
#
# kernel = np.ones((5,5), np.uint8)
# print(kernel)
#
#
# img = cv2.imread("lena.jpg")
# print(img.shape)
# cv2.imshow('img', img)
#
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray", gray)
# blur = cv2.GaussianBlur(img, (7,7), 0)
# cv2.imshow("blur", blur)
# imgcanny = cv2.Canny(img, 100, 200)
# cv2.imshow("imgcanny", imgcanny)
# dailation = cv2.dilate(img, kernel, iterations=1)
# cv2.imshow("dailation", dailation)
# Erasion = cv2.erode(img, kernel, iterations=1)
# cv2.imshow("erasion",Erasion)
# Blankimg = np.zeros((512,512), np.uint8)
# cv2.imshow("Blanking", Blankimg)
# cv2.waitKey(0)
#
# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture(0)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)
#
# def stackImages(imgArray,scale,lables=[]):
#     sizeW= imgArray[0][0].shape[1]
#     sizeH = imgArray[0][0].shape[0]
#     rows = len(imgArray)
#     cols = len(imgArray[0])
#     rowsAvailable = isinstance(imgArray[0], list)
#     width = imgArray[0][0].shape[1]
#     height = imgArray[0][0].shape[0]
#     if rowsAvailable:
#         for x in range ( 0, rows):
#             for y in range(0, cols):
#                 imgArray[x][y] = cv2.resize(imgArray[x][y], (sizeW, sizeH), None, scale, scale)
#                 if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
#         imageBlank = np.zeros((height, width, 3), np.uint8)
#         hor = [imageBlank]*rows
#         hor_con = [imageBlank]*rows
#         for x in range(0, rows):
#             hor[x] = np.hstack(imgArray[x])
#             hor_con[x] = np.concatenate(imgArray[x])
#         ver = np.vstack(hor)
#         ver_con = np.concatenate(hor)
#     else:
#         for x in range(0, rows):
#             imgArray[x] = cv2.resize(imgArray[x], (sizeW, sizeH), None, scale, scale)
#             if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
#         hor= np.hstack(imgArray)
#         hor_con= np.concatenate(imgArray)
#         ver = hor
#     if len(lables) != 0:
#         eachImgWidth= int(ver.shape[1] / cols)
#         eachImgHeight = int(ver.shape[0] / rows)
#         print(eachImgHeight)
#         for d in range(0, rows):
#             for c in range (0,cols):
#                 cv2.rectangle(ver,(c*eachImgWidth,eachImgHeight*d),(c*eachImgWidth+len(lables[d][c])*13+27,30+eachImgHeight*d),(255,255,255),cv2.FILLED)
#                 cv2.putText(ver,lables[d][c],(eachImgWidth*c+10,eachImgHeight*d+20),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,255),2)
#     return ver
#
# stackImages = stackImages(([img , gray]), 0.8)
# cv2.imshow("stacked ",stackImages)
#



# cv2.imshow("lena", img)
# cv2.imshow("GRAY", gray)
# cv2.imshow("blur", blur)
# cv2.imshow("Canny", imgcanny)
# cv2.imshow("dialation", dailation)
# cv2.imshow("Erasion", Erasion)
# cv2.imshow("blank_Image", Blankimg)
# cv2.waitKey(0)
